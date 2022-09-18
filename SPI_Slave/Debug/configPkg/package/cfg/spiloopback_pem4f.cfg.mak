# invoke SourceDir generated makefile for spiloopback.pem4f
spiloopback.pem4f: .libraries,spiloopback.pem4f
.libraries,spiloopback.pem4f: package/cfg/spiloopback_pem4f.xdl
	$(MAKE) -f E:\ti\spiloopback_EK_TM4C123GXL_TI/src/makefile.libs

clean::
	$(MAKE) -f E:\ti\spiloopback_EK_TM4C123GXL_TI/src/makefile.libs clean

