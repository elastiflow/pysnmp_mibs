# SNMP MIB module (NDS-DTH3-IPSTREAMER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-IPSTREAMER.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ndsDTH3Encoder = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpStreamer_ObjectIdentity = ObjectIdentity
ipStreamer = _IpStreamer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20)
)
_IpStreamerStatusTable_Object = MibTable
ipStreamerStatusTable = _IpStreamerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 1)
)
if mibBuilder.loadTexts:
    ipStreamerStatusTable.setStatus("current")
_IpStreamerStatusEntry_Object = MibTableRow
ipStreamerStatusEntry = _IpStreamerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 1, 1)
)
ipStreamerStatusEntry.setIndexNames(
    (0, "NDS-DTH3-IPSTREAMER", "ipStreamerStatusModuleIndex"),
)
if mibBuilder.loadTexts:
    ipStreamerStatusEntry.setStatus("current")


class _IpStreamerStatusModuleIndex_Type(Integer32):
    """Custom type ipStreamerStatusModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IpStreamerStatusModuleIndex_Type.__name__ = "Integer32"
_IpStreamerStatusModuleIndex_Object = MibTableColumn
ipStreamerStatusModuleIndex = _IpStreamerStatusModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 1, 1, 1),
    _IpStreamerStatusModuleIndex_Type()
)
ipStreamerStatusModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStreamerStatusModuleIndex.setStatus("current")


class _IpStreamerSoftwareRelease_Type(DisplayString):
    """Custom type ipStreamerSoftwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IpStreamerSoftwareRelease_Type.__name__ = "DisplayString"
_IpStreamerSoftwareRelease_Object = MibTableColumn
ipStreamerSoftwareRelease = _IpStreamerSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 1, 1, 2),
    _IpStreamerSoftwareRelease_Type()
)
ipStreamerSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStreamerSoftwareRelease.setStatus("current")


class _IpStreamerAlarmStatus_Type(Integer32):
    """Custom type ipStreamerAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpStreamerAlarmStatus_Type.__name__ = "Integer32"
_IpStreamerAlarmStatus_Object = MibTableColumn
ipStreamerAlarmStatus = _IpStreamerAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 1, 1, 3),
    _IpStreamerAlarmStatus_Type()
)
ipStreamerAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStreamerAlarmStatus.setStatus("current")


class _IpStreamerHeartBeat_Type(Integer32):
    """Custom type ipStreamerHeartBeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpStreamerHeartBeat_Type.__name__ = "Integer32"
_IpStreamerHeartBeat_Object = MibTableColumn
ipStreamerHeartBeat = _IpStreamerHeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 1, 1, 4),
    _IpStreamerHeartBeat_Type()
)
ipStreamerHeartBeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStreamerHeartBeat.setStatus("current")
_IpStreamernextTimeDate_Type = DateAndTime
_IpStreamernextTimeDate_Object = MibTableColumn
ipStreamernextTimeDate = _IpStreamernextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 1, 1, 5),
    _IpStreamernextTimeDate_Type()
)
ipStreamernextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamernextTimeDate.setStatus("current")
_IpStreamerTable_Object = MibTable
ipStreamerTable = _IpStreamerTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2)
)
if mibBuilder.loadTexts:
    ipStreamerTable.setStatus("current")
_IpStreamerEntry_Object = MibTableRow
ipStreamerEntry = _IpStreamerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1)
)
ipStreamerEntry.setIndexNames(
    (0, "NDS-DTH3-IPSTREAMER", "ipStreamerModuleIndex"),
    (0, "NDS-DTH3-IPSTREAMER", "ipStreamerCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    ipStreamerEntry.setStatus("current")


class _IpStreamerCurrentNextIndex_Type(Integer32):
    """Custom type ipStreamerCurrentNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-current", 1),
          ("index-next", 2))
    )


_IpStreamerCurrentNextIndex_Type.__name__ = "Integer32"
_IpStreamerCurrentNextIndex_Object = MibTableColumn
ipStreamerCurrentNextIndex = _IpStreamerCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 1),
    _IpStreamerCurrentNextIndex_Type()
)
ipStreamerCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStreamerCurrentNextIndex.setStatus("current")


class _IpStreamerModuleIndex_Type(Integer32):
    """Custom type ipStreamerModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IpStreamerModuleIndex_Type.__name__ = "Integer32"
_IpStreamerModuleIndex_Object = MibTableColumn
ipStreamerModuleIndex = _IpStreamerModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 2),
    _IpStreamerModuleIndex_Type()
)
ipStreamerModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStreamerModuleIndex.setStatus("current")
_IpStreamerOwnIPAddress_Type = IpAddress
_IpStreamerOwnIPAddress_Object = MibTableColumn
ipStreamerOwnIPAddress = _IpStreamerOwnIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 3),
    _IpStreamerOwnIPAddress_Type()
)
ipStreamerOwnIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerOwnIPAddress.setStatus("current")
_IpStreamerNetworkMask_Type = IpAddress
_IpStreamerNetworkMask_Object = MibTableColumn
ipStreamerNetworkMask = _IpStreamerNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 4),
    _IpStreamerNetworkMask_Type()
)
ipStreamerNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerNetworkMask.setStatus("current")
_IpStreamerRouterIPAddress_Type = IpAddress
_IpStreamerRouterIPAddress_Object = MibTableColumn
ipStreamerRouterIPAddress = _IpStreamerRouterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 5),
    _IpStreamerRouterIPAddress_Type()
)
ipStreamerRouterIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerRouterIPAddress.setStatus("current")
_IpStreamerDestinationIPAddress_Type = IpAddress
_IpStreamerDestinationIPAddress_Object = MibTableColumn
ipStreamerDestinationIPAddress = _IpStreamerDestinationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 6),
    _IpStreamerDestinationIPAddress_Type()
)
ipStreamerDestinationIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerDestinationIPAddress.setStatus("current")


class _IpStreamerDestinationUDPPort_Type(Integer32):
    """Custom type ipStreamerDestinationUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpStreamerDestinationUDPPort_Type.__name__ = "Integer32"
_IpStreamerDestinationUDPPort_Object = MibTableColumn
ipStreamerDestinationUDPPort = _IpStreamerDestinationUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 7),
    _IpStreamerDestinationUDPPort_Type()
)
ipStreamerDestinationUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerDestinationUDPPort.setStatus("current")


class _IpStreamerTSPacketsPerUDPFrame_Type(Integer32):
    """Custom type ipStreamerTSPacketsPerUDPFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IpStreamerTSPacketsPerUDPFrame_Type.__name__ = "Integer32"
_IpStreamerTSPacketsPerUDPFrame_Object = MibTableColumn
ipStreamerTSPacketsPerUDPFrame = _IpStreamerTSPacketsPerUDPFrame_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 8),
    _IpStreamerTSPacketsPerUDPFrame_Type()
)
ipStreamerTSPacketsPerUDPFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerTSPacketsPerUDPFrame.setStatus("current")
_IpStreamerMulticastIPAddress_Type = IpAddress
_IpStreamerMulticastIPAddress_Object = MibTableColumn
ipStreamerMulticastIPAddress = _IpStreamerMulticastIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 9),
    _IpStreamerMulticastIPAddress_Type()
)
ipStreamerMulticastIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerMulticastIPAddress.setStatus("current")


class _IpStreamerTimeToLive_Type(Integer32):
    """Custom type ipStreamerTimeToLive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpStreamerTimeToLive_Type.__name__ = "Integer32"
_IpStreamerTimeToLive_Object = MibTableColumn
ipStreamerTimeToLive = _IpStreamerTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 10),
    _IpStreamerTimeToLive_Type()
)
ipStreamerTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerTimeToLive.setStatus("current")


class _IpStreamerTypeOfService_Type(Integer32):
    """Custom type ipStreamerTypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpStreamerTypeOfService_Type.__name__ = "Integer32"
_IpStreamerTypeOfService_Object = MibTableColumn
ipStreamerTypeOfService = _IpStreamerTypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 11),
    _IpStreamerTypeOfService_Type()
)
ipStreamerTypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerTypeOfService.setStatus("current")
_IpStreamerListenMulticastIPAddress_Type = IpAddress
_IpStreamerListenMulticastIPAddress_Object = MibTableColumn
ipStreamerListenMulticastIPAddress = _IpStreamerListenMulticastIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 12),
    _IpStreamerListenMulticastIPAddress_Type()
)
ipStreamerListenMulticastIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerListenMulticastIPAddress.setStatus("current")


class _IpStreamerListenUDPPort_Type(Integer32):
    """Custom type ipStreamerListenUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpStreamerListenUDPPort_Type.__name__ = "Integer32"
_IpStreamerListenUDPPort_Object = MibTableColumn
ipStreamerListenUDPPort = _IpStreamerListenUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 13),
    _IpStreamerListenUDPPort_Type()
)
ipStreamerListenUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerListenUDPPort.setStatus("current")
_IpStreamerLastReceivedFromIP_Type = IpAddress
_IpStreamerLastReceivedFromIP_Object = MibTableColumn
ipStreamerLastReceivedFromIP = _IpStreamerLastReceivedFromIP_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 14),
    _IpStreamerLastReceivedFromIP_Type()
)
ipStreamerLastReceivedFromIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipStreamerLastReceivedFromIP.setStatus("current")


class _IpStreamerRxOutput_Type(Integer32):
    """Custom type ipStreamerRxOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hotlink", 1),
          ("c-row", 2),
          ("b-row", 4))
    )


_IpStreamerRxOutput_Type.__name__ = "Integer32"
_IpStreamerRxOutput_Object = MibTableColumn
ipStreamerRxOutput = _IpStreamerRxOutput_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 15),
    _IpStreamerRxOutput_Type()
)
ipStreamerRxOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerRxOutput.setStatus("current")


class _IpStreamerTxSource_Type(Integer32):
    """Custom type ipStreamerTxSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hotlink1", 1),
          ("hotlink2", 2),
          ("a-row", 4))
    )


_IpStreamerTxSource_Type.__name__ = "Integer32"
_IpStreamerTxSource_Object = MibTableColumn
ipStreamerTxSource = _IpStreamerTxSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 16),
    _IpStreamerTxSource_Type()
)
ipStreamerTxSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerTxSource.setStatus("current")


class _IpStreamerPowerupDelay_Type(Integer32):
    """Custom type ipStreamerPowerupDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpStreamerPowerupDelay_Type.__name__ = "Integer32"
_IpStreamerPowerupDelay_Object = MibTableColumn
ipStreamerPowerupDelay = _IpStreamerPowerupDelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 17),
    _IpStreamerPowerupDelay_Type()
)
ipStreamerPowerupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerPowerupDelay.setStatus("current")


class _IpStreamerFECOutput_Type(Integer32):
    """Custom type ipStreamerFECOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("rtp", 2),
          ("rtp-fec-0", 3),
          ("rtp-fec-1", 4),
          ("rtp-fec-2", 5),
          ("rtp-fec-3", 6),
          ("rtp-fec-4", 7))
    )


_IpStreamerFECOutput_Type.__name__ = "Integer32"
_IpStreamerFECOutput_Object = MibTableColumn
ipStreamerFECOutput = _IpStreamerFECOutput_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 20, 2, 1, 18),
    _IpStreamerFECOutput_Type()
)
ipStreamerFECOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipStreamerFECOutput.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-IPSTREAMER",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "ipStreamer": ipStreamer,
       "ipStreamerStatusTable": ipStreamerStatusTable,
       "ipStreamerStatusEntry": ipStreamerStatusEntry,
       "ipStreamerStatusModuleIndex": ipStreamerStatusModuleIndex,
       "ipStreamerSoftwareRelease": ipStreamerSoftwareRelease,
       "ipStreamerAlarmStatus": ipStreamerAlarmStatus,
       "ipStreamerHeartBeat": ipStreamerHeartBeat,
       "ipStreamernextTimeDate": ipStreamernextTimeDate,
       "ipStreamerTable": ipStreamerTable,
       "ipStreamerEntry": ipStreamerEntry,
       "ipStreamerCurrentNextIndex": ipStreamerCurrentNextIndex,
       "ipStreamerModuleIndex": ipStreamerModuleIndex,
       "ipStreamerOwnIPAddress": ipStreamerOwnIPAddress,
       "ipStreamerNetworkMask": ipStreamerNetworkMask,
       "ipStreamerRouterIPAddress": ipStreamerRouterIPAddress,
       "ipStreamerDestinationIPAddress": ipStreamerDestinationIPAddress,
       "ipStreamerDestinationUDPPort": ipStreamerDestinationUDPPort,
       "ipStreamerTSPacketsPerUDPFrame": ipStreamerTSPacketsPerUDPFrame,
       "ipStreamerMulticastIPAddress": ipStreamerMulticastIPAddress,
       "ipStreamerTimeToLive": ipStreamerTimeToLive,
       "ipStreamerTypeOfService": ipStreamerTypeOfService,
       "ipStreamerListenMulticastIPAddress": ipStreamerListenMulticastIPAddress,
       "ipStreamerListenUDPPort": ipStreamerListenUDPPort,
       "ipStreamerLastReceivedFromIP": ipStreamerLastReceivedFromIP,
       "ipStreamerRxOutput": ipStreamerRxOutput,
       "ipStreamerTxSource": ipStreamerTxSource,
       "ipStreamerPowerupDelay": ipStreamerPowerupDelay,
       "ipStreamerFECOutput": ipStreamerFECOutput}
)
