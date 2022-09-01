#include <stdint.h>
#include "inc\tm4c123gh6pm.h"

void SPI_master(void);
void SSI1Write(unsigned char data);
void SystemInit(void);

int main(void)
{
    unsigned char i;
    SPI_master();
    for(;;)
    {
    for (i = 'A'; i <= 'Z'; i++)
    {
        SSI1Write('A'); /* write a character */
    }
    }


}





void SPI_master(void)
{
    SYSCTL_RCGCSSI_R |= 2;             // Enable and provide a clock to SPI1
    SYSCTL_RCGCGPIO_R  |= 0x8;       // Enable and provide a clock to GPIO PortD

    /* configure PORTD 3, 0 for SSI1 clock and Tx */
    GPIO_PORTD_AMSEL_R &= ~0x09;
    GPIO_PORTD_DEN_R |= 0x09;
    GPIO_PORTD_AFSEL_R  |= 0x09;
    GPIO_PORTD_PCTL_R &= ~0x0000F00F;
    GPIO_PORTD_PCTL_R |= 0x00002002;

    /* configure PORTF 2 for slave select */
//    GPIO_PORTF_DEN_R |= 0x04;
//    GPIO_PORTF_DIR_R |= 0x04;
//    GPIO_PORTF_DATA_R |= 0x04;


    /* SPI Master, POL = 0, PHA = 0, clock = 4 MHz, 16 bit data */
    SSI1_CR1_R = 0;              // Disable SPI and configure it as a master
    SSI1_CC_R = 0;              // Select the SPI Baud Clock Source as system clock
    SSI1_CPSR_R = 2;           //  prescaler divided by 2
    SSI1_CR0_R = 0x0007;      //  8 MHz SSI clock, SPI mode, 8 bit data  BR= SYSCLK/(CPSDVSR * (1+SCR) )
    SSI0_CR1_R |= 2;         // Enable SPI


}

void SSI1Write(unsigned char data)
{
    GPIO_PORTF_DATA_R &= ~0x04;        // assert SS low
    while((SSI1_SR_R & 2) == 0);      // wait until FIFO not full
    SSI1_SR_R = data;                // transmit high byte
    while(SSI1_SR_R & 0x10);        // wait until transmit complete
    GPIO_PORTF_DATA_R |= 0x04;     // keep SS idle high
}



void SystemInit(void)
{
    /* Grant co processor access */
    /* This is required since TM4C123G has a floating point coprocessor */
    NVIC_CPAC_R  |= 0x00f00000;
}

