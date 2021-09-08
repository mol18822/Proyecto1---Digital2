#ifndef __I2C_H
#define	__I2C_H
#include <xc.h> 
#include <pic16f887.h>
#include <stdint.h>
#ifndef _XTAL_FREQ
#define _XTAL_FREQ 8000000
#endif

// ---------------------- Iniciando I2C Master --------------------------------

void I2C_Master_Init(const unsigned long c);

// ------------------------ Send/Receive Data ---------------------------------

void I2C_Master_Wait(void);

// --------------------- Initialize de comunicaci�n I2C -----------------------

void I2C_Master_Start(void);

// --------------------- Reset de comunicaci�n I2C ----------------------------

void I2C_Master_RepeatedStart(void);

// ------------------------ Stop I2C comunicaci�n -----------------------------

void I2C_Master_Stop(void);

// ---------------- Transmisi�n de datos de Master a Slave --------------------

void I2C_Master_Write(unsigned d);

// ---------------- Transmisi�n de datos de Slave a Master --------------------

unsigned short I2C_Master_Read(unsigned short a);

// ----------------------- Iniciando I2C Slave --------------------------------

void I2C_Slave_Init(uint8_t address);

#endif	