---
layout: page
title: Dolphin EMU
permalink: /dolphin-emu/
--- 

While playing Wind Waker in Dolphin, I ran into a error that proceded to crash Dolphin.

> Incomplete cleanup! (regs)

<https://github.com/dolphin-emu/dolphin/blob/4c004b6dc978d7585bf0765e22351ef1edd39a3a/Source/Core/Core/PowerPC/Jit64IL/IR_X86.cpp#L2337>

I "Fixed" this by going to the Config and changing the CPU Emulator setting from JITIL to JIT.
