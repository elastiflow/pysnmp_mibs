# SNMP MIB module (DIGI-UDP-SERIAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-UDP-SERIAL-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:31 2025
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

(digiUdpSerial,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiUdpSerial")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Switch(Integer32):
    """Custom type Switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )





class UDPOverflow(Integer32):
    """Custom type UDPOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("flush", 2))
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UdpSerialSettingsTable_Object = MibTable
udpSerialSettingsTable = _UdpSerialSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11)
)
if mibBuilder.loadTexts:
    udpSerialSettingsTable.setStatus("mandatory")
_UdpSerialSettingsEntry_Object = MibTableRow
udpSerialSettingsEntry = _UdpSerialSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11, 1)
)
udpSerialSettingsEntry.setIndexNames(
    (0, "DIGI-UDP-SERIAL-MIB", "udpSerialPortIndex"),
)
if mibBuilder.loadTexts:
    udpSerialSettingsEntry.setStatus("mandatory")
_UdpSerialPortIndex_Type = Integer32
_UdpSerialPortIndex_Object = MibTableColumn
udpSerialPortIndex = _UdpSerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11, 1, 11),
    _UdpSerialPortIndex_Type()
)
udpSerialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialPortIndex.setStatus("mandatory")


class _UdpSerialRmax_Type(Integer32):
    """Custom type udpSerialRmax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UdpSerialRmax_Type.__name__ = "Integer32"
_UdpSerialRmax_Object = MibTableColumn
udpSerialRmax = _UdpSerialRmax_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11, 1, 12),
    _UdpSerialRmax_Type()
)
udpSerialRmax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialRmax.setStatus("mandatory")


class _UdpSerialRtime_Type(Integer32):
    """Custom type udpSerialRtime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UdpSerialRtime_Type.__name__ = "Integer32"
_UdpSerialRtime_Object = MibTableColumn
udpSerialRtime = _UdpSerialRtime_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11, 1, 13),
    _UdpSerialRtime_Type()
)
udpSerialRtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialRtime.setStatus("mandatory")
_UdpSerialOverflowPolicy_Type = UDPOverflow
_UdpSerialOverflowPolicy_Object = MibTableColumn
udpSerialOverflowPolicy = _UdpSerialOverflowPolicy_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11, 1, 14),
    _UdpSerialOverflowPolicy_Type()
)
udpSerialOverflowPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialOverflowPolicy.setStatus("mandatory")
_UdpSerialStripDelimiters_Type = Switch
_UdpSerialStripDelimiters_Object = MibTableColumn
udpSerialStripDelimiters = _UdpSerialStripDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11, 1, 15),
    _UdpSerialStripDelimiters_Type()
)
udpSerialStripDelimiters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialStripDelimiters.setStatus("mandatory")
_UdpSerialDelimiters_Type = DisplayString
_UdpSerialDelimiters_Object = MibTableColumn
udpSerialDelimiters = _UdpSerialDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11, 1, 16),
    _UdpSerialDelimiters_Type()
)
udpSerialDelimiters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialDelimiters.setStatus("mandatory")
_UdpSerialRemoveDelimiters_Type = Integer32
_UdpSerialRemoveDelimiters_Object = MibTableColumn
udpSerialRemoveDelimiters = _UdpSerialRemoveDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11, 1, 17),
    _UdpSerialRemoveDelimiters_Type()
)
udpSerialRemoveDelimiters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialRemoveDelimiters.setStatus("mandatory")
_UdpSerialValidateNext_Type = Integer32
_UdpSerialValidateNext_Object = MibTableColumn
udpSerialValidateNext = _UdpSerialValidateNext_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11, 1, 18),
    _UdpSerialValidateNext_Type()
)
udpSerialValidateNext.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialValidateNext.setStatus("mandatory")


class _UdpSerialResetDesinations_Type(Integer32):
    """Custom type udpSerialResetDesinations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("factory", 2),
          ("nvram", 3))
    )


_UdpSerialResetDesinations_Type.__name__ = "Integer32"
_UdpSerialResetDesinations_Object = MibTableColumn
udpSerialResetDesinations = _UdpSerialResetDesinations_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11, 1, 19),
    _UdpSerialResetDesinations_Type()
)
udpSerialResetDesinations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialResetDesinations.setStatus("mandatory")
_UdpSerialDestinationsMask_Type = DisplayString
_UdpSerialDestinationsMask_Object = MibTableColumn
udpSerialDestinationsMask = _UdpSerialDestinationsMask_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 11, 1, 20),
    _UdpSerialDestinationsMask_Type()
)
udpSerialDestinationsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialDestinationsMask.setStatus("mandatory")
_UdpSerialDestinationsTable_Object = MibTable
udpSerialDestinationsTable = _UdpSerialDestinationsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 12)
)
if mibBuilder.loadTexts:
    udpSerialDestinationsTable.setStatus("mandatory")
_UdpSerialDestinationsEntry_Object = MibTableRow
udpSerialDestinationsEntry = _UdpSerialDestinationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 12, 1)
)
udpSerialDestinationsEntry.setIndexNames(
    (0, "DIGI-UDP-SERIAL-MIB", "udpSerialDestinationIndex"),
)
if mibBuilder.loadTexts:
    udpSerialDestinationsEntry.setStatus("mandatory")
_UdpSerialDestinationIndex_Type = Integer32
_UdpSerialDestinationIndex_Object = MibTableColumn
udpSerialDestinationIndex = _UdpSerialDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 12, 1, 11),
    _UdpSerialDestinationIndex_Type()
)
udpSerialDestinationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialDestinationIndex.setStatus("mandatory")
_UdpSerialDestinationIpAddress_Type = IpAddress
_UdpSerialDestinationIpAddress_Object = MibTableColumn
udpSerialDestinationIpAddress = _UdpSerialDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 12, 1, 12),
    _UdpSerialDestinationIpAddress_Type()
)
udpSerialDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialDestinationIpAddress.setStatus("mandatory")


class _UdpSerialDestinationIpPort_Type(Integer32):
    """Custom type udpSerialDestinationIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_UdpSerialDestinationIpPort_Type.__name__ = "Integer32"
_UdpSerialDestinationIpPort_Object = MibTableColumn
udpSerialDestinationIpPort = _UdpSerialDestinationIpPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 12, 1, 13),
    _UdpSerialDestinationIpPort_Type()
)
udpSerialDestinationIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialDestinationIpPort.setStatus("mandatory")
_UdpSerialDestinationName_Type = DisplayString
_UdpSerialDestinationName_Object = MibTableColumn
udpSerialDestinationName = _UdpSerialDestinationName_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 12, 1, 14),
    _UdpSerialDestinationName_Type()
)
udpSerialDestinationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialDestinationName.setStatus("mandatory")
_UdpSerialDestinationRemove_Type = Switch
_UdpSerialDestinationRemove_Object = MibTableColumn
udpSerialDestinationRemove = _UdpSerialDestinationRemove_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 12, 1, 15),
    _UdpSerialDestinationRemove_Type()
)
udpSerialDestinationRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialDestinationRemove.setStatus("mandatory")
_UdpSerialStatisticsTable_Object = MibTable
udpSerialStatisticsTable = _UdpSerialStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13)
)
if mibBuilder.loadTexts:
    udpSerialStatisticsTable.setStatus("mandatory")
_UdpSerialStatisticsEntry_Object = MibTableRow
udpSerialStatisticsEntry = _UdpSerialStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1)
)
udpSerialStatisticsEntry.setIndexNames(
    (0, "DIGI-UDP-SERIAL-MIB", "udpSerialStatisticIndex"),
)
if mibBuilder.loadTexts:
    udpSerialStatisticsEntry.setStatus("mandatory")
_UdpSerialStatisticIndex_Type = Integer32
_UdpSerialStatisticIndex_Object = MibTableColumn
udpSerialStatisticIndex = _UdpSerialStatisticIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 11),
    _UdpSerialStatisticIndex_Type()
)
udpSerialStatisticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticIndex.setStatus("mandatory")
_UdpSerialStatisticDgramTxCnt_Type = Integer32
_UdpSerialStatisticDgramTxCnt_Object = MibTableColumn
udpSerialStatisticDgramTxCnt = _UdpSerialStatisticDgramTxCnt_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 12),
    _UdpSerialStatisticDgramTxCnt_Type()
)
udpSerialStatisticDgramTxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticDgramTxCnt.setStatus("mandatory")
_UdpSerialStatisticDgramTxBytes_Type = Integer32
_UdpSerialStatisticDgramTxBytes_Object = MibTableColumn
udpSerialStatisticDgramTxBytes = _UdpSerialStatisticDgramTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 13),
    _UdpSerialStatisticDgramTxBytes_Type()
)
udpSerialStatisticDgramTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticDgramTxBytes.setStatus("mandatory")
_UdpSerialStatisticDgramRxCnt_Type = Integer32
_UdpSerialStatisticDgramRxCnt_Object = MibTableColumn
udpSerialStatisticDgramRxCnt = _UdpSerialStatisticDgramRxCnt_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 14),
    _UdpSerialStatisticDgramRxCnt_Type()
)
udpSerialStatisticDgramRxCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticDgramRxCnt.setStatus("mandatory")
_UdpSerialStatisticDgramRxBytes_Type = Integer32
_UdpSerialStatisticDgramRxBytes_Object = MibTableColumn
udpSerialStatisticDgramRxBytes = _UdpSerialStatisticDgramRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 15),
    _UdpSerialStatisticDgramRxBytes_Type()
)
udpSerialStatisticDgramRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticDgramRxBytes.setStatus("mandatory")
_UdpSerialStatisticSerialTxBytes_Type = Integer32
_UdpSerialStatisticSerialTxBytes_Object = MibTableColumn
udpSerialStatisticSerialTxBytes = _UdpSerialStatisticSerialTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 16),
    _UdpSerialStatisticSerialTxBytes_Type()
)
udpSerialStatisticSerialTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticSerialTxBytes.setStatus("mandatory")
_UdpSerialStatisticSerialRxBytes_Type = Integer32
_UdpSerialStatisticSerialRxBytes_Object = MibTableColumn
udpSerialStatisticSerialRxBytes = _UdpSerialStatisticSerialRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 17),
    _UdpSerialStatisticSerialRxBytes_Type()
)
udpSerialStatisticSerialRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticSerialRxBytes.setStatus("mandatory")
_UdpSerialStatisticDgramHostUnreach_Type = Integer32
_UdpSerialStatisticDgramHostUnreach_Object = MibTableColumn
udpSerialStatisticDgramHostUnreach = _UdpSerialStatisticDgramHostUnreach_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 18),
    _UdpSerialStatisticDgramHostUnreach_Type()
)
udpSerialStatisticDgramHostUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticDgramHostUnreach.setStatus("mandatory")
_UdpSerialStatisticDgramNetErrors_Type = Integer32
_UdpSerialStatisticDgramNetErrors_Object = MibTableColumn
udpSerialStatisticDgramNetErrors = _UdpSerialStatisticDgramNetErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 19),
    _UdpSerialStatisticDgramNetErrors_Type()
)
udpSerialStatisticDgramNetErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticDgramNetErrors.setStatus("mandatory")
_UdpSerialStatisticSerialPortBusy_Type = Integer32
_UdpSerialStatisticSerialPortBusy_Object = MibTableColumn
udpSerialStatisticSerialPortBusy = _UdpSerialStatisticSerialPortBusy_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 20),
    _UdpSerialStatisticSerialPortBusy_Type()
)
udpSerialStatisticSerialPortBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticSerialPortBusy.setStatus("mandatory")
_UdpSerialStatisticSerialErrors_Type = Integer32
_UdpSerialStatisticSerialErrors_Object = MibTableColumn
udpSerialStatisticSerialErrors = _UdpSerialStatisticSerialErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 21),
    _UdpSerialStatisticSerialErrors_Type()
)
udpSerialStatisticSerialErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticSerialErrors.setStatus("mandatory")
_UdpSerialStatisticDgramBytesLost_Type = Integer32
_UdpSerialStatisticDgramBytesLost_Object = MibTableColumn
udpSerialStatisticDgramBytesLost = _UdpSerialStatisticDgramBytesLost_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 22),
    _UdpSerialStatisticDgramBytesLost_Type()
)
udpSerialStatisticDgramBytesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticDgramBytesLost.setStatus("mandatory")
_UdpSerialStatisticSerialBytesLost_Type = Integer32
_UdpSerialStatisticSerialBytesLost_Object = MibTableColumn
udpSerialStatisticSerialBytesLost = _UdpSerialStatisticSerialBytesLost_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 23),
    _UdpSerialStatisticSerialBytesLost_Type()
)
udpSerialStatisticSerialBytesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticSerialBytesLost.setStatus("mandatory")
_UdpSerialStatisticPortReconfigured_Type = Integer32
_UdpSerialStatisticPortReconfigured_Object = MibTableColumn
udpSerialStatisticPortReconfigured = _UdpSerialStatisticPortReconfigured_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 24),
    _UdpSerialStatisticPortReconfigured_Type()
)
udpSerialStatisticPortReconfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpSerialStatisticPortReconfigured.setStatus("mandatory")
_UdpSerialStatisticPortClear_Type = Integer32
_UdpSerialStatisticPortClear_Object = MibTableColumn
udpSerialStatisticPortClear = _UdpSerialStatisticPortClear_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 13, 1, 25),
    _UdpSerialStatisticPortClear_Type()
)
udpSerialStatisticPortClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialStatisticPortClear.setStatus("mandatory")
_UdpSerialStatisticsClear_Type = Integer32
_UdpSerialStatisticsClear_Object = MibScalar
udpSerialStatisticsClear = _UdpSerialStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 13, 14),
    _UdpSerialStatisticsClear_Type()
)
udpSerialStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    udpSerialStatisticsClear.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-UDP-SERIAL-MIB",
    **{"Switch": Switch,
       "UDPOverflow": UDPOverflow,
       "DisplayString": DisplayString,
       "udpSerialSettingsTable": udpSerialSettingsTable,
       "udpSerialSettingsEntry": udpSerialSettingsEntry,
       "udpSerialPortIndex": udpSerialPortIndex,
       "udpSerialRmax": udpSerialRmax,
       "udpSerialRtime": udpSerialRtime,
       "udpSerialOverflowPolicy": udpSerialOverflowPolicy,
       "udpSerialStripDelimiters": udpSerialStripDelimiters,
       "udpSerialDelimiters": udpSerialDelimiters,
       "udpSerialRemoveDelimiters": udpSerialRemoveDelimiters,
       "udpSerialValidateNext": udpSerialValidateNext,
       "udpSerialResetDesinations": udpSerialResetDesinations,
       "udpSerialDestinationsMask": udpSerialDestinationsMask,
       "udpSerialDestinationsTable": udpSerialDestinationsTable,
       "udpSerialDestinationsEntry": udpSerialDestinationsEntry,
       "udpSerialDestinationIndex": udpSerialDestinationIndex,
       "udpSerialDestinationIpAddress": udpSerialDestinationIpAddress,
       "udpSerialDestinationIpPort": udpSerialDestinationIpPort,
       "udpSerialDestinationName": udpSerialDestinationName,
       "udpSerialDestinationRemove": udpSerialDestinationRemove,
       "udpSerialStatisticsTable": udpSerialStatisticsTable,
       "udpSerialStatisticsEntry": udpSerialStatisticsEntry,
       "udpSerialStatisticIndex": udpSerialStatisticIndex,
       "udpSerialStatisticDgramTxCnt": udpSerialStatisticDgramTxCnt,
       "udpSerialStatisticDgramTxBytes": udpSerialStatisticDgramTxBytes,
       "udpSerialStatisticDgramRxCnt": udpSerialStatisticDgramRxCnt,
       "udpSerialStatisticDgramRxBytes": udpSerialStatisticDgramRxBytes,
       "udpSerialStatisticSerialTxBytes": udpSerialStatisticSerialTxBytes,
       "udpSerialStatisticSerialRxBytes": udpSerialStatisticSerialRxBytes,
       "udpSerialStatisticDgramHostUnreach": udpSerialStatisticDgramHostUnreach,
       "udpSerialStatisticDgramNetErrors": udpSerialStatisticDgramNetErrors,
       "udpSerialStatisticSerialPortBusy": udpSerialStatisticSerialPortBusy,
       "udpSerialStatisticSerialErrors": udpSerialStatisticSerialErrors,
       "udpSerialStatisticDgramBytesLost": udpSerialStatisticDgramBytesLost,
       "udpSerialStatisticSerialBytesLost": udpSerialStatisticSerialBytesLost,
       "udpSerialStatisticPortReconfigured": udpSerialStatisticPortReconfigured,
       "udpSerialStatisticPortClear": udpSerialStatisticPortClear,
       "udpSerialStatisticsClear": udpSerialStatisticsClear}
)
