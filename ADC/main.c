#include <stdint.h>
#include "inc\tm4c123gh6pm.h"


void adc_init();
void SPI1_init(void);
void SSI1Write(unsigned char data);
void Delay(unsigned long counter);


int main(){
   volatile long ADC_Output=0;
   volatile long temp_c=0;

   adc_init();
   SPI1_init();

      while(1){
          ADC0_PSSI_R |= 0x8;                                 //Initiate SS3
          while ((ADC0_RIS_R & 0x8) == 0);                   // Wait for conversion done
          ADC_Output = ADC0_SSFIFO3_R & 0xFFF;              // Read output
          temp_c = 147.5 - ((247.5 * ADC_Output) / 4096);  // Convert read value to be in celsius
          ADC0_ISC_R = 0x8;                               //  Acknowledge complete  , deassert the flag
          SSI1Write(temp_c);                             //  send temp
          Delay(100000);                                //   delay
      }

}


void adc_init(){

    SYSCTL_RCGC0_R |=0x00010000;  // Activate ADC0 ,bit 16 if RCGC register
    Delay(1);
    SYSCTL_RCGC0_R &=~0x00000300; // Configure the samplin rate default value of 125K bit 8 and 9
    ADC0_SSPRI_R &=~0xF000;      // set priority of sequencer 3 the highest one zeros at bits 15-12
    ADC0_ACTSS_R &=~0x8;        // Disable sequencer 3 during configuration
    ADC0_EMUX_R &=~0xF000;     //  make sequencer 3 triggered software/start 0x0 at bits 0-3
    ADC0_SSMUX3_R=0x0;        // Get input from channel 0
    ADC0_SSCTL3_R |=0x0E;    // enable temperature measurment
    ADC0_ACTSS_R |=0x8;     // enable sequencer 3

}

void Delay(unsigned long counter){
    unsigned long i = 0;
    for(i=0; i< counter; i++);
}

void SPI1_init(void){

    /* Enable clock for spi1 GPIO D */
    SYSCTL_RCGCSSI_R |=0x2;                        // set clock enabling for spi1
    SYSCTL_RCGCGPIO_R |=(1<<3);                   // enable clock to GPIO D for SPI1
    Delay(1);                                    // to make sure clock reach spi module and GPIO port D


    /* Initialize PD3 and PD0 for SPI1 alternate function */
    GPIO_PORTD_AFSEL_R |=0x0D;                 //  enable alternate function of PD0 PD2 PD3
    GPIO_PORTD_PCTL_R &=~0x00002202;          // clear PD0 PD1 PD2  PD3 pins to use as alternative function
    GPIO_PORTD_PCTL_R |=0x00002202;          // enable alternative function  PD0 PD1 PD2  PD3 pins to SPI1
    GPIO_PORTD_DEN_R |=0x0F;                // set PD0 PD1 PD2 PD3 as digital pins
    GPIO_PORTD_AMSEL_R &=~0x0F;            // disable analog function
    GPIO_PORTD_LOCK_R =0x4C4F434B;        // write this value in GPIO LOCK register to unlock GPIOFCR register
    GPIO_PORTD_CR_R=0xFF;                // Allow changes to registers (GPIOAFSEL, GPIOPUR, GPIOPDR, or GPIODEN)
    GPIO_PORTD_DIR_R |=0x02;            // set the direction of 2nd bit in Port D as output


    /* Initialize SPI1 */
    SSI1_CR1_R = 0x4;            // Disable SPI and configure it as a slave POL = 0, PHA = 0
    SSI1_CC_R = 0;              // Select the SPI Baud Clock Source as system clock
    SSI1_CPSR_R = 4;           //  prescaler -> divided by 4
    SSI1_CR0_R = 0x0007;      //  4 MHz SSI clock, SPI mode, 8 bit data  BR= SYSCLK/(CPSDVSR * (1+SCR) )
    SSI1_CR1_R |= 2;         //   Enable SPI
}

void SSI1Write(unsigned char data)
{
    while((SSI1_SR_R & 2)==0);     // wait until FIFO not full
    SSI1_DR_R = data;             // transmit high byte
    while(SSI1_SR_R & 0x10);     // wait until transmit complete
}
