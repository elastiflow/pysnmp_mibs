# SNMP MIB module (DIGI-IA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/digi_332/DIGI-IA-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 11:54:30 2025
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

(digiIA,) = mibBuilder.importSymbols(
    "DIGI-SMI",
    "digiIA")

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





class IAProtocol(Integer32):
    """Custom type IAProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("modbusascii", 2),
          ("modbusrtu", 3),
          ("df1fullduplex", 4),
          ("userdefined", 5),
          ("omronhostlink", 6),
          ("df1halfduplex", 7),
          ("omroncompowayf", 8),
          ("omronfins", 9))
    )





class IANetProtocol(Integer32):
    """Custom type IANetProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("none", 2),
          ("tcpsocket", 3),
          ("udpsocket", 4),
          ("modbtcp", 5),
          ("abethernet", 6),
          ("ethernetip", 7),
          ("modbascii", 8),
          ("modbrtu", 9),
          ("df1full", 10))
    )





class IAType(Integer32):
    """Custom type IAType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("master", 2),
          ("slave", 3))
    )





class IARouteType(Integer32):
    """Custom type IARouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("unconfigured", 2),
          ("serial", 3),
          ("network", 4))
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IaSerialSettings_ObjectIdentity = ObjectIdentity
iaSerialSettings = _IaSerialSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11)
)
_IaSerialGeneralSettingsTable_Object = MibTable
iaSerialGeneralSettingsTable = _IaSerialGeneralSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 11)
)
if mibBuilder.loadTexts:
    iaSerialGeneralSettingsTable.setStatus("mandatory")
_IaSerialGeneralSettingsEntry_Object = MibTableRow
iaSerialGeneralSettingsEntry = _IaSerialGeneralSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 11, 1)
)
iaSerialGeneralSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaSerialPortIndex"),
)
if mibBuilder.loadTexts:
    iaSerialGeneralSettingsEntry.setStatus("mandatory")
_IaSerialPortIndex_Type = Integer32
_IaSerialPortIndex_Object = MibTableColumn
iaSerialPortIndex = _IaSerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 11, 1, 11),
    _IaSerialPortIndex_Type()
)
iaSerialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iaSerialPortIndex.setStatus("mandatory")
_IaSerialPortType_Type = IAType
_IaSerialPortType_Object = MibTableColumn
iaSerialPortType = _IaSerialPortType_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 11, 1, 12),
    _IaSerialPortType_Type()
)
iaSerialPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialPortType.setStatus("mandatory")
_IaSerialPortProtocol_Type = IAProtocol
_IaSerialPortProtocol_Object = MibTableColumn
iaSerialPortProtocol = _IaSerialPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 11, 1, 13),
    _IaSerialPortProtocol_Type()
)
iaSerialPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialPortProtocol.setStatus("mandatory")


class _IaSerialMessageTimeout_Type(Integer32):
    """Custom type iaSerialMessageTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaSerialMessageTimeout_Type.__name__ = "Integer32"
_IaSerialMessageTimeout_Object = MibTableColumn
iaSerialMessageTimeout = _IaSerialMessageTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 11, 1, 14),
    _IaSerialMessageTimeout_Type()
)
iaSerialMessageTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialMessageTimeout.setStatus("mandatory")
_IaSerialNetSlaveList_Type = DisplayString
_IaSerialNetSlaveList_Object = MibTableColumn
iaSerialNetSlaveList = _IaSerialNetSlaveList_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 11, 1, 15),
    _IaSerialNetSlaveList_Type()
)
iaSerialNetSlaveList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialNetSlaveList.setStatus("obsolete")


class _IaSerialRevert_Type(Integer32):
    """Custom type iaSerialRevert based on Integer32"""
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


_IaSerialRevert_Type.__name__ = "Integer32"
_IaSerialRevert_Object = MibTableColumn
iaSerialRevert = _IaSerialRevert_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 11, 1, 16),
    _IaSerialRevert_Type()
)
iaSerialRevert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialRevert.setStatus("mandatory")


class _IaSerialResetNetSlaves_Type(Integer32):
    """Custom type iaSerialResetNetSlaves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaSerialResetNetSlaves_Type.__name__ = "Integer32"
_IaSerialResetNetSlaves_Object = MibTableColumn
iaSerialResetNetSlaves = _IaSerialResetNetSlaves_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 11, 1, 17),
    _IaSerialResetNetSlaves_Type()
)
iaSerialResetNetSlaves.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialResetNetSlaves.setStatus("obsolete")
_IaSerialAddRouteEntry_Type = Integer32
_IaSerialAddRouteEntry_Object = MibTableColumn
iaSerialAddRouteEntry = _IaSerialAddRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 11, 1, 18),
    _IaSerialAddRouteEntry_Type()
)
iaSerialAddRouteEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialAddRouteEntry.setStatus("mandatory")
_IaSerialModbusRTUSettingsTable_Object = MibTable
iaSerialModbusRTUSettingsTable = _IaSerialModbusRTUSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 12)
)
if mibBuilder.loadTexts:
    iaSerialModbusRTUSettingsTable.setStatus("mandatory")
_IaSerialModbusRTUSettingsEntry_Object = MibTableRow
iaSerialModbusRTUSettingsEntry = _IaSerialModbusRTUSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 12, 1)
)
iaSerialModbusRTUSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaSerialPortModbusRTUIndex"),
)
if mibBuilder.loadTexts:
    iaSerialModbusRTUSettingsEntry.setStatus("mandatory")
_IaSerialPortModbusRTUIndex_Type = Integer32
_IaSerialPortModbusRTUIndex_Object = MibTableColumn
iaSerialPortModbusRTUIndex = _IaSerialPortModbusRTUIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 12, 1, 11),
    _IaSerialPortModbusRTUIndex_Type()
)
iaSerialPortModbusRTUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iaSerialPortModbusRTUIndex.setStatus("mandatory")


class _IaSerialModbusRTUTimeout_Type(Integer32):
    """Custom type iaSerialModbusRTUTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaSerialModbusRTUTimeout_Type.__name__ = "Integer32"
_IaSerialModbusRTUTimeout_Object = MibTableColumn
iaSerialModbusRTUTimeout = _IaSerialModbusRTUTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 12, 1, 12),
    _IaSerialModbusRTUTimeout_Type()
)
iaSerialModbusRTUTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialModbusRTUTimeout.setStatus("mandatory")


class _IaSerialModbusRTUFixedAddress_Type(Integer32):
    """Custom type iaSerialModbusRTUFixedAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IaSerialModbusRTUFixedAddress_Type.__name__ = "Integer32"
_IaSerialModbusRTUFixedAddress_Object = MibTableColumn
iaSerialModbusRTUFixedAddress = _IaSerialModbusRTUFixedAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 12, 1, 13),
    _IaSerialModbusRTUFixedAddress_Type()
)
iaSerialModbusRTUFixedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialModbusRTUFixedAddress.setStatus("mandatory")


class _IaSerialModbusRTUBroadcastFlag_Type(Integer32):
    """Custom type iaSerialModbusRTUBroadcastFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("replace", 3))
    )


_IaSerialModbusRTUBroadcastFlag_Type.__name__ = "Integer32"
_IaSerialModbusRTUBroadcastFlag_Object = MibTableColumn
iaSerialModbusRTUBroadcastFlag = _IaSerialModbusRTUBroadcastFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 12, 1, 14),
    _IaSerialModbusRTUBroadcastFlag_Type()
)
iaSerialModbusRTUBroadcastFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialModbusRTUBroadcastFlag.setStatus("mandatory")


class _IaSerialModbusRTUErrorResponseFlag_Type(Integer32):
    """Custom type iaSerialModbusRTUErrorResponseFlag based on Integer32"""
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


_IaSerialModbusRTUErrorResponseFlag_Type.__name__ = "Integer32"
_IaSerialModbusRTUErrorResponseFlag_Object = MibTableColumn
iaSerialModbusRTUErrorResponseFlag = _IaSerialModbusRTUErrorResponseFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 12, 1, 15),
    _IaSerialModbusRTUErrorResponseFlag_Type()
)
iaSerialModbusRTUErrorResponseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialModbusRTUErrorResponseFlag.setStatus("mandatory")


class _IaSerialModbusRTUExtendedTimeout_Type(Integer32):
    """Custom type iaSerialModbusRTUExtendedTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaSerialModbusRTUExtendedTimeout_Type.__name__ = "Integer32"
_IaSerialModbusRTUExtendedTimeout_Object = MibTableColumn
iaSerialModbusRTUExtendedTimeout = _IaSerialModbusRTUExtendedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 12, 1, 16),
    _IaSerialModbusRTUExtendedTimeout_Type()
)
iaSerialModbusRTUExtendedTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialModbusRTUExtendedTimeout.setStatus("mandatory")
_IaSerialModbusRTUExtendedFunctions_Type = DisplayString
_IaSerialModbusRTUExtendedFunctions_Object = MibTableColumn
iaSerialModbusRTUExtendedFunctions = _IaSerialModbusRTUExtendedFunctions_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 12, 1, 17),
    _IaSerialModbusRTUExtendedFunctions_Type()
)
iaSerialModbusRTUExtendedFunctions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialModbusRTUExtendedFunctions.setStatus("mandatory")
_IaSerialModbusRTUAddExtendedFunctions_Type = DisplayString
_IaSerialModbusRTUAddExtendedFunctions_Object = MibTableColumn
iaSerialModbusRTUAddExtendedFunctions = _IaSerialModbusRTUAddExtendedFunctions_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 12, 1, 18),
    _IaSerialModbusRTUAddExtendedFunctions_Type()
)
iaSerialModbusRTUAddExtendedFunctions.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iaSerialModbusRTUAddExtendedFunctions.setStatus("mandatory")
_IaSerialModbusRTURemoveExtendedFunctions_Type = DisplayString
_IaSerialModbusRTURemoveExtendedFunctions_Object = MibTableColumn
iaSerialModbusRTURemoveExtendedFunctions = _IaSerialModbusRTURemoveExtendedFunctions_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 12, 1, 19),
    _IaSerialModbusRTURemoveExtendedFunctions_Type()
)
iaSerialModbusRTURemoveExtendedFunctions.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iaSerialModbusRTURemoveExtendedFunctions.setStatus("mandatory")
_IaSerialDF1FullDuplexSettingsTable_Object = MibTable
iaSerialDF1FullDuplexSettingsTable = _IaSerialDF1FullDuplexSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 13)
)
if mibBuilder.loadTexts:
    iaSerialDF1FullDuplexSettingsTable.setStatus("mandatory")
_IaSerialDF1FullDuplexSettingsEntry_Object = MibTableRow
iaSerialDF1FullDuplexSettingsEntry = _IaSerialDF1FullDuplexSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 13, 1)
)
iaSerialDF1FullDuplexSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaSerialPortDF1FullDuplexIndex"),
)
if mibBuilder.loadTexts:
    iaSerialDF1FullDuplexSettingsEntry.setStatus("mandatory")
_IaSerialPortDF1FullDuplexIndex_Type = Integer32
_IaSerialPortDF1FullDuplexIndex_Object = MibTableColumn
iaSerialPortDF1FullDuplexIndex = _IaSerialPortDF1FullDuplexIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 13, 1, 11),
    _IaSerialPortDF1FullDuplexIndex_Type()
)
iaSerialPortDF1FullDuplexIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iaSerialPortDF1FullDuplexIndex.setStatus("mandatory")


class _IaSerialDF1FullDuplexChecksum_Type(Integer32):
    """Custom type iaSerialDF1FullDuplexChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bcc", 1),
          ("crc", 2))
    )


_IaSerialDF1FullDuplexChecksum_Type.__name__ = "Integer32"
_IaSerialDF1FullDuplexChecksum_Object = MibTableColumn
iaSerialDF1FullDuplexChecksum = _IaSerialDF1FullDuplexChecksum_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 13, 1, 12),
    _IaSerialDF1FullDuplexChecksum_Type()
)
iaSerialDF1FullDuplexChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1FullDuplexChecksum.setStatus("mandatory")


class _IaSerialDF1FullDuplexAckTimeout_Type(Integer32):
    """Custom type iaSerialDF1FullDuplexAckTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaSerialDF1FullDuplexAckTimeout_Type.__name__ = "Integer32"
_IaSerialDF1FullDuplexAckTimeout_Object = MibTableColumn
iaSerialDF1FullDuplexAckTimeout = _IaSerialDF1FullDuplexAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 13, 1, 13),
    _IaSerialDF1FullDuplexAckTimeout_Type()
)
iaSerialDF1FullDuplexAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1FullDuplexAckTimeout.setStatus("mandatory")


class _IaSerialDF1FullDuplexAckTimeoutLimit_Type(Integer32):
    """Custom type iaSerialDF1FullDuplexAckTimeoutLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IaSerialDF1FullDuplexAckTimeoutLimit_Type.__name__ = "Integer32"
_IaSerialDF1FullDuplexAckTimeoutLimit_Object = MibTableColumn
iaSerialDF1FullDuplexAckTimeoutLimit = _IaSerialDF1FullDuplexAckTimeoutLimit_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 13, 1, 14),
    _IaSerialDF1FullDuplexAckTimeoutLimit_Type()
)
iaSerialDF1FullDuplexAckTimeoutLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1FullDuplexAckTimeoutLimit.setStatus("mandatory")


class _IaSerialDF1FullDuplexNakTimeoutLimit_Type(Integer32):
    """Custom type iaSerialDF1FullDuplexNakTimeoutLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IaSerialDF1FullDuplexNakTimeoutLimit_Type.__name__ = "Integer32"
_IaSerialDF1FullDuplexNakTimeoutLimit_Object = MibTableColumn
iaSerialDF1FullDuplexNakTimeoutLimit = _IaSerialDF1FullDuplexNakTimeoutLimit_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 13, 1, 15),
    _IaSerialDF1FullDuplexNakTimeoutLimit_Type()
)
iaSerialDF1FullDuplexNakTimeoutLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1FullDuplexNakTimeoutLimit.setStatus("mandatory")


class _IaSerialDF1FullDuplexErrorResponseFlag_Type(Integer32):
    """Custom type iaSerialDF1FullDuplexErrorResponseFlag based on Integer32"""
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


_IaSerialDF1FullDuplexErrorResponseFlag_Type.__name__ = "Integer32"
_IaSerialDF1FullDuplexErrorResponseFlag_Object = MibTableColumn
iaSerialDF1FullDuplexErrorResponseFlag = _IaSerialDF1FullDuplexErrorResponseFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 13, 1, 16),
    _IaSerialDF1FullDuplexErrorResponseFlag_Type()
)
iaSerialDF1FullDuplexErrorResponseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1FullDuplexErrorResponseFlag.setStatus("mandatory")


class _IaSerialDF1FullDuplexDuplicateDetectFlag_Type(Integer32):
    """Custom type iaSerialDF1FullDuplexDuplicateDetectFlag based on Integer32"""
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


_IaSerialDF1FullDuplexDuplicateDetectFlag_Type.__name__ = "Integer32"
_IaSerialDF1FullDuplexDuplicateDetectFlag_Object = MibTableColumn
iaSerialDF1FullDuplexDuplicateDetectFlag = _IaSerialDF1FullDuplexDuplicateDetectFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 13, 1, 17),
    _IaSerialDF1FullDuplexDuplicateDetectFlag_Type()
)
iaSerialDF1FullDuplexDuplicateDetectFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1FullDuplexDuplicateDetectFlag.setStatus("mandatory")
_IaSerialDF1HalfDuplexSettingsTable_Object = MibTable
iaSerialDF1HalfDuplexSettingsTable = _IaSerialDF1HalfDuplexSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 14)
)
if mibBuilder.loadTexts:
    iaSerialDF1HalfDuplexSettingsTable.setStatus("mandatory")
_IaSerialDF1HalfDuplexSettingsEntry_Object = MibTableRow
iaSerialDF1HalfDuplexSettingsEntry = _IaSerialDF1HalfDuplexSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 14, 1)
)
iaSerialDF1HalfDuplexSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaSerialPortDF1HalfDuplexIndex"),
)
if mibBuilder.loadTexts:
    iaSerialDF1HalfDuplexSettingsEntry.setStatus("mandatory")
_IaSerialPortDF1HalfDuplexIndex_Type = Integer32
_IaSerialPortDF1HalfDuplexIndex_Object = MibTableColumn
iaSerialPortDF1HalfDuplexIndex = _IaSerialPortDF1HalfDuplexIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 14, 1, 11),
    _IaSerialPortDF1HalfDuplexIndex_Type()
)
iaSerialPortDF1HalfDuplexIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iaSerialPortDF1HalfDuplexIndex.setStatus("mandatory")


class _IaSerialDF1HalfDuplexChecksum_Type(Integer32):
    """Custom type iaSerialDF1HalfDuplexChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bcc", 1),
          ("crc", 2))
    )


_IaSerialDF1HalfDuplexChecksum_Type.__name__ = "Integer32"
_IaSerialDF1HalfDuplexChecksum_Object = MibTableColumn
iaSerialDF1HalfDuplexChecksum = _IaSerialDF1HalfDuplexChecksum_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 14, 1, 12),
    _IaSerialDF1HalfDuplexChecksum_Type()
)
iaSerialDF1HalfDuplexChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1HalfDuplexChecksum.setStatus("mandatory")


class _IaSerialDF1HalfDuplexAckTimeout_Type(Integer32):
    """Custom type iaSerialDF1HalfDuplexAckTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaSerialDF1HalfDuplexAckTimeout_Type.__name__ = "Integer32"
_IaSerialDF1HalfDuplexAckTimeout_Object = MibTableColumn
iaSerialDF1HalfDuplexAckTimeout = _IaSerialDF1HalfDuplexAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 14, 1, 13),
    _IaSerialDF1HalfDuplexAckTimeout_Type()
)
iaSerialDF1HalfDuplexAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1HalfDuplexAckTimeout.setStatus("mandatory")


class _IaSerialDF1HalfDuplexAckTimeoutLimit_Type(Integer32):
    """Custom type iaSerialDF1HalfDuplexAckTimeoutLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IaSerialDF1HalfDuplexAckTimeoutLimit_Type.__name__ = "Integer32"
_IaSerialDF1HalfDuplexAckTimeoutLimit_Object = MibTableColumn
iaSerialDF1HalfDuplexAckTimeoutLimit = _IaSerialDF1HalfDuplexAckTimeoutLimit_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 14, 1, 14),
    _IaSerialDF1HalfDuplexAckTimeoutLimit_Type()
)
iaSerialDF1HalfDuplexAckTimeoutLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1HalfDuplexAckTimeoutLimit.setStatus("mandatory")


class _IaSerialDF1HalfDuplexPollTimeout_Type(Integer32):
    """Custom type iaSerialDF1HalfDuplexPollTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaSerialDF1HalfDuplexPollTimeout_Type.__name__ = "Integer32"
_IaSerialDF1HalfDuplexPollTimeout_Object = MibTableColumn
iaSerialDF1HalfDuplexPollTimeout = _IaSerialDF1HalfDuplexPollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 14, 1, 15),
    _IaSerialDF1HalfDuplexPollTimeout_Type()
)
iaSerialDF1HalfDuplexPollTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1HalfDuplexPollTimeout.setStatus("mandatory")


class _IaSerialDF1HalfDuplexPollTimeoutLimit_Type(Integer32):
    """Custom type iaSerialDF1HalfDuplexPollTimeoutLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IaSerialDF1HalfDuplexPollTimeoutLimit_Type.__name__ = "Integer32"
_IaSerialDF1HalfDuplexPollTimeoutLimit_Object = MibTableColumn
iaSerialDF1HalfDuplexPollTimeoutLimit = _IaSerialDF1HalfDuplexPollTimeoutLimit_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 14, 1, 16),
    _IaSerialDF1HalfDuplexPollTimeoutLimit_Type()
)
iaSerialDF1HalfDuplexPollTimeoutLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1HalfDuplexPollTimeoutLimit.setStatus("mandatory")


class _IaSerialDF1HalfDuplexErrorResponseFlag_Type(Integer32):
    """Custom type iaSerialDF1HalfDuplexErrorResponseFlag based on Integer32"""
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


_IaSerialDF1HalfDuplexErrorResponseFlag_Type.__name__ = "Integer32"
_IaSerialDF1HalfDuplexErrorResponseFlag_Object = MibTableColumn
iaSerialDF1HalfDuplexErrorResponseFlag = _IaSerialDF1HalfDuplexErrorResponseFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 14, 1, 17),
    _IaSerialDF1HalfDuplexErrorResponseFlag_Type()
)
iaSerialDF1HalfDuplexErrorResponseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1HalfDuplexErrorResponseFlag.setStatus("mandatory")


class _IaSerialDF1HalfDuplexDuplicateDetectFlag_Type(Integer32):
    """Custom type iaSerialDF1HalfDuplexDuplicateDetectFlag based on Integer32"""
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


_IaSerialDF1HalfDuplexDuplicateDetectFlag_Type.__name__ = "Integer32"
_IaSerialDF1HalfDuplexDuplicateDetectFlag_Object = MibTableColumn
iaSerialDF1HalfDuplexDuplicateDetectFlag = _IaSerialDF1HalfDuplexDuplicateDetectFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 14, 1, 18),
    _IaSerialDF1HalfDuplexDuplicateDetectFlag_Type()
)
iaSerialDF1HalfDuplexDuplicateDetectFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialDF1HalfDuplexDuplicateDetectFlag.setStatus("mandatory")
_IaSerialUserDefinedSettingsTable_Object = MibTable
iaSerialUserDefinedSettingsTable = _IaSerialUserDefinedSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 15)
)
if mibBuilder.loadTexts:
    iaSerialUserDefinedSettingsTable.setStatus("mandatory")
_IaSerialUserDefinedSettingsEntry_Object = MibTableRow
iaSerialUserDefinedSettingsEntry = _IaSerialUserDefinedSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 15, 1)
)
iaSerialUserDefinedSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaSerialPortUserDefinedIndex"),
)
if mibBuilder.loadTexts:
    iaSerialUserDefinedSettingsEntry.setStatus("mandatory")
_IaSerialPortUserDefinedIndex_Type = Integer32
_IaSerialPortUserDefinedIndex_Object = MibTableColumn
iaSerialPortUserDefinedIndex = _IaSerialPortUserDefinedIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 15, 1, 11),
    _IaSerialPortUserDefinedIndex_Type()
)
iaSerialPortUserDefinedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iaSerialPortUserDefinedIndex.setStatus("mandatory")
_IaSerialUserDefinedStart_Type = DisplayString
_IaSerialUserDefinedStart_Object = MibTableColumn
iaSerialUserDefinedStart = _IaSerialUserDefinedStart_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 15, 1, 12),
    _IaSerialUserDefinedStart_Type()
)
iaSerialUserDefinedStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialUserDefinedStart.setStatus("mandatory")
_IaSerialUserDefinedEnd_Type = DisplayString
_IaSerialUserDefinedEnd_Object = MibTableColumn
iaSerialUserDefinedEnd = _IaSerialUserDefinedEnd_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 15, 1, 13),
    _IaSerialUserDefinedEnd_Type()
)
iaSerialUserDefinedEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialUserDefinedEnd.setStatus("mandatory")


class _IaSerialUserDefinedAnsiEscapeFlag_Type(Integer32):
    """Custom type iaSerialUserDefinedAnsiEscapeFlag based on Integer32"""
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


_IaSerialUserDefinedAnsiEscapeFlag_Type.__name__ = "Integer32"
_IaSerialUserDefinedAnsiEscapeFlag_Object = MibTableColumn
iaSerialUserDefinedAnsiEscapeFlag = _IaSerialUserDefinedAnsiEscapeFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 15, 1, 14),
    _IaSerialUserDefinedAnsiEscapeFlag_Type()
)
iaSerialUserDefinedAnsiEscapeFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialUserDefinedAnsiEscapeFlag.setStatus("mandatory")
_IaSerialOmronHostLinkSettingsTable_Object = MibTable
iaSerialOmronHostLinkSettingsTable = _IaSerialOmronHostLinkSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 16)
)
if mibBuilder.loadTexts:
    iaSerialOmronHostLinkSettingsTable.setStatus("mandatory")
_IaSerialOmronHostLinkSettingsEntry_Object = MibTableRow
iaSerialOmronHostLinkSettingsEntry = _IaSerialOmronHostLinkSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 16, 1)
)
iaSerialOmronHostLinkSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaSerialPortOmronHostLinkIndex"),
)
if mibBuilder.loadTexts:
    iaSerialOmronHostLinkSettingsEntry.setStatus("mandatory")
_IaSerialPortOmronHostLinkIndex_Type = Integer32
_IaSerialPortOmronHostLinkIndex_Object = MibTableColumn
iaSerialPortOmronHostLinkIndex = _IaSerialPortOmronHostLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 16, 1, 11),
    _IaSerialPortOmronHostLinkIndex_Type()
)
iaSerialPortOmronHostLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iaSerialPortOmronHostLinkIndex.setStatus("mandatory")


class _IaSerialOmronHostLinkAckTimeout_Type(Integer32):
    """Custom type iaSerialOmronHostLinkAckTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaSerialOmronHostLinkAckTimeout_Type.__name__ = "Integer32"
_IaSerialOmronHostLinkAckTimeout_Object = MibTableColumn
iaSerialOmronHostLinkAckTimeout = _IaSerialOmronHostLinkAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 16, 1, 12),
    _IaSerialOmronHostLinkAckTimeout_Type()
)
iaSerialOmronHostLinkAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialOmronHostLinkAckTimeout.setStatus("mandatory")


class _IaSerialOmronHostLinkAckTimeoutLimit_Type(Integer32):
    """Custom type iaSerialOmronHostLinkAckTimeoutLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IaSerialOmronHostLinkAckTimeoutLimit_Type.__name__ = "Integer32"
_IaSerialOmronHostLinkAckTimeoutLimit_Object = MibTableColumn
iaSerialOmronHostLinkAckTimeoutLimit = _IaSerialOmronHostLinkAckTimeoutLimit_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 16, 1, 13),
    _IaSerialOmronHostLinkAckTimeoutLimit_Type()
)
iaSerialOmronHostLinkAckTimeoutLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialOmronHostLinkAckTimeoutLimit.setStatus("mandatory")
_IaSerialOmronFinsSettingsTable_Object = MibTable
iaSerialOmronFinsSettingsTable = _IaSerialOmronFinsSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 17)
)
if mibBuilder.loadTexts:
    iaSerialOmronFinsSettingsTable.setStatus("mandatory")
_IaSerialOmronFinsSettingsEntry_Object = MibTableRow
iaSerialOmronFinsSettingsEntry = _IaSerialOmronFinsSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 17, 1)
)
iaSerialOmronFinsSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaSerialPortOmronFinsIndex"),
)
if mibBuilder.loadTexts:
    iaSerialOmronFinsSettingsEntry.setStatus("mandatory")
_IaSerialPortOmronFinsIndex_Type = Integer32
_IaSerialPortOmronFinsIndex_Object = MibTableColumn
iaSerialPortOmronFinsIndex = _IaSerialPortOmronFinsIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 17, 1, 11),
    _IaSerialPortOmronFinsIndex_Type()
)
iaSerialPortOmronFinsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iaSerialPortOmronFinsIndex.setStatus("mandatory")


class _IaSerialOmronFinsAckTimeout_Type(Integer32):
    """Custom type iaSerialOmronFinsAckTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaSerialOmronFinsAckTimeout_Type.__name__ = "Integer32"
_IaSerialOmronFinsAckTimeout_Object = MibTableColumn
iaSerialOmronFinsAckTimeout = _IaSerialOmronFinsAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 17, 1, 12),
    _IaSerialOmronFinsAckTimeout_Type()
)
iaSerialOmronFinsAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialOmronFinsAckTimeout.setStatus("mandatory")


class _IaSerialOmronFinsAckTimeoutLimit_Type(Integer32):
    """Custom type iaSerialOmronFinsAckTimeoutLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IaSerialOmronFinsAckTimeoutLimit_Type.__name__ = "Integer32"
_IaSerialOmronFinsAckTimeoutLimit_Object = MibTableColumn
iaSerialOmronFinsAckTimeoutLimit = _IaSerialOmronFinsAckTimeoutLimit_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 17, 1, 13),
    _IaSerialOmronFinsAckTimeoutLimit_Type()
)
iaSerialOmronFinsAckTimeoutLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialOmronFinsAckTimeoutLimit.setStatus("mandatory")
_IaSerialModbusAsciiSettingsTable_Object = MibTable
iaSerialModbusAsciiSettingsTable = _IaSerialModbusAsciiSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 18)
)
if mibBuilder.loadTexts:
    iaSerialModbusAsciiSettingsTable.setStatus("mandatory")
_IaSerialModbusAsciiSettingsEntry_Object = MibTableRow
iaSerialModbusAsciiSettingsEntry = _IaSerialModbusAsciiSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 18, 1)
)
iaSerialModbusAsciiSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaSerialPortModbusAsciiIndex"),
)
if mibBuilder.loadTexts:
    iaSerialModbusAsciiSettingsEntry.setStatus("mandatory")
_IaSerialPortModbusAsciiIndex_Type = Integer32
_IaSerialPortModbusAsciiIndex_Object = MibTableColumn
iaSerialPortModbusAsciiIndex = _IaSerialPortModbusAsciiIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 18, 1, 11),
    _IaSerialPortModbusAsciiIndex_Type()
)
iaSerialPortModbusAsciiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iaSerialPortModbusAsciiIndex.setStatus("mandatory")


class _IaSerialModbusAsciiFixedAddress_Type(Integer32):
    """Custom type iaSerialModbusAsciiFixedAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IaSerialModbusAsciiFixedAddress_Type.__name__ = "Integer32"
_IaSerialModbusAsciiFixedAddress_Object = MibTableColumn
iaSerialModbusAsciiFixedAddress = _IaSerialModbusAsciiFixedAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 18, 1, 12),
    _IaSerialModbusAsciiFixedAddress_Type()
)
iaSerialModbusAsciiFixedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialModbusAsciiFixedAddress.setStatus("mandatory")


class _IaSerialModbusAsciiBroadcastFlag_Type(Integer32):
    """Custom type iaSerialModbusAsciiBroadcastFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("replace", 3))
    )


_IaSerialModbusAsciiBroadcastFlag_Type.__name__ = "Integer32"
_IaSerialModbusAsciiBroadcastFlag_Object = MibTableColumn
iaSerialModbusAsciiBroadcastFlag = _IaSerialModbusAsciiBroadcastFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 18, 1, 13),
    _IaSerialModbusAsciiBroadcastFlag_Type()
)
iaSerialModbusAsciiBroadcastFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialModbusAsciiBroadcastFlag.setStatus("mandatory")


class _IaSerialModbusAsciiErrorResponseFlag_Type(Integer32):
    """Custom type iaSerialModbusAsciiErrorResponseFlag based on Integer32"""
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


_IaSerialModbusAsciiErrorResponseFlag_Type.__name__ = "Integer32"
_IaSerialModbusAsciiErrorResponseFlag_Object = MibTableColumn
iaSerialModbusAsciiErrorResponseFlag = _IaSerialModbusAsciiErrorResponseFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 18, 1, 14),
    _IaSerialModbusAsciiErrorResponseFlag_Type()
)
iaSerialModbusAsciiErrorResponseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialModbusAsciiErrorResponseFlag.setStatus("mandatory")


class _IaSerialModbusAsciiExtendedTimeout_Type(Integer32):
    """Custom type iaSerialModbusAsciiExtendedTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaSerialModbusAsciiExtendedTimeout_Type.__name__ = "Integer32"
_IaSerialModbusAsciiExtendedTimeout_Object = MibTableColumn
iaSerialModbusAsciiExtendedTimeout = _IaSerialModbusAsciiExtendedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 18, 1, 15),
    _IaSerialModbusAsciiExtendedTimeout_Type()
)
iaSerialModbusAsciiExtendedTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialModbusAsciiExtendedTimeout.setStatus("mandatory")
_IaSerialModbusAsciiExtendedFunctions_Type = DisplayString
_IaSerialModbusAsciiExtendedFunctions_Object = MibTableColumn
iaSerialModbusAsciiExtendedFunctions = _IaSerialModbusAsciiExtendedFunctions_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 18, 1, 16),
    _IaSerialModbusAsciiExtendedFunctions_Type()
)
iaSerialModbusAsciiExtendedFunctions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaSerialModbusAsciiExtendedFunctions.setStatus("mandatory")
_IaSerialModbusAsciiAddExtendedFunctions_Type = DisplayString
_IaSerialModbusAsciiAddExtendedFunctions_Object = MibTableColumn
iaSerialModbusAsciiAddExtendedFunctions = _IaSerialModbusAsciiAddExtendedFunctions_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 18, 1, 17),
    _IaSerialModbusAsciiAddExtendedFunctions_Type()
)
iaSerialModbusAsciiAddExtendedFunctions.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iaSerialModbusAsciiAddExtendedFunctions.setStatus("mandatory")
_IaSerialModbusAsciiRemoveExtendedFunctions_Type = DisplayString
_IaSerialModbusAsciiRemoveExtendedFunctions_Object = MibTableColumn
iaSerialModbusAsciiRemoveExtendedFunctions = _IaSerialModbusAsciiRemoveExtendedFunctions_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 11, 18, 1, 18),
    _IaSerialModbusAsciiRemoveExtendedFunctions_Type()
)
iaSerialModbusAsciiRemoveExtendedFunctions.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iaSerialModbusAsciiRemoveExtendedFunctions.setStatus("mandatory")
_IaNetMasterSettings_ObjectIdentity = ObjectIdentity
iaNetMasterSettings = _IaNetMasterSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12)
)
_IaNetMasterGeneralSettingsTable_Object = MibTable
iaNetMasterGeneralSettingsTable = _IaNetMasterGeneralSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 11)
)
if mibBuilder.loadTexts:
    iaNetMasterGeneralSettingsTable.setStatus("mandatory")
_IaNetMasterGeneralSettingsEntry_Object = MibTableRow
iaNetMasterGeneralSettingsEntry = _IaNetMasterGeneralSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 11, 1)
)
iaNetMasterGeneralSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaNetMasterIndex"),
)
if mibBuilder.loadTexts:
    iaNetMasterGeneralSettingsEntry.setStatus("mandatory")
_IaNetMasterIndex_Type = Integer32
_IaNetMasterIndex_Object = MibTableColumn
iaNetMasterIndex = _IaNetMasterIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 11, 1, 11),
    _IaNetMasterIndex_Type()
)
iaNetMasterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iaNetMasterIndex.setStatus("mandatory")
_IaNetMasterProtocol_Type = IANetProtocol
_IaNetMasterProtocol_Object = MibTableColumn
iaNetMasterProtocol = _IaNetMasterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 11, 1, 12),
    _IaNetMasterProtocol_Type()
)
iaNetMasterProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterProtocol.setStatus("mandatory")
_IaNetMasterModbusTCPSettings_ObjectIdentity = ObjectIdentity
iaNetMasterModbusTCPSettings = _IaNetMasterModbusTCPSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 12)
)


class _IaNetMasterModbusTCPMessageTimeout_Type(Integer32):
    """Custom type iaNetMasterModbusTCPMessageTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaNetMasterModbusTCPMessageTimeout_Type.__name__ = "Integer32"
_IaNetMasterModbusTCPMessageTimeout_Object = MibScalar
iaNetMasterModbusTCPMessageTimeout = _IaNetMasterModbusTCPMessageTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 12, 11),
    _IaNetMasterModbusTCPMessageTimeout_Type()
)
iaNetMasterModbusTCPMessageTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterModbusTCPMessageTimeout.setStatus("mandatory")


class _IaNetMasterModbusTCPConnectTimeout_Type(Integer32):
    """Custom type iaNetMasterModbusTCPConnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaNetMasterModbusTCPConnectTimeout_Type.__name__ = "Integer32"
_IaNetMasterModbusTCPConnectTimeout_Object = MibScalar
iaNetMasterModbusTCPConnectTimeout = _IaNetMasterModbusTCPConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 12, 12),
    _IaNetMasterModbusTCPConnectTimeout_Type()
)
iaNetMasterModbusTCPConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterModbusTCPConnectTimeout.setStatus("mandatory")


class _IaNetMasterModbusTCPActiveFlag_Type(Integer32):
    """Custom type iaNetMasterModbusTCPActiveFlag based on Integer32"""
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


_IaNetMasterModbusTCPActiveFlag_Type.__name__ = "Integer32"
_IaNetMasterModbusTCPActiveFlag_Object = MibScalar
iaNetMasterModbusTCPActiveFlag = _IaNetMasterModbusTCPActiveFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 12, 13),
    _IaNetMasterModbusTCPActiveFlag_Type()
)
iaNetMasterModbusTCPActiveFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterModbusTCPActiveFlag.setStatus("mandatory")


class _IaNetMasterModbusTCPBroadcastFlag_Type(Integer32):
    """Custom type iaNetMasterModbusTCPBroadcastFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("replace", 3))
    )


_IaNetMasterModbusTCPBroadcastFlag_Type.__name__ = "Integer32"
_IaNetMasterModbusTCPBroadcastFlag_Object = MibScalar
iaNetMasterModbusTCPBroadcastFlag = _IaNetMasterModbusTCPBroadcastFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 12, 14),
    _IaNetMasterModbusTCPBroadcastFlag_Type()
)
iaNetMasterModbusTCPBroadcastFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterModbusTCPBroadcastFlag.setStatus("mandatory")


class _IaNetMasterModbusTCPErrorResponseFlag_Type(Integer32):
    """Custom type iaNetMasterModbusTCPErrorResponseFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("replace", 3))
    )


_IaNetMasterModbusTCPErrorResponseFlag_Type.__name__ = "Integer32"
_IaNetMasterModbusTCPErrorResponseFlag_Object = MibScalar
iaNetMasterModbusTCPErrorResponseFlag = _IaNetMasterModbusTCPErrorResponseFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 12, 15),
    _IaNetMasterModbusTCPErrorResponseFlag_Type()
)
iaNetMasterModbusTCPErrorResponseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterModbusTCPErrorResponseFlag.setStatus("mandatory")


class _IaNetMasterModbusTCPExtendedTimeout_Type(Integer32):
    """Custom type iaNetMasterModbusTCPExtendedTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaNetMasterModbusTCPExtendedTimeout_Type.__name__ = "Integer32"
_IaNetMasterModbusTCPExtendedTimeout_Object = MibScalar
iaNetMasterModbusTCPExtendedTimeout = _IaNetMasterModbusTCPExtendedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 12, 16),
    _IaNetMasterModbusTCPExtendedTimeout_Type()
)
iaNetMasterModbusTCPExtendedTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterModbusTCPExtendedTimeout.setStatus("mandatory")
_IaNetMasterModbusTCPExtendedFunctions_Type = DisplayString
_IaNetMasterModbusTCPExtendedFunctions_Object = MibScalar
iaNetMasterModbusTCPExtendedFunctions = _IaNetMasterModbusTCPExtendedFunctions_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 12, 17),
    _IaNetMasterModbusTCPExtendedFunctions_Type()
)
iaNetMasterModbusTCPExtendedFunctions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterModbusTCPExtendedFunctions.setStatus("mandatory")
_IaNetMasterModbusTCPAddExtendedFunctions_Type = DisplayString
_IaNetMasterModbusTCPAddExtendedFunctions_Object = MibScalar
iaNetMasterModbusTCPAddExtendedFunctions = _IaNetMasterModbusTCPAddExtendedFunctions_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 12, 18),
    _IaNetMasterModbusTCPAddExtendedFunctions_Type()
)
iaNetMasterModbusTCPAddExtendedFunctions.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iaNetMasterModbusTCPAddExtendedFunctions.setStatus("mandatory")
_IaNetMasterModbusTCPRemoveExtendedFunctions_Type = DisplayString
_IaNetMasterModbusTCPRemoveExtendedFunctions_Object = MibScalar
iaNetMasterModbusTCPRemoveExtendedFunctions = _IaNetMasterModbusTCPRemoveExtendedFunctions_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 12, 19),
    _IaNetMasterModbusTCPRemoveExtendedFunctions_Type()
)
iaNetMasterModbusTCPRemoveExtendedFunctions.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    iaNetMasterModbusTCPRemoveExtendedFunctions.setStatus("mandatory")
_IaNetMasterABEthernetSettings_ObjectIdentity = ObjectIdentity
iaNetMasterABEthernetSettings = _IaNetMasterABEthernetSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 13)
)


class _IaNetMasterABEthernetMessageTimeout_Type(Integer32):
    """Custom type iaNetMasterABEthernetMessageTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaNetMasterABEthernetMessageTimeout_Type.__name__ = "Integer32"
_IaNetMasterABEthernetMessageTimeout_Object = MibScalar
iaNetMasterABEthernetMessageTimeout = _IaNetMasterABEthernetMessageTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 13, 11),
    _IaNetMasterABEthernetMessageTimeout_Type()
)
iaNetMasterABEthernetMessageTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterABEthernetMessageTimeout.setStatus("mandatory")


class _IaNetMasterABEthernetConnectTimeout_Type(Integer32):
    """Custom type iaNetMasterABEthernetConnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaNetMasterABEthernetConnectTimeout_Type.__name__ = "Integer32"
_IaNetMasterABEthernetConnectTimeout_Object = MibScalar
iaNetMasterABEthernetConnectTimeout = _IaNetMasterABEthernetConnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 13, 12),
    _IaNetMasterABEthernetConnectTimeout_Type()
)
iaNetMasterABEthernetConnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterABEthernetConnectTimeout.setStatus("mandatory")


class _IaNetMasterABEthernetActiveFlag_Type(Integer32):
    """Custom type iaNetMasterABEthernetActiveFlag based on Integer32"""
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


_IaNetMasterABEthernetActiveFlag_Type.__name__ = "Integer32"
_IaNetMasterABEthernetActiveFlag_Object = MibScalar
iaNetMasterABEthernetActiveFlag = _IaNetMasterABEthernetActiveFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 13, 13),
    _IaNetMasterABEthernetActiveFlag_Type()
)
iaNetMasterABEthernetActiveFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterABEthernetActiveFlag.setStatus("mandatory")


class _IaNetMasterABEthernetErrorResponseFlag_Type(Integer32):
    """Custom type iaNetMasterABEthernetErrorResponseFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("replace", 3))
    )


_IaNetMasterABEthernetErrorResponseFlag_Type.__name__ = "Integer32"
_IaNetMasterABEthernetErrorResponseFlag_Object = MibScalar
iaNetMasterABEthernetErrorResponseFlag = _IaNetMasterABEthernetErrorResponseFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 13, 14),
    _IaNetMasterABEthernetErrorResponseFlag_Type()
)
iaNetMasterABEthernetErrorResponseFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterABEthernetErrorResponseFlag.setStatus("mandatory")
_IaNetMasterEthernetIPSettings_ObjectIdentity = ObjectIdentity
iaNetMasterEthernetIPSettings = _IaNetMasterEthernetIPSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 14)
)


class _IaNetMasterEthernetIPMessageTimeout_Type(Integer32):
    """Custom type iaNetMasterEthernetIPMessageTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IaNetMasterEthernetIPMessageTimeout_Type.__name__ = "Integer32"
_IaNetMasterEthernetIPMessageTimeout_Object = MibScalar
iaNetMasterEthernetIPMessageTimeout = _IaNetMasterEthernetIPMessageTimeout_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 14, 11),
    _IaNetMasterEthernetIPMessageTimeout_Type()
)
iaNetMasterEthernetIPMessageTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterEthernetIPMessageTimeout.setStatus("mandatory")


class _IaNetMasterEthernetIPActiveFlag_Type(Integer32):
    """Custom type iaNetMasterEthernetIPActiveFlag based on Integer32"""
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


_IaNetMasterEthernetIPActiveFlag_Type.__name__ = "Integer32"
_IaNetMasterEthernetIPActiveFlag_Object = MibScalar
iaNetMasterEthernetIPActiveFlag = _IaNetMasterEthernetIPActiveFlag_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 12, 14, 12),
    _IaNetMasterEthernetIPActiveFlag_Type()
)
iaNetMasterEthernetIPActiveFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetMasterEthernetIPActiveFlag.setStatus("mandatory")
_IaNetSlaveSettings_ObjectIdentity = ObjectIdentity
iaNetSlaveSettings = _IaNetSlaveSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 13)
)
_IaNetSlaveGeneralSettingsTable_Object = MibTable
iaNetSlaveGeneralSettingsTable = _IaNetSlaveGeneralSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 13, 11)
)
if mibBuilder.loadTexts:
    iaNetSlaveGeneralSettingsTable.setStatus("obsolete")
_IaNetSlaveGeneralSettingsEntry_Object = MibTableRow
iaNetSlaveGeneralSettingsEntry = _IaNetSlaveGeneralSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 13, 11, 1)
)
iaNetSlaveGeneralSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaNetSlaveIndex"),
)
if mibBuilder.loadTexts:
    iaNetSlaveGeneralSettingsEntry.setStatus("obsolete")
_IaNetSlaveIndex_Type = Integer32
_IaNetSlaveIndex_Object = MibTableColumn
iaNetSlaveIndex = _IaNetSlaveIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 13, 11, 1, 11),
    _IaNetSlaveIndex_Type()
)
iaNetSlaveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iaNetSlaveIndex.setStatus("obsolete")
_IaNetSlaveProtocol_Type = IANetProtocol
_IaNetSlaveProtocol_Object = MibTableColumn
iaNetSlaveProtocol = _IaNetSlaveProtocol_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 13, 11, 1, 12),
    _IaNetSlaveProtocol_Type()
)
iaNetSlaveProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetSlaveProtocol.setStatus("obsolete")
_IaNetSlaveIpAddress_Type = IpAddress
_IaNetSlaveIpAddress_Object = MibTableColumn
iaNetSlaveIpAddress = _IaNetSlaveIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 13, 11, 1, 13),
    _IaNetSlaveIpAddress_Type()
)
iaNetSlaveIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetSlaveIpAddress.setStatus("obsolete")
_IaNetSlaveIpPort_Type = Integer32
_IaNetSlaveIpPort_Object = MibTableColumn
iaNetSlaveIpPort = _IaNetSlaveIpPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 13, 11, 1, 14),
    _IaNetSlaveIpPort_Type()
)
iaNetSlaveIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetSlaveIpPort.setStatus("obsolete")
_IaNetSlaveReconnectTime_Type = Integer32
_IaNetSlaveReconnectTime_Object = MibTableColumn
iaNetSlaveReconnectTime = _IaNetSlaveReconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 13, 11, 1, 15),
    _IaNetSlaveReconnectTime_Type()
)
iaNetSlaveReconnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetSlaveReconnectTime.setStatus("obsolete")
_IaNetSlaveName_Type = DisplayString
_IaNetSlaveName_Object = MibTableColumn
iaNetSlaveName = _IaNetSlaveName_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 13, 11, 1, 16),
    _IaNetSlaveName_Type()
)
iaNetSlaveName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetSlaveName.setStatus("obsolete")
_IaNetSlaveActivateNextFree_Type = Integer32
_IaNetSlaveActivateNextFree_Object = MibScalar
iaNetSlaveActivateNextFree = _IaNetSlaveActivateNextFree_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 13, 12),
    _IaNetSlaveActivateNextFree_Type()
)
iaNetSlaveActivateNextFree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaNetSlaveActivateNextFree.setStatus("obsolete")
_IaStatistics_ObjectIdentity = ObjectIdentity
iaStatistics = _IaStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14)
)
_IaStatisticsClear_Type = Switch
_IaStatisticsClear_Object = MibScalar
iaStatisticsClear = _IaStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 10),
    _IaStatisticsClear_Type()
)
iaStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaStatisticsClear.setStatus("mandatory")
_IaStatisticsModbus_ObjectIdentity = ObjectIdentity
iaStatisticsModbus = _IaStatisticsModbus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11)
)
_ModbusResourceErrors_Type = Integer32
_ModbusResourceErrors_Object = MibScalar
modbusResourceErrors = _ModbusResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 11),
    _ModbusResourceErrors_Type()
)
modbusResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusResourceErrors.setStatus("mandatory")
_ModbusConfigurationErrors_Type = Integer32
_ModbusConfigurationErrors_Object = MibScalar
modbusConfigurationErrors = _ModbusConfigurationErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 12),
    _ModbusConfigurationErrors_Type()
)
modbusConfigurationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusConfigurationErrors.setStatus("mandatory")
_ModbusBadRequestMessageErrors_Type = Integer32
_ModbusBadRequestMessageErrors_Object = MibScalar
modbusBadRequestMessageErrors = _ModbusBadRequestMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 13),
    _ModbusBadRequestMessageErrors_Type()
)
modbusBadRequestMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusBadRequestMessageErrors.setStatus("mandatory")
_ModbusBadResponseMessageErrors_Type = Integer32
_ModbusBadResponseMessageErrors_Object = MibScalar
modbusBadResponseMessageErrors = _ModbusBadResponseMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 14),
    _ModbusBadResponseMessageErrors_Type()
)
modbusBadResponseMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusBadResponseMessageErrors.setStatus("mandatory")
_ModbusRequestMessageDroppedErrors_Type = Integer32
_ModbusRequestMessageDroppedErrors_Object = MibScalar
modbusRequestMessageDroppedErrors = _ModbusRequestMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 15),
    _ModbusRequestMessageDroppedErrors_Type()
)
modbusRequestMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusRequestMessageDroppedErrors.setStatus("mandatory")
_ModbusResponseMessageDroppedErrors_Type = Integer32
_ModbusResponseMessageDroppedErrors_Object = MibScalar
modbusResponseMessageDroppedErrors = _ModbusResponseMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 16),
    _ModbusResponseMessageDroppedErrors_Type()
)
modbusResponseMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusResponseMessageDroppedErrors.setStatus("mandatory")
_ModbusMessageTimeoutErrors_Type = Integer32
_ModbusMessageTimeoutErrors_Object = MibScalar
modbusMessageTimeoutErrors = _ModbusMessageTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 17),
    _ModbusMessageTimeoutErrors_Type()
)
modbusMessageTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusMessageTimeoutErrors.setStatus("mandatory")
_ModbusChecksumErrors_Type = Integer32
_ModbusChecksumErrors_Object = MibScalar
modbusChecksumErrors = _ModbusChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 18),
    _ModbusChecksumErrors_Type()
)
modbusChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusChecksumErrors.setStatus("mandatory")
_ModbusValidRequests_Type = Integer32
_ModbusValidRequests_Object = MibScalar
modbusValidRequests = _ModbusValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 19),
    _ModbusValidRequests_Type()
)
modbusValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusValidRequests.setStatus("mandatory")
_ModbusValidResponses_Type = Integer32
_ModbusValidResponses_Object = MibScalar
modbusValidResponses = _ModbusValidResponses_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 20),
    _ModbusValidResponses_Type()
)
modbusValidResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusValidResponses.setStatus("mandatory")
_ModbusNetworkHangups_Type = Integer32
_ModbusNetworkHangups_Object = MibScalar
modbusNetworkHangups = _ModbusNetworkHangups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 21),
    _ModbusNetworkHangups_Type()
)
modbusNetworkHangups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusNetworkHangups.setStatus("mandatory")
_ModbusActiveMasterConnections_Type = Integer32
_ModbusActiveMasterConnections_Object = MibScalar
modbusActiveMasterConnections = _ModbusActiveMasterConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 22),
    _ModbusActiveMasterConnections_Type()
)
modbusActiveMasterConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusActiveMasterConnections.setStatus("mandatory")
_ModbusActiveSlaveConnections_Type = Integer32
_ModbusActiveSlaveConnections_Object = MibScalar
modbusActiveSlaveConnections = _ModbusActiveSlaveConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 11, 23),
    _ModbusActiveSlaveConnections_Type()
)
modbusActiveSlaveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modbusActiveSlaveConnections.setStatus("mandatory")
_IaStatisticsDF1FullDuplex_ObjectIdentity = ObjectIdentity
iaStatisticsDF1FullDuplex = _IaStatisticsDF1FullDuplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12)
)
_Df1FullDuplexResourceErrors_Type = Integer32
_Df1FullDuplexResourceErrors_Object = MibScalar
df1FullDuplexResourceErrors = _Df1FullDuplexResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 11),
    _Df1FullDuplexResourceErrors_Type()
)
df1FullDuplexResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexResourceErrors.setStatus("mandatory")
_Df1FullDuplexConfigurationErrors_Type = Integer32
_Df1FullDuplexConfigurationErrors_Object = MibScalar
df1FullDuplexConfigurationErrors = _Df1FullDuplexConfigurationErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 12),
    _Df1FullDuplexConfigurationErrors_Type()
)
df1FullDuplexConfigurationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexConfigurationErrors.setStatus("mandatory")
_Df1FullDuplexBadRequestMessageErrors_Type = Integer32
_Df1FullDuplexBadRequestMessageErrors_Object = MibScalar
df1FullDuplexBadRequestMessageErrors = _Df1FullDuplexBadRequestMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 13),
    _Df1FullDuplexBadRequestMessageErrors_Type()
)
df1FullDuplexBadRequestMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexBadRequestMessageErrors.setStatus("mandatory")
_Df1FullDuplexBadResponseMessageErrors_Type = Integer32
_Df1FullDuplexBadResponseMessageErrors_Object = MibScalar
df1FullDuplexBadResponseMessageErrors = _Df1FullDuplexBadResponseMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 14),
    _Df1FullDuplexBadResponseMessageErrors_Type()
)
df1FullDuplexBadResponseMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexBadResponseMessageErrors.setStatus("mandatory")
_Df1FullDuplexRequestMessageDroppedErrors_Type = Integer32
_Df1FullDuplexRequestMessageDroppedErrors_Object = MibScalar
df1FullDuplexRequestMessageDroppedErrors = _Df1FullDuplexRequestMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 15),
    _Df1FullDuplexRequestMessageDroppedErrors_Type()
)
df1FullDuplexRequestMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexRequestMessageDroppedErrors.setStatus("mandatory")
_Df1FullDuplexResponseMessageDroppedErrors_Type = Integer32
_Df1FullDuplexResponseMessageDroppedErrors_Object = MibScalar
df1FullDuplexResponseMessageDroppedErrors = _Df1FullDuplexResponseMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 16),
    _Df1FullDuplexResponseMessageDroppedErrors_Type()
)
df1FullDuplexResponseMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexResponseMessageDroppedErrors.setStatus("mandatory")
_Df1FullDuplexMessageTimeoutErrors_Type = Integer32
_Df1FullDuplexMessageTimeoutErrors_Object = MibScalar
df1FullDuplexMessageTimeoutErrors = _Df1FullDuplexMessageTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 17),
    _Df1FullDuplexMessageTimeoutErrors_Type()
)
df1FullDuplexMessageTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexMessageTimeoutErrors.setStatus("mandatory")
_Df1FullDuplexChecksumErrors_Type = Integer32
_Df1FullDuplexChecksumErrors_Object = MibScalar
df1FullDuplexChecksumErrors = _Df1FullDuplexChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 18),
    _Df1FullDuplexChecksumErrors_Type()
)
df1FullDuplexChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexChecksumErrors.setStatus("mandatory")
_Df1FullDuplexValidRequests_Type = Integer32
_Df1FullDuplexValidRequests_Object = MibScalar
df1FullDuplexValidRequests = _Df1FullDuplexValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 19),
    _Df1FullDuplexValidRequests_Type()
)
df1FullDuplexValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexValidRequests.setStatus("mandatory")
_Df1FullDuplexValidResponses_Type = Integer32
_Df1FullDuplexValidResponses_Object = MibScalar
df1FullDuplexValidResponses = _Df1FullDuplexValidResponses_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 20),
    _Df1FullDuplexValidResponses_Type()
)
df1FullDuplexValidResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexValidResponses.setStatus("mandatory")
_Df1FullDuplexNetworkHangups_Type = Integer32
_Df1FullDuplexNetworkHangups_Object = MibScalar
df1FullDuplexNetworkHangups = _Df1FullDuplexNetworkHangups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 21),
    _Df1FullDuplexNetworkHangups_Type()
)
df1FullDuplexNetworkHangups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexNetworkHangups.setStatus("mandatory")
_Df1FullDuplexActiveMasterConnections_Type = Integer32
_Df1FullDuplexActiveMasterConnections_Object = MibScalar
df1FullDuplexActiveMasterConnections = _Df1FullDuplexActiveMasterConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 22),
    _Df1FullDuplexActiveMasterConnections_Type()
)
df1FullDuplexActiveMasterConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexActiveMasterConnections.setStatus("mandatory")
_Df1FullDuplexActiveSlaveConnections_Type = Integer32
_Df1FullDuplexActiveSlaveConnections_Object = MibScalar
df1FullDuplexActiveSlaveConnections = _Df1FullDuplexActiveSlaveConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 12, 23),
    _Df1FullDuplexActiveSlaveConnections_Type()
)
df1FullDuplexActiveSlaveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1FullDuplexActiveSlaveConnections.setStatus("mandatory")
_IaStatisticsOmronHostLink_ObjectIdentity = ObjectIdentity
iaStatisticsOmronHostLink = _IaStatisticsOmronHostLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13)
)
_OmronHostLinkResourceErrors_Type = Integer32
_OmronHostLinkResourceErrors_Object = MibScalar
omronHostLinkResourceErrors = _OmronHostLinkResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 11),
    _OmronHostLinkResourceErrors_Type()
)
omronHostLinkResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkResourceErrors.setStatus("mandatory")
_OmronHostLinkConfigurationErrors_Type = Integer32
_OmronHostLinkConfigurationErrors_Object = MibScalar
omronHostLinkConfigurationErrors = _OmronHostLinkConfigurationErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 12),
    _OmronHostLinkConfigurationErrors_Type()
)
omronHostLinkConfigurationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkConfigurationErrors.setStatus("mandatory")
_OmronHostLinkBadRequestMessageErrors_Type = Integer32
_OmronHostLinkBadRequestMessageErrors_Object = MibScalar
omronHostLinkBadRequestMessageErrors = _OmronHostLinkBadRequestMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 13),
    _OmronHostLinkBadRequestMessageErrors_Type()
)
omronHostLinkBadRequestMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkBadRequestMessageErrors.setStatus("mandatory")
_OmronHostLinkBadResponseMessageErrors_Type = Integer32
_OmronHostLinkBadResponseMessageErrors_Object = MibScalar
omronHostLinkBadResponseMessageErrors = _OmronHostLinkBadResponseMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 14),
    _OmronHostLinkBadResponseMessageErrors_Type()
)
omronHostLinkBadResponseMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkBadResponseMessageErrors.setStatus("mandatory")
_OmronHostLinkRequestMessageDroppedErrors_Type = Integer32
_OmronHostLinkRequestMessageDroppedErrors_Object = MibScalar
omronHostLinkRequestMessageDroppedErrors = _OmronHostLinkRequestMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 15),
    _OmronHostLinkRequestMessageDroppedErrors_Type()
)
omronHostLinkRequestMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkRequestMessageDroppedErrors.setStatus("mandatory")
_OmronHostLinkResponseMessageDroppedErrors_Type = Integer32
_OmronHostLinkResponseMessageDroppedErrors_Object = MibScalar
omronHostLinkResponseMessageDroppedErrors = _OmronHostLinkResponseMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 16),
    _OmronHostLinkResponseMessageDroppedErrors_Type()
)
omronHostLinkResponseMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkResponseMessageDroppedErrors.setStatus("mandatory")
_OmronHostLinkMessageTimeoutErrors_Type = Integer32
_OmronHostLinkMessageTimeoutErrors_Object = MibScalar
omronHostLinkMessageTimeoutErrors = _OmronHostLinkMessageTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 17),
    _OmronHostLinkMessageTimeoutErrors_Type()
)
omronHostLinkMessageTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkMessageTimeoutErrors.setStatus("mandatory")
_OmronHostLinkChecksumErrors_Type = Integer32
_OmronHostLinkChecksumErrors_Object = MibScalar
omronHostLinkChecksumErrors = _OmronHostLinkChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 18),
    _OmronHostLinkChecksumErrors_Type()
)
omronHostLinkChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkChecksumErrors.setStatus("mandatory")
_OmronHostLinkValidRequests_Type = Integer32
_OmronHostLinkValidRequests_Object = MibScalar
omronHostLinkValidRequests = _OmronHostLinkValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 19),
    _OmronHostLinkValidRequests_Type()
)
omronHostLinkValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkValidRequests.setStatus("mandatory")
_OmronHostLinkValidResponses_Type = Integer32
_OmronHostLinkValidResponses_Object = MibScalar
omronHostLinkValidResponses = _OmronHostLinkValidResponses_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 20),
    _OmronHostLinkValidResponses_Type()
)
omronHostLinkValidResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkValidResponses.setStatus("mandatory")
_OmronHostLinkNetworkHangups_Type = Integer32
_OmronHostLinkNetworkHangups_Object = MibScalar
omronHostLinkNetworkHangups = _OmronHostLinkNetworkHangups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 21),
    _OmronHostLinkNetworkHangups_Type()
)
omronHostLinkNetworkHangups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkNetworkHangups.setStatus("mandatory")
_OmronHostLinkActiveMasterConnections_Type = Integer32
_OmronHostLinkActiveMasterConnections_Object = MibScalar
omronHostLinkActiveMasterConnections = _OmronHostLinkActiveMasterConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 22),
    _OmronHostLinkActiveMasterConnections_Type()
)
omronHostLinkActiveMasterConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkActiveMasterConnections.setStatus("mandatory")
_OmronHostLinkActiveSlaveConnections_Type = Integer32
_OmronHostLinkActiveSlaveConnections_Object = MibScalar
omronHostLinkActiveSlaveConnections = _OmronHostLinkActiveSlaveConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 13, 23),
    _OmronHostLinkActiveSlaveConnections_Type()
)
omronHostLinkActiveSlaveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronHostLinkActiveSlaveConnections.setStatus("mandatory")
_IaStatisticsOmronFins_ObjectIdentity = ObjectIdentity
iaStatisticsOmronFins = _IaStatisticsOmronFins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14)
)
_OmronFinsResourceErrors_Type = Integer32
_OmronFinsResourceErrors_Object = MibScalar
omronFinsResourceErrors = _OmronFinsResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 11),
    _OmronFinsResourceErrors_Type()
)
omronFinsResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsResourceErrors.setStatus("mandatory")
_OmronFinsConfigurationErrors_Type = Integer32
_OmronFinsConfigurationErrors_Object = MibScalar
omronFinsConfigurationErrors = _OmronFinsConfigurationErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 12),
    _OmronFinsConfigurationErrors_Type()
)
omronFinsConfigurationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsConfigurationErrors.setStatus("mandatory")
_OmronFinsBadRequestMessageErrors_Type = Integer32
_OmronFinsBadRequestMessageErrors_Object = MibScalar
omronFinsBadRequestMessageErrors = _OmronFinsBadRequestMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 13),
    _OmronFinsBadRequestMessageErrors_Type()
)
omronFinsBadRequestMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsBadRequestMessageErrors.setStatus("mandatory")
_OmronFinsBadResponseMessageErrors_Type = Integer32
_OmronFinsBadResponseMessageErrors_Object = MibScalar
omronFinsBadResponseMessageErrors = _OmronFinsBadResponseMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 14),
    _OmronFinsBadResponseMessageErrors_Type()
)
omronFinsBadResponseMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsBadResponseMessageErrors.setStatus("mandatory")
_OmronFinsRequestMessageDroppedErrors_Type = Integer32
_OmronFinsRequestMessageDroppedErrors_Object = MibScalar
omronFinsRequestMessageDroppedErrors = _OmronFinsRequestMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 15),
    _OmronFinsRequestMessageDroppedErrors_Type()
)
omronFinsRequestMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsRequestMessageDroppedErrors.setStatus("mandatory")
_OmronFinsResponseMessageDroppedErrors_Type = Integer32
_OmronFinsResponseMessageDroppedErrors_Object = MibScalar
omronFinsResponseMessageDroppedErrors = _OmronFinsResponseMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 16),
    _OmronFinsResponseMessageDroppedErrors_Type()
)
omronFinsResponseMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsResponseMessageDroppedErrors.setStatus("mandatory")
_OmronFinsMessageTimeoutErrors_Type = Integer32
_OmronFinsMessageTimeoutErrors_Object = MibScalar
omronFinsMessageTimeoutErrors = _OmronFinsMessageTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 17),
    _OmronFinsMessageTimeoutErrors_Type()
)
omronFinsMessageTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsMessageTimeoutErrors.setStatus("mandatory")
_OmronFinsChecksumErrors_Type = Integer32
_OmronFinsChecksumErrors_Object = MibScalar
omronFinsChecksumErrors = _OmronFinsChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 18),
    _OmronFinsChecksumErrors_Type()
)
omronFinsChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsChecksumErrors.setStatus("mandatory")
_OmronFinsValidRequests_Type = Integer32
_OmronFinsValidRequests_Object = MibScalar
omronFinsValidRequests = _OmronFinsValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 19),
    _OmronFinsValidRequests_Type()
)
omronFinsValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsValidRequests.setStatus("mandatory")
_OmronFinsValidResponses_Type = Integer32
_OmronFinsValidResponses_Object = MibScalar
omronFinsValidResponses = _OmronFinsValidResponses_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 20),
    _OmronFinsValidResponses_Type()
)
omronFinsValidResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsValidResponses.setStatus("mandatory")
_OmronFinsNetworkHangups_Type = Integer32
_OmronFinsNetworkHangups_Object = MibScalar
omronFinsNetworkHangups = _OmronFinsNetworkHangups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 21),
    _OmronFinsNetworkHangups_Type()
)
omronFinsNetworkHangups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsNetworkHangups.setStatus("mandatory")
_OmronFinsActiveMasterConnections_Type = Integer32
_OmronFinsActiveMasterConnections_Object = MibScalar
omronFinsActiveMasterConnections = _OmronFinsActiveMasterConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 22),
    _OmronFinsActiveMasterConnections_Type()
)
omronFinsActiveMasterConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsActiveMasterConnections.setStatus("mandatory")
_OmronFinsActiveSlaveConnections_Type = Integer32
_OmronFinsActiveSlaveConnections_Object = MibScalar
omronFinsActiveSlaveConnections = _OmronFinsActiveSlaveConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 14, 23),
    _OmronFinsActiveSlaveConnections_Type()
)
omronFinsActiveSlaveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronFinsActiveSlaveConnections.setStatus("mandatory")
_IaStatisticsOmronCompowayf_ObjectIdentity = ObjectIdentity
iaStatisticsOmronCompowayf = _IaStatisticsOmronCompowayf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15)
)
_OmronCompowayfResourceErrors_Type = Integer32
_OmronCompowayfResourceErrors_Object = MibScalar
omronCompowayfResourceErrors = _OmronCompowayfResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 11),
    _OmronCompowayfResourceErrors_Type()
)
omronCompowayfResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfResourceErrors.setStatus("mandatory")
_OmronCompowayfConfigurationErrors_Type = Integer32
_OmronCompowayfConfigurationErrors_Object = MibScalar
omronCompowayfConfigurationErrors = _OmronCompowayfConfigurationErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 12),
    _OmronCompowayfConfigurationErrors_Type()
)
omronCompowayfConfigurationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfConfigurationErrors.setStatus("mandatory")
_OmronCompowayfBadRequestMessageErrors_Type = Integer32
_OmronCompowayfBadRequestMessageErrors_Object = MibScalar
omronCompowayfBadRequestMessageErrors = _OmronCompowayfBadRequestMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 13),
    _OmronCompowayfBadRequestMessageErrors_Type()
)
omronCompowayfBadRequestMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfBadRequestMessageErrors.setStatus("mandatory")
_OmronCompowayfBadResponseMessageErrors_Type = Integer32
_OmronCompowayfBadResponseMessageErrors_Object = MibScalar
omronCompowayfBadResponseMessageErrors = _OmronCompowayfBadResponseMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 14),
    _OmronCompowayfBadResponseMessageErrors_Type()
)
omronCompowayfBadResponseMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfBadResponseMessageErrors.setStatus("mandatory")
_OmronCompowayfRequestMessageDroppedErrors_Type = Integer32
_OmronCompowayfRequestMessageDroppedErrors_Object = MibScalar
omronCompowayfRequestMessageDroppedErrors = _OmronCompowayfRequestMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 15),
    _OmronCompowayfRequestMessageDroppedErrors_Type()
)
omronCompowayfRequestMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfRequestMessageDroppedErrors.setStatus("mandatory")
_OmronCompowayfResponseMessageDroppedErrors_Type = Integer32
_OmronCompowayfResponseMessageDroppedErrors_Object = MibScalar
omronCompowayfResponseMessageDroppedErrors = _OmronCompowayfResponseMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 16),
    _OmronCompowayfResponseMessageDroppedErrors_Type()
)
omronCompowayfResponseMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfResponseMessageDroppedErrors.setStatus("mandatory")
_OmronCompowayfMessageTimeoutErrors_Type = Integer32
_OmronCompowayfMessageTimeoutErrors_Object = MibScalar
omronCompowayfMessageTimeoutErrors = _OmronCompowayfMessageTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 17),
    _OmronCompowayfMessageTimeoutErrors_Type()
)
omronCompowayfMessageTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfMessageTimeoutErrors.setStatus("mandatory")
_OmronCompowayfChecksumErrors_Type = Integer32
_OmronCompowayfChecksumErrors_Object = MibScalar
omronCompowayfChecksumErrors = _OmronCompowayfChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 18),
    _OmronCompowayfChecksumErrors_Type()
)
omronCompowayfChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfChecksumErrors.setStatus("mandatory")
_OmronCompowayfValidRequests_Type = Integer32
_OmronCompowayfValidRequests_Object = MibScalar
omronCompowayfValidRequests = _OmronCompowayfValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 19),
    _OmronCompowayfValidRequests_Type()
)
omronCompowayfValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfValidRequests.setStatus("mandatory")
_OmronCompowayfValidResponses_Type = Integer32
_OmronCompowayfValidResponses_Object = MibScalar
omronCompowayfValidResponses = _OmronCompowayfValidResponses_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 20),
    _OmronCompowayfValidResponses_Type()
)
omronCompowayfValidResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfValidResponses.setStatus("mandatory")
_OmronCompowayfNetworkHangups_Type = Integer32
_OmronCompowayfNetworkHangups_Object = MibScalar
omronCompowayfNetworkHangups = _OmronCompowayfNetworkHangups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 21),
    _OmronCompowayfNetworkHangups_Type()
)
omronCompowayfNetworkHangups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfNetworkHangups.setStatus("mandatory")
_OmronCompowayfActiveMasterConnections_Type = Integer32
_OmronCompowayfActiveMasterConnections_Object = MibScalar
omronCompowayfActiveMasterConnections = _OmronCompowayfActiveMasterConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 22),
    _OmronCompowayfActiveMasterConnections_Type()
)
omronCompowayfActiveMasterConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfActiveMasterConnections.setStatus("mandatory")
_OmronCompowayfActiveSlaveConnections_Type = Integer32
_OmronCompowayfActiveSlaveConnections_Object = MibScalar
omronCompowayfActiveSlaveConnections = _OmronCompowayfActiveSlaveConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 15, 23),
    _OmronCompowayfActiveSlaveConnections_Type()
)
omronCompowayfActiveSlaveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    omronCompowayfActiveSlaveConnections.setStatus("mandatory")
_IaStatisticsUserDefined_ObjectIdentity = ObjectIdentity
iaStatisticsUserDefined = _IaStatisticsUserDefined_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16)
)
_UserDefinedResourceErrors_Type = Integer32
_UserDefinedResourceErrors_Object = MibScalar
userDefinedResourceErrors = _UserDefinedResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 11),
    _UserDefinedResourceErrors_Type()
)
userDefinedResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedResourceErrors.setStatus("mandatory")
_UserDefinedConfigurationErrors_Type = Integer32
_UserDefinedConfigurationErrors_Object = MibScalar
userDefinedConfigurationErrors = _UserDefinedConfigurationErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 12),
    _UserDefinedConfigurationErrors_Type()
)
userDefinedConfigurationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedConfigurationErrors.setStatus("mandatory")
_UserDefinedBadRequestMessageErrors_Type = Integer32
_UserDefinedBadRequestMessageErrors_Object = MibScalar
userDefinedBadRequestMessageErrors = _UserDefinedBadRequestMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 13),
    _UserDefinedBadRequestMessageErrors_Type()
)
userDefinedBadRequestMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedBadRequestMessageErrors.setStatus("mandatory")
_UserDefinedBadResponseMessageErrors_Type = Integer32
_UserDefinedBadResponseMessageErrors_Object = MibScalar
userDefinedBadResponseMessageErrors = _UserDefinedBadResponseMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 14),
    _UserDefinedBadResponseMessageErrors_Type()
)
userDefinedBadResponseMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedBadResponseMessageErrors.setStatus("mandatory")
_UserDefinedRequestMessageDroppedErrors_Type = Integer32
_UserDefinedRequestMessageDroppedErrors_Object = MibScalar
userDefinedRequestMessageDroppedErrors = _UserDefinedRequestMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 15),
    _UserDefinedRequestMessageDroppedErrors_Type()
)
userDefinedRequestMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedRequestMessageDroppedErrors.setStatus("mandatory")
_UserDefinedResponseMessageDroppedErrors_Type = Integer32
_UserDefinedResponseMessageDroppedErrors_Object = MibScalar
userDefinedResponseMessageDroppedErrors = _UserDefinedResponseMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 16),
    _UserDefinedResponseMessageDroppedErrors_Type()
)
userDefinedResponseMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedResponseMessageDroppedErrors.setStatus("mandatory")
_UserDefinedMessageTimeoutErrors_Type = Integer32
_UserDefinedMessageTimeoutErrors_Object = MibScalar
userDefinedMessageTimeoutErrors = _UserDefinedMessageTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 17),
    _UserDefinedMessageTimeoutErrors_Type()
)
userDefinedMessageTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedMessageTimeoutErrors.setStatus("mandatory")
_UserDefinedChecksumErrors_Type = Integer32
_UserDefinedChecksumErrors_Object = MibScalar
userDefinedChecksumErrors = _UserDefinedChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 18),
    _UserDefinedChecksumErrors_Type()
)
userDefinedChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedChecksumErrors.setStatus("mandatory")
_UserDefinedValidRequests_Type = Integer32
_UserDefinedValidRequests_Object = MibScalar
userDefinedValidRequests = _UserDefinedValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 19),
    _UserDefinedValidRequests_Type()
)
userDefinedValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedValidRequests.setStatus("mandatory")
_UserDefinedValidResponses_Type = Integer32
_UserDefinedValidResponses_Object = MibScalar
userDefinedValidResponses = _UserDefinedValidResponses_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 20),
    _UserDefinedValidResponses_Type()
)
userDefinedValidResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedValidResponses.setStatus("mandatory")
_UserDefinedNetworkHangups_Type = Integer32
_UserDefinedNetworkHangups_Object = MibScalar
userDefinedNetworkHangups = _UserDefinedNetworkHangups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 21),
    _UserDefinedNetworkHangups_Type()
)
userDefinedNetworkHangups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedNetworkHangups.setStatus("mandatory")
_UserDefinedActiveMasterConnections_Type = Integer32
_UserDefinedActiveMasterConnections_Object = MibScalar
userDefinedActiveMasterConnections = _UserDefinedActiveMasterConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 22),
    _UserDefinedActiveMasterConnections_Type()
)
userDefinedActiveMasterConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedActiveMasterConnections.setStatus("mandatory")
_UserDefinedActiveSlaveConnections_Type = Integer32
_UserDefinedActiveSlaveConnections_Object = MibScalar
userDefinedActiveSlaveConnections = _UserDefinedActiveSlaveConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 16, 23),
    _UserDefinedActiveSlaveConnections_Type()
)
userDefinedActiveSlaveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userDefinedActiveSlaveConnections.setStatus("mandatory")
_IaStatisticsDF1HalfDuplex_ObjectIdentity = ObjectIdentity
iaStatisticsDF1HalfDuplex = _IaStatisticsDF1HalfDuplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17)
)
_Df1HalfDuplexResourceErrors_Type = Integer32
_Df1HalfDuplexResourceErrors_Object = MibScalar
df1HalfDuplexResourceErrors = _Df1HalfDuplexResourceErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 11),
    _Df1HalfDuplexResourceErrors_Type()
)
df1HalfDuplexResourceErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexResourceErrors.setStatus("mandatory")
_Df1HalfDuplexConfigurationErrors_Type = Integer32
_Df1HalfDuplexConfigurationErrors_Object = MibScalar
df1HalfDuplexConfigurationErrors = _Df1HalfDuplexConfigurationErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 12),
    _Df1HalfDuplexConfigurationErrors_Type()
)
df1HalfDuplexConfigurationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexConfigurationErrors.setStatus("mandatory")
_Df1HalfDuplexBadRequestMessageErrors_Type = Integer32
_Df1HalfDuplexBadRequestMessageErrors_Object = MibScalar
df1HalfDuplexBadRequestMessageErrors = _Df1HalfDuplexBadRequestMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 13),
    _Df1HalfDuplexBadRequestMessageErrors_Type()
)
df1HalfDuplexBadRequestMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexBadRequestMessageErrors.setStatus("mandatory")
_Df1HalfDuplexBadResponseMessageErrors_Type = Integer32
_Df1HalfDuplexBadResponseMessageErrors_Object = MibScalar
df1HalfDuplexBadResponseMessageErrors = _Df1HalfDuplexBadResponseMessageErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 14),
    _Df1HalfDuplexBadResponseMessageErrors_Type()
)
df1HalfDuplexBadResponseMessageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexBadResponseMessageErrors.setStatus("mandatory")
_Df1HalfDuplexRequestMessageDroppedErrors_Type = Integer32
_Df1HalfDuplexRequestMessageDroppedErrors_Object = MibScalar
df1HalfDuplexRequestMessageDroppedErrors = _Df1HalfDuplexRequestMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 15),
    _Df1HalfDuplexRequestMessageDroppedErrors_Type()
)
df1HalfDuplexRequestMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexRequestMessageDroppedErrors.setStatus("mandatory")
_Df1HalfDuplexResponseMessageDroppedErrors_Type = Integer32
_Df1HalfDuplexResponseMessageDroppedErrors_Object = MibScalar
df1HalfDuplexResponseMessageDroppedErrors = _Df1HalfDuplexResponseMessageDroppedErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 16),
    _Df1HalfDuplexResponseMessageDroppedErrors_Type()
)
df1HalfDuplexResponseMessageDroppedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexResponseMessageDroppedErrors.setStatus("mandatory")
_Df1HalfDuplexMessageTimeoutErrors_Type = Integer32
_Df1HalfDuplexMessageTimeoutErrors_Object = MibScalar
df1HalfDuplexMessageTimeoutErrors = _Df1HalfDuplexMessageTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 17),
    _Df1HalfDuplexMessageTimeoutErrors_Type()
)
df1HalfDuplexMessageTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexMessageTimeoutErrors.setStatus("mandatory")
_Df1HalfDuplexChecksumErrors_Type = Integer32
_Df1HalfDuplexChecksumErrors_Object = MibScalar
df1HalfDuplexChecksumErrors = _Df1HalfDuplexChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 18),
    _Df1HalfDuplexChecksumErrors_Type()
)
df1HalfDuplexChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexChecksumErrors.setStatus("mandatory")
_Df1HalfDuplexValidRequests_Type = Integer32
_Df1HalfDuplexValidRequests_Object = MibScalar
df1HalfDuplexValidRequests = _Df1HalfDuplexValidRequests_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 19),
    _Df1HalfDuplexValidRequests_Type()
)
df1HalfDuplexValidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexValidRequests.setStatus("mandatory")
_Df1HalfDuplexValidResponses_Type = Integer32
_Df1HalfDuplexValidResponses_Object = MibScalar
df1HalfDuplexValidResponses = _Df1HalfDuplexValidResponses_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 20),
    _Df1HalfDuplexValidResponses_Type()
)
df1HalfDuplexValidResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexValidResponses.setStatus("mandatory")
_Df1HalfDuplexNetworkHangups_Type = Integer32
_Df1HalfDuplexNetworkHangups_Object = MibScalar
df1HalfDuplexNetworkHangups = _Df1HalfDuplexNetworkHangups_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 21),
    _Df1HalfDuplexNetworkHangups_Type()
)
df1HalfDuplexNetworkHangups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexNetworkHangups.setStatus("mandatory")
_Df1HalfDuplexActiveMasterConnections_Type = Integer32
_Df1HalfDuplexActiveMasterConnections_Object = MibScalar
df1HalfDuplexActiveMasterConnections = _Df1HalfDuplexActiveMasterConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 22),
    _Df1HalfDuplexActiveMasterConnections_Type()
)
df1HalfDuplexActiveMasterConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexActiveMasterConnections.setStatus("mandatory")
_Df1HalfDuplexActiveSlaveConnections_Type = Integer32
_Df1HalfDuplexActiveSlaveConnections_Object = MibScalar
df1HalfDuplexActiveSlaveConnections = _Df1HalfDuplexActiveSlaveConnections_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 14, 17, 23),
    _Df1HalfDuplexActiveSlaveConnections_Type()
)
df1HalfDuplexActiveSlaveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    df1HalfDuplexActiveSlaveConnections.setStatus("mandatory")
_IaRouteSettings_ObjectIdentity = ObjectIdentity
iaRouteSettings = _IaRouteSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15)
)
_IaRouteGeneralSettingsTable_Object = MibTable
iaRouteGeneralSettingsTable = _IaRouteGeneralSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11)
)
if mibBuilder.loadTexts:
    iaRouteGeneralSettingsTable.setStatus("mandatory")
_IaRouteGeneralSettingsEntry_Object = MibTableRow
iaRouteGeneralSettingsEntry = _IaRouteGeneralSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1)
)
iaRouteGeneralSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaRouteIndex"),
)
if mibBuilder.loadTexts:
    iaRouteGeneralSettingsEntry.setStatus("mandatory")
_IaRouteIndex_Type = Integer32
_IaRouteIndex_Object = MibTableColumn
iaRouteIndex = _IaRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 11),
    _IaRouteIndex_Type()
)
iaRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iaRouteIndex.setStatus("mandatory")
_IaRouteDestinationType_Type = IARouteType
_IaRouteDestinationType_Object = MibTableColumn
iaRouteDestinationType = _IaRouteDestinationType_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 12),
    _IaRouteDestinationType_Type()
)
iaRouteDestinationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteDestinationType.setStatus("mandatory")
_IaRouteDestinationIndex_Type = Integer32
_IaRouteDestinationIndex_Object = MibTableColumn
iaRouteDestinationIndex = _IaRouteDestinationIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 13),
    _IaRouteDestinationIndex_Type()
)
iaRouteDestinationIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteDestinationIndex.setStatus("mandatory")
_IaRouteTransmitAllMessages_Type = Switch
_IaRouteTransmitAllMessages_Object = MibTableColumn
iaRouteTransmitAllMessages = _IaRouteTransmitAllMessages_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 14),
    _IaRouteTransmitAllMessages_Type()
)
iaRouteTransmitAllMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteTransmitAllMessages.setStatus("mandatory")
_IaRouteTransmitMinRange_Type = Integer32
_IaRouteTransmitMinRange_Object = MibTableColumn
iaRouteTransmitMinRange = _IaRouteTransmitMinRange_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 15),
    _IaRouteTransmitMinRange_Type()
)
iaRouteTransmitMinRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteTransmitMinRange.setStatus("mandatory")
_IaRouteTransmitMaxRange_Type = Integer32
_IaRouteTransmitMaxRange_Object = MibTableColumn
iaRouteTransmitMaxRange = _IaRouteTransmitMaxRange_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 16),
    _IaRouteTransmitMaxRange_Type()
)
iaRouteTransmitMaxRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteTransmitMaxRange.setStatus("mandatory")
_IaRouteNetSlaveProtocol_Type = IANetProtocol
_IaRouteNetSlaveProtocol_Object = MibTableColumn
iaRouteNetSlaveProtocol = _IaRouteNetSlaveProtocol_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 17),
    _IaRouteNetSlaveProtocol_Type()
)
iaRouteNetSlaveProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteNetSlaveProtocol.setStatus("mandatory")
_IaRouteNetSlaveIpAddress_Type = IpAddress
_IaRouteNetSlaveIpAddress_Object = MibTableColumn
iaRouteNetSlaveIpAddress = _IaRouteNetSlaveIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 18),
    _IaRouteNetSlaveIpAddress_Type()
)
iaRouteNetSlaveIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteNetSlaveIpAddress.setStatus("mandatory")
_IaRouteNetSlaveIpPort_Type = Integer32
_IaRouteNetSlaveIpPort_Object = MibTableColumn
iaRouteNetSlaveIpPort = _IaRouteNetSlaveIpPort_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 19),
    _IaRouteNetSlaveIpPort_Type()
)
iaRouteNetSlaveIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteNetSlaveIpPort.setStatus("mandatory")
_IaRouteNetSlaveReconnectTime_Type = Integer32
_IaRouteNetSlaveReconnectTime_Object = MibTableColumn
iaRouteNetSlaveReconnectTime = _IaRouteNetSlaveReconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 20),
    _IaRouteNetSlaveReconnectTime_Type()
)
iaRouteNetSlaveReconnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteNetSlaveReconnectTime.setStatus("mandatory")
_IaRouteDescription_Type = DisplayString
_IaRouteDescription_Object = MibTableColumn
iaRouteDescription = _IaRouteDescription_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 21),
    _IaRouteDescription_Type()
)
iaRouteDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteDescription.setStatus("mandatory")
_IaRouteRemoveEntry_Type = Integer32
_IaRouteRemoveEntry_Object = MibTableColumn
iaRouteRemoveEntry = _IaRouteRemoveEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 11, 1, 22),
    _IaRouteRemoveEntry_Type()
)
iaRouteRemoveEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteRemoveEntry.setStatus("mandatory")
_IaRouteNetSlaveModbusTCPSettingsTable_Object = MibTable
iaRouteNetSlaveModbusTCPSettingsTable = _IaRouteNetSlaveModbusTCPSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 12)
)
if mibBuilder.loadTexts:
    iaRouteNetSlaveModbusTCPSettingsTable.setStatus("mandatory")
_IaRouteNetSlaveModbusTCPSettingsEntry_Object = MibTableRow
iaRouteNetSlaveModbusTCPSettingsEntry = _IaRouteNetSlaveModbusTCPSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 12, 1)
)
iaRouteNetSlaveModbusTCPSettingsEntry.setIndexNames(
    (0, "DIGI-IA-MIB", "iaRouteNetSlaveModbusTCPIndex"),
)
if mibBuilder.loadTexts:
    iaRouteNetSlaveModbusTCPSettingsEntry.setStatus("mandatory")
_IaRouteNetSlaveModbusTCPIndex_Type = Integer32
_IaRouteNetSlaveModbusTCPIndex_Object = MibTableColumn
iaRouteNetSlaveModbusTCPIndex = _IaRouteNetSlaveModbusTCPIndex_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 12, 1, 11),
    _IaRouteNetSlaveModbusTCPIndex_Type()
)
iaRouteNetSlaveModbusTCPIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteNetSlaveModbusTCPIndex.setStatus("mandatory")
_IaRouteNetSlaveModbusTCPFixedAddress_Type = Integer32
_IaRouteNetSlaveModbusTCPFixedAddress_Object = MibTableColumn
iaRouteNetSlaveModbusTCPFixedAddress = _IaRouteNetSlaveModbusTCPFixedAddress_Object(
    (1, 3, 6, 1, 4, 1, 332, 10, 11, 12, 15, 12, 1, 12),
    _IaRouteNetSlaveModbusTCPFixedAddress_Type()
)
iaRouteNetSlaveModbusTCPFixedAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iaRouteNetSlaveModbusTCPFixedAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIGI-IA-MIB",
    **{"Switch": Switch,
       "IAProtocol": IAProtocol,
       "IANetProtocol": IANetProtocol,
       "IAType": IAType,
       "IARouteType": IARouteType,
       "DisplayString": DisplayString,
       "iaSerialSettings": iaSerialSettings,
       "iaSerialGeneralSettingsTable": iaSerialGeneralSettingsTable,
       "iaSerialGeneralSettingsEntry": iaSerialGeneralSettingsEntry,
       "iaSerialPortIndex": iaSerialPortIndex,
       "iaSerialPortType": iaSerialPortType,
       "iaSerialPortProtocol": iaSerialPortProtocol,
       "iaSerialMessageTimeout": iaSerialMessageTimeout,
       "iaSerialNetSlaveList": iaSerialNetSlaveList,
       "iaSerialRevert": iaSerialRevert,
       "iaSerialResetNetSlaves": iaSerialResetNetSlaves,
       "iaSerialAddRouteEntry": iaSerialAddRouteEntry,
       "iaSerialModbusRTUSettingsTable": iaSerialModbusRTUSettingsTable,
       "iaSerialModbusRTUSettingsEntry": iaSerialModbusRTUSettingsEntry,
       "iaSerialPortModbusRTUIndex": iaSerialPortModbusRTUIndex,
       "iaSerialModbusRTUTimeout": iaSerialModbusRTUTimeout,
       "iaSerialModbusRTUFixedAddress": iaSerialModbusRTUFixedAddress,
       "iaSerialModbusRTUBroadcastFlag": iaSerialModbusRTUBroadcastFlag,
       "iaSerialModbusRTUErrorResponseFlag": iaSerialModbusRTUErrorResponseFlag,
       "iaSerialModbusRTUExtendedTimeout": iaSerialModbusRTUExtendedTimeout,
       "iaSerialModbusRTUExtendedFunctions": iaSerialModbusRTUExtendedFunctions,
       "iaSerialModbusRTUAddExtendedFunctions": iaSerialModbusRTUAddExtendedFunctions,
       "iaSerialModbusRTURemoveExtendedFunctions": iaSerialModbusRTURemoveExtendedFunctions,
       "iaSerialDF1FullDuplexSettingsTable": iaSerialDF1FullDuplexSettingsTable,
       "iaSerialDF1FullDuplexSettingsEntry": iaSerialDF1FullDuplexSettingsEntry,
       "iaSerialPortDF1FullDuplexIndex": iaSerialPortDF1FullDuplexIndex,
       "iaSerialDF1FullDuplexChecksum": iaSerialDF1FullDuplexChecksum,
       "iaSerialDF1FullDuplexAckTimeout": iaSerialDF1FullDuplexAckTimeout,
       "iaSerialDF1FullDuplexAckTimeoutLimit": iaSerialDF1FullDuplexAckTimeoutLimit,
       "iaSerialDF1FullDuplexNakTimeoutLimit": iaSerialDF1FullDuplexNakTimeoutLimit,
       "iaSerialDF1FullDuplexErrorResponseFlag": iaSerialDF1FullDuplexErrorResponseFlag,
       "iaSerialDF1FullDuplexDuplicateDetectFlag": iaSerialDF1FullDuplexDuplicateDetectFlag,
       "iaSerialDF1HalfDuplexSettingsTable": iaSerialDF1HalfDuplexSettingsTable,
       "iaSerialDF1HalfDuplexSettingsEntry": iaSerialDF1HalfDuplexSettingsEntry,
       "iaSerialPortDF1HalfDuplexIndex": iaSerialPortDF1HalfDuplexIndex,
       "iaSerialDF1HalfDuplexChecksum": iaSerialDF1HalfDuplexChecksum,
       "iaSerialDF1HalfDuplexAckTimeout": iaSerialDF1HalfDuplexAckTimeout,
       "iaSerialDF1HalfDuplexAckTimeoutLimit": iaSerialDF1HalfDuplexAckTimeoutLimit,
       "iaSerialDF1HalfDuplexPollTimeout": iaSerialDF1HalfDuplexPollTimeout,
       "iaSerialDF1HalfDuplexPollTimeoutLimit": iaSerialDF1HalfDuplexPollTimeoutLimit,
       "iaSerialDF1HalfDuplexErrorResponseFlag": iaSerialDF1HalfDuplexErrorResponseFlag,
       "iaSerialDF1HalfDuplexDuplicateDetectFlag": iaSerialDF1HalfDuplexDuplicateDetectFlag,
       "iaSerialUserDefinedSettingsTable": iaSerialUserDefinedSettingsTable,
       "iaSerialUserDefinedSettingsEntry": iaSerialUserDefinedSettingsEntry,
       "iaSerialPortUserDefinedIndex": iaSerialPortUserDefinedIndex,
       "iaSerialUserDefinedStart": iaSerialUserDefinedStart,
       "iaSerialUserDefinedEnd": iaSerialUserDefinedEnd,
       "iaSerialUserDefinedAnsiEscapeFlag": iaSerialUserDefinedAnsiEscapeFlag,
       "iaSerialOmronHostLinkSettingsTable": iaSerialOmronHostLinkSettingsTable,
       "iaSerialOmronHostLinkSettingsEntry": iaSerialOmronHostLinkSettingsEntry,
       "iaSerialPortOmronHostLinkIndex": iaSerialPortOmronHostLinkIndex,
       "iaSerialOmronHostLinkAckTimeout": iaSerialOmronHostLinkAckTimeout,
       "iaSerialOmronHostLinkAckTimeoutLimit": iaSerialOmronHostLinkAckTimeoutLimit,
       "iaSerialOmronFinsSettingsTable": iaSerialOmronFinsSettingsTable,
       "iaSerialOmronFinsSettingsEntry": iaSerialOmronFinsSettingsEntry,
       "iaSerialPortOmronFinsIndex": iaSerialPortOmronFinsIndex,
       "iaSerialOmronFinsAckTimeout": iaSerialOmronFinsAckTimeout,
       "iaSerialOmronFinsAckTimeoutLimit": iaSerialOmronFinsAckTimeoutLimit,
       "iaSerialModbusAsciiSettingsTable": iaSerialModbusAsciiSettingsTable,
       "iaSerialModbusAsciiSettingsEntry": iaSerialModbusAsciiSettingsEntry,
       "iaSerialPortModbusAsciiIndex": iaSerialPortModbusAsciiIndex,
       "iaSerialModbusAsciiFixedAddress": iaSerialModbusAsciiFixedAddress,
       "iaSerialModbusAsciiBroadcastFlag": iaSerialModbusAsciiBroadcastFlag,
       "iaSerialModbusAsciiErrorResponseFlag": iaSerialModbusAsciiErrorResponseFlag,
       "iaSerialModbusAsciiExtendedTimeout": iaSerialModbusAsciiExtendedTimeout,
       "iaSerialModbusAsciiExtendedFunctions": iaSerialModbusAsciiExtendedFunctions,
       "iaSerialModbusAsciiAddExtendedFunctions": iaSerialModbusAsciiAddExtendedFunctions,
       "iaSerialModbusAsciiRemoveExtendedFunctions": iaSerialModbusAsciiRemoveExtendedFunctions,
       "iaNetMasterSettings": iaNetMasterSettings,
       "iaNetMasterGeneralSettingsTable": iaNetMasterGeneralSettingsTable,
       "iaNetMasterGeneralSettingsEntry": iaNetMasterGeneralSettingsEntry,
       "iaNetMasterIndex": iaNetMasterIndex,
       "iaNetMasterProtocol": iaNetMasterProtocol,
       "iaNetMasterModbusTCPSettings": iaNetMasterModbusTCPSettings,
       "iaNetMasterModbusTCPMessageTimeout": iaNetMasterModbusTCPMessageTimeout,
       "iaNetMasterModbusTCPConnectTimeout": iaNetMasterModbusTCPConnectTimeout,
       "iaNetMasterModbusTCPActiveFlag": iaNetMasterModbusTCPActiveFlag,
       "iaNetMasterModbusTCPBroadcastFlag": iaNetMasterModbusTCPBroadcastFlag,
       "iaNetMasterModbusTCPErrorResponseFlag": iaNetMasterModbusTCPErrorResponseFlag,
       "iaNetMasterModbusTCPExtendedTimeout": iaNetMasterModbusTCPExtendedTimeout,
       "iaNetMasterModbusTCPExtendedFunctions": iaNetMasterModbusTCPExtendedFunctions,
       "iaNetMasterModbusTCPAddExtendedFunctions": iaNetMasterModbusTCPAddExtendedFunctions,
       "iaNetMasterModbusTCPRemoveExtendedFunctions": iaNetMasterModbusTCPRemoveExtendedFunctions,
       "iaNetMasterABEthernetSettings": iaNetMasterABEthernetSettings,
       "iaNetMasterABEthernetMessageTimeout": iaNetMasterABEthernetMessageTimeout,
       "iaNetMasterABEthernetConnectTimeout": iaNetMasterABEthernetConnectTimeout,
       "iaNetMasterABEthernetActiveFlag": iaNetMasterABEthernetActiveFlag,
       "iaNetMasterABEthernetErrorResponseFlag": iaNetMasterABEthernetErrorResponseFlag,
       "iaNetMasterEthernetIPSettings": iaNetMasterEthernetIPSettings,
       "iaNetMasterEthernetIPMessageTimeout": iaNetMasterEthernetIPMessageTimeout,
       "iaNetMasterEthernetIPActiveFlag": iaNetMasterEthernetIPActiveFlag,
       "iaNetSlaveSettings": iaNetSlaveSettings,
       "iaNetSlaveGeneralSettingsTable": iaNetSlaveGeneralSettingsTable,
       "iaNetSlaveGeneralSettingsEntry": iaNetSlaveGeneralSettingsEntry,
       "iaNetSlaveIndex": iaNetSlaveIndex,
       "iaNetSlaveProtocol": iaNetSlaveProtocol,
       "iaNetSlaveIpAddress": iaNetSlaveIpAddress,
       "iaNetSlaveIpPort": iaNetSlaveIpPort,
       "iaNetSlaveReconnectTime": iaNetSlaveReconnectTime,
       "iaNetSlaveName": iaNetSlaveName,
       "iaNetSlaveActivateNextFree": iaNetSlaveActivateNextFree,
       "iaStatistics": iaStatistics,
       "iaStatisticsClear": iaStatisticsClear,
       "iaStatisticsModbus": iaStatisticsModbus,
       "modbusResourceErrors": modbusResourceErrors,
       "modbusConfigurationErrors": modbusConfigurationErrors,
       "modbusBadRequestMessageErrors": modbusBadRequestMessageErrors,
       "modbusBadResponseMessageErrors": modbusBadResponseMessageErrors,
       "modbusRequestMessageDroppedErrors": modbusRequestMessageDroppedErrors,
       "modbusResponseMessageDroppedErrors": modbusResponseMessageDroppedErrors,
       "modbusMessageTimeoutErrors": modbusMessageTimeoutErrors,
       "modbusChecksumErrors": modbusChecksumErrors,
       "modbusValidRequests": modbusValidRequests,
       "modbusValidResponses": modbusValidResponses,
       "modbusNetworkHangups": modbusNetworkHangups,
       "modbusActiveMasterConnections": modbusActiveMasterConnections,
       "modbusActiveSlaveConnections": modbusActiveSlaveConnections,
       "iaStatisticsDF1FullDuplex": iaStatisticsDF1FullDuplex,
       "df1FullDuplexResourceErrors": df1FullDuplexResourceErrors,
       "df1FullDuplexConfigurationErrors": df1FullDuplexConfigurationErrors,
       "df1FullDuplexBadRequestMessageErrors": df1FullDuplexBadRequestMessageErrors,
       "df1FullDuplexBadResponseMessageErrors": df1FullDuplexBadResponseMessageErrors,
       "df1FullDuplexRequestMessageDroppedErrors": df1FullDuplexRequestMessageDroppedErrors,
       "df1FullDuplexResponseMessageDroppedErrors": df1FullDuplexResponseMessageDroppedErrors,
       "df1FullDuplexMessageTimeoutErrors": df1FullDuplexMessageTimeoutErrors,
       "df1FullDuplexChecksumErrors": df1FullDuplexChecksumErrors,
       "df1FullDuplexValidRequests": df1FullDuplexValidRequests,
       "df1FullDuplexValidResponses": df1FullDuplexValidResponses,
       "df1FullDuplexNetworkHangups": df1FullDuplexNetworkHangups,
       "df1FullDuplexActiveMasterConnections": df1FullDuplexActiveMasterConnections,
       "df1FullDuplexActiveSlaveConnections": df1FullDuplexActiveSlaveConnections,
       "iaStatisticsOmronHostLink": iaStatisticsOmronHostLink,
       "omronHostLinkResourceErrors": omronHostLinkResourceErrors,
       "omronHostLinkConfigurationErrors": omronHostLinkConfigurationErrors,
       "omronHostLinkBadRequestMessageErrors": omronHostLinkBadRequestMessageErrors,
       "omronHostLinkBadResponseMessageErrors": omronHostLinkBadResponseMessageErrors,
       "omronHostLinkRequestMessageDroppedErrors": omronHostLinkRequestMessageDroppedErrors,
       "omronHostLinkResponseMessageDroppedErrors": omronHostLinkResponseMessageDroppedErrors,
       "omronHostLinkMessageTimeoutErrors": omronHostLinkMessageTimeoutErrors,
       "omronHostLinkChecksumErrors": omronHostLinkChecksumErrors,
       "omronHostLinkValidRequests": omronHostLinkValidRequests,
       "omronHostLinkValidResponses": omronHostLinkValidResponses,
       "omronHostLinkNetworkHangups": omronHostLinkNetworkHangups,
       "omronHostLinkActiveMasterConnections": omronHostLinkActiveMasterConnections,
       "omronHostLinkActiveSlaveConnections": omronHostLinkActiveSlaveConnections,
       "iaStatisticsOmronFins": iaStatisticsOmronFins,
       "omronFinsResourceErrors": omronFinsResourceErrors,
       "omronFinsConfigurationErrors": omronFinsConfigurationErrors,
       "omronFinsBadRequestMessageErrors": omronFinsBadRequestMessageErrors,
       "omronFinsBadResponseMessageErrors": omronFinsBadResponseMessageErrors,
       "omronFinsRequestMessageDroppedErrors": omronFinsRequestMessageDroppedErrors,
       "omronFinsResponseMessageDroppedErrors": omronFinsResponseMessageDroppedErrors,
       "omronFinsMessageTimeoutErrors": omronFinsMessageTimeoutErrors,
       "omronFinsChecksumErrors": omronFinsChecksumErrors,
       "omronFinsValidRequests": omronFinsValidRequests,
       "omronFinsValidResponses": omronFinsValidResponses,
       "omronFinsNetworkHangups": omronFinsNetworkHangups,
       "omronFinsActiveMasterConnections": omronFinsActiveMasterConnections,
       "omronFinsActiveSlaveConnections": omronFinsActiveSlaveConnections,
       "iaStatisticsOmronCompowayf": iaStatisticsOmronCompowayf,
       "omronCompowayfResourceErrors": omronCompowayfResourceErrors,
       "omronCompowayfConfigurationErrors": omronCompowayfConfigurationErrors,
       "omronCompowayfBadRequestMessageErrors": omronCompowayfBadRequestMessageErrors,
       "omronCompowayfBadResponseMessageErrors": omronCompowayfBadResponseMessageErrors,
       "omronCompowayfRequestMessageDroppedErrors": omronCompowayfRequestMessageDroppedErrors,
       "omronCompowayfResponseMessageDroppedErrors": omronCompowayfResponseMessageDroppedErrors,
       "omronCompowayfMessageTimeoutErrors": omronCompowayfMessageTimeoutErrors,
       "omronCompowayfChecksumErrors": omronCompowayfChecksumErrors,
       "omronCompowayfValidRequests": omronCompowayfValidRequests,
       "omronCompowayfValidResponses": omronCompowayfValidResponses,
       "omronCompowayfNetworkHangups": omronCompowayfNetworkHangups,
       "omronCompowayfActiveMasterConnections": omronCompowayfActiveMasterConnections,
       "omronCompowayfActiveSlaveConnections": omronCompowayfActiveSlaveConnections,
       "iaStatisticsUserDefined": iaStatisticsUserDefined,
       "userDefinedResourceErrors": userDefinedResourceErrors,
       "userDefinedConfigurationErrors": userDefinedConfigurationErrors,
       "userDefinedBadRequestMessageErrors": userDefinedBadRequestMessageErrors,
       "userDefinedBadResponseMessageErrors": userDefinedBadResponseMessageErrors,
       "userDefinedRequestMessageDroppedErrors": userDefinedRequestMessageDroppedErrors,
       "userDefinedResponseMessageDroppedErrors": userDefinedResponseMessageDroppedErrors,
       "userDefinedMessageTimeoutErrors": userDefinedMessageTimeoutErrors,
       "userDefinedChecksumErrors": userDefinedChecksumErrors,
       "userDefinedValidRequests": userDefinedValidRequests,
       "userDefinedValidResponses": userDefinedValidResponses,
       "userDefinedNetworkHangups": userDefinedNetworkHangups,
       "userDefinedActiveMasterConnections": userDefinedActiveMasterConnections,
       "userDefinedActiveSlaveConnections": userDefinedActiveSlaveConnections,
       "iaStatisticsDF1HalfDuplex": iaStatisticsDF1HalfDuplex,
       "df1HalfDuplexResourceErrors": df1HalfDuplexResourceErrors,
       "df1HalfDuplexConfigurationErrors": df1HalfDuplexConfigurationErrors,
       "df1HalfDuplexBadRequestMessageErrors": df1HalfDuplexBadRequestMessageErrors,
       "df1HalfDuplexBadResponseMessageErrors": df1HalfDuplexBadResponseMessageErrors,
       "df1HalfDuplexRequestMessageDroppedErrors": df1HalfDuplexRequestMessageDroppedErrors,
       "df1HalfDuplexResponseMessageDroppedErrors": df1HalfDuplexResponseMessageDroppedErrors,
       "df1HalfDuplexMessageTimeoutErrors": df1HalfDuplexMessageTimeoutErrors,
       "df1HalfDuplexChecksumErrors": df1HalfDuplexChecksumErrors,
       "df1HalfDuplexValidRequests": df1HalfDuplexValidRequests,
       "df1HalfDuplexValidResponses": df1HalfDuplexValidResponses,
       "df1HalfDuplexNetworkHangups": df1HalfDuplexNetworkHangups,
       "df1HalfDuplexActiveMasterConnections": df1HalfDuplexActiveMasterConnections,
       "df1HalfDuplexActiveSlaveConnections": df1HalfDuplexActiveSlaveConnections,
       "iaRouteSettings": iaRouteSettings,
       "iaRouteGeneralSettingsTable": iaRouteGeneralSettingsTable,
       "iaRouteGeneralSettingsEntry": iaRouteGeneralSettingsEntry,
       "iaRouteIndex": iaRouteIndex,
       "iaRouteDestinationType": iaRouteDestinationType,
       "iaRouteDestinationIndex": iaRouteDestinationIndex,
       "iaRouteTransmitAllMessages": iaRouteTransmitAllMessages,
       "iaRouteTransmitMinRange": iaRouteTransmitMinRange,
       "iaRouteTransmitMaxRange": iaRouteTransmitMaxRange,
       "iaRouteNetSlaveProtocol": iaRouteNetSlaveProtocol,
       "iaRouteNetSlaveIpAddress": iaRouteNetSlaveIpAddress,
       "iaRouteNetSlaveIpPort": iaRouteNetSlaveIpPort,
       "iaRouteNetSlaveReconnectTime": iaRouteNetSlaveReconnectTime,
       "iaRouteDescription": iaRouteDescription,
       "iaRouteRemoveEntry": iaRouteRemoveEntry,
       "iaRouteNetSlaveModbusTCPSettingsTable": iaRouteNetSlaveModbusTCPSettingsTable,
       "iaRouteNetSlaveModbusTCPSettingsEntry": iaRouteNetSlaveModbusTCPSettingsEntry,
       "iaRouteNetSlaveModbusTCPIndex": iaRouteNetSlaveModbusTCPIndex,
       "iaRouteNetSlaveModbusTCPFixedAddress": iaRouteNetSlaveModbusTCPFixedAddress}
)
