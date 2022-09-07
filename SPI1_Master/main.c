#include <stdint.h>
#include "inc\tm4c123gh6pm.h"

void SPI1_init(void);
void SSI1Write(unsigned char data);

void main(void)
{
    unsigned char val='A';
    SPI1_init();
    while(1){
        SSI1Write(val);
    }

//	return 0;
}

void SPI1_init(void){

    /* enable clock for spi1 GPIO D and GPIO F*/

    SYSCTL_RCGCSSI_R =0x2;        // set clock enabling for spi1
    SYSCTL_RCGCGPIO_R |=(1<<3);  // enable clock to GPIO D for SPI1
    unsigned char delay=SYSCTL_RCGCSSI_R ;


    // Initialize PD3 and PD0 for SPI1 alternate function

    GPIO_PORTD_LOCK_R =0x4C4F434B; // write this value in GPIO LOCK register to unlock GPIOFCR register
    GPIO_PORTD_CR_R=0xFF;         // Allow changes to registers (GPIOAFSEL, GPIOPUR, GPIOPDR, or GPIODEN)

    GPIO_PORTD_AFSEL_R |=0x0F; //  enable alternate function of PD0 PD1 PD2 PD3
    GPIO_PORTD_PCTL_R &=~0x00002222;   // assign PD0 PD1 PD2  PD3 pins to SPI1
    GPIO_PORTD_PCTL_R |=0x00002222;   // assign PD0 PD1 PD2  PD3 pins to SPI1
    GPIO_PORTD_AMSEL_R &=~0x0F;  // disable analog function
    GPIO_PORTD_DEN_R |=0x0F;    // set PD0 PD1 PD2 PD3 as digital pins

    SSI1_CR1_R = 0;              // Disable SPI and configure it as a master POL = 0, PHA = 0
    SSI1_CC_R = 0;              // Select the SPI Baud Clock Source as system clock
    SSI1_CPSR_R = 4;           //  prescaler -> divided by 4
    SSI1_CR0_R = 0x0007;      //  4 MHz SSI clock, SPI mode, 8 bit data  BR= SYSCLK/(CPSDVSR * (1+SCR) )
    SSI1_CR1_R |= 2;         //   Enable SPI


}

void SSI1Write(unsigned char data)
{
    GPIO_PORTD_DATA_R &=~ (1<<1);       // assert SS low
    while((SSI1_SR_R & 2)==0);         // wait until FIFO not full
    SSI1_DR_R = data;                 // transmit high byte
    while(SSI1_SR_R & 0x10);         // wait until transmit complete
    GPIO_PORTD_DATA_R |= (1<<1);    // keep SS idle high
}
