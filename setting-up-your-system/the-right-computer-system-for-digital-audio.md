# The Right Computer System for Digital Audio
It is nice to think that one could just go and buy any computer, install
a bit of software on it and start using it to record and create music.
This idea isn\'t necessarily wrong, but there are some important details
that it misses. Any computer that can be bought today (since somewhere
around the end of 2012) is capable of recording and processing a lot of
audio data. It will come with a builtin audio interface that can accept
inputs from microphones and/or electrical instruments; it will have a
disk with a huge amount of space for storing audio files.

However, when recording, editing and mixing music, it is generally
desirable to have very little [latency]{.dfn} between the time a sound
is generated and when it can be heard. When the audio signal flows
through a computer, that means that the computer has to be able to
receive the signal, process it and send it back out again as quickly as
possible. And this is where it becomes very important *what* computer
system is being used for this task, because it is **absolutely not** the
case that *any* computer can do it well.

Routing audio through a computer will always cause some delay, but if it
is small, it will generally never be noticed. There are also ways to
work in which the delay does not matter at all (for example, not sending
the output from the computer to speakers).

The latency that is typically needed for working with digital audio is
in the 1--5 ms range. For comparison, if one is sitting 1 m (3 ft) from
a set of speakers, the time the sound takes to reach the ears is about
3 ms. Any modern computer can limit the delay to 100 ms; most can keep
it under 50 ms. Many will be able to get down to 10 ms without too much
effort. Attempting to reduce the latency on a computer that cannot
physically do it will cause clicks and glitches in the audio, which is
clearly undesirable.

## Hardware-related Considerations

|  |  |
|----|----|
| Video interface | Poorly engineered video interfaces (and/or their device drivers) can \"steal\" computer resources for a long time, preventing the audio interface from keeping up with the flow of data. |
| Wireless interface | Poorly engineered wireless networking interfaces (and/or their device drivers) can also block the audio interface from keeping up with the flow of data. |
| [USB]{.abbr title="Universal Serial Bus"} ports | When using an audio interface connected via USB, and sometimes even if not, the precise configuration of the system\'s USB ports can make a big difference. There are many cases where plugging the interface into one port will work, but using different USB port results in much worse performance. This has been seen even on Apple systems. |
| Internal USB Hubs | Ideally, all USB ports should connect directly to the main bus inside the computer. Some laptops (and possibly some desktop systems) come wired with an internal USB hub between the ports and the system bus, which can then cause problems for various kinds of external USB devices, including some models of audio interfaces. It is very difficult to discover whether this is true or not, without simply trying it out. |
| [CPU]{.abbr title="Central Processing Unit"} speed control | Handling audio with low latency requires that the processor keeps running at its highest speed at all times. Many portable systems try to regulate processor speed in order to save power---for low latency audio, this should be totally disabled, either in the BIOS or at the OS level. |
| Excessive Interrupt Sharing | If the audio interface is forced by the computer to share an interrupt line (basically a way to tell the CPU that something needs its attention) with too many other (or wrong) devices, this can also prevent the audio interface from keeping up with the flow of data. In laptops it is generally impossible to do anything about this. In many desktop systems, it is possible at the BIOS level to reassign interrupts to work around the problem. |
| [SMI]{.abbr title="System Management Interrupt"}s | SMIs are interrupts sent by the motherboard to tell the computer about the state of various hardware. They cannot safely be disabled, and they can take a relatively long time to process. It is better to have a motherboard which never sends SMIs at all---this is also a requirement for realtime stock trading systems, which have similar issues with latency. |
| Hyperthreading | This technology is becoming less common as actual multi-core CPUs become the norm, but it still exists and is generally not good for realtime performance. Sometimes this can be disabled in the BIOS, sometimes it cannot. A processor that uses hyperthreading will be less stable in very low latency situations than one without. |
| Excessive vibration | This doesn\'t affect the flow of data to or from the audio interface, but it can cause the flow of data to and from (spinning) disk storage to become *much* slower. If a computer going to be used in an environment with loud live sound (specifically, high bass volume), make sure it is placed so that the disk is not subjected to noticeable vibration. The vibrations will physically displace the read-write heads of disk, and the resulting errors will force a retry of the reading from the disk. Retrying over and over massively reduces the rate at which data can be read from the disk. Avoid this.If you find this hard to believe, check out [this video](https://www.youtube.com/watch?v=tDacjrSCeq4) which shows the effects of merely shouting at your drives. This is likely not an issue with contemporary SSD drives, which have no spinning/head mechanisms. |

Richard Ames presents a long (28 minutes)
[video](https://www.youtube.com/watch?v=GUsLLEkswzE) that is very
helpful if you want to understand these issues in more depth. It is a
little bit Windows-centric, but the explanations apply to all types of
computers and operating systems.
