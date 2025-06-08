# SNMP MIB module (RUIJIE-CPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-CPP-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:05:39 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijieCPPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132)
)
if mibBuilder.loadTexts:
    ruijieCPPMIB.setRevisions(
        ("2014-12-19 21:00",
         "2014-12-19 21:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieCPPMIBObjects_ObjectIdentity = ObjectIdentity
ruijieCPPMIBObjects = _RuijieCPPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1)
)
_RuijieCPPTable_Object = MibTable
ruijieCPPTable = _RuijieCPPTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieCPPTable.setStatus("current")
_RuijieCPPEntry_Object = MibTableRow
ruijieCPPEntry = _RuijieCPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1)
)
ruijieCPPEntry.setIndexNames(
    (0, "RUIJIE-CPP-MIB", "cppIndex"),
)
if mibBuilder.loadTexts:
    ruijieCPPEntry.setStatus("current")


class _CppIndex_Type(Integer32):
    """Custom type cppIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppIndex_Type.__name__ = "Integer32"
_CppIndex_Object = MibTableColumn
cppIndex = _CppIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1, 1),
    _CppIndex_Type()
)
cppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppIndex.setStatus("current")


class _CppDeviceId_Type(Integer32):
    """Custom type cppDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppDeviceId_Type.__name__ = "Integer32"
_CppDeviceId_Object = MibTableColumn
cppDeviceId = _CppDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1, 2),
    _CppDeviceId_Type()
)
cppDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppDeviceId.setStatus("current")


class _CppSlotId_Type(Integer32):
    """Custom type cppSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppSlotId_Type.__name__ = "Integer32"
_CppSlotId_Object = MibTableColumn
cppSlotId = _CppSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1, 3),
    _CppSlotId_Type()
)
cppSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppSlotId.setStatus("current")


class _CppCardIndex_Type(DisplayString):
    """Custom type cppCardIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CppCardIndex_Type.__name__ = "DisplayString"
_CppCardIndex_Object = MibTableColumn
cppCardIndex = _CppCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1, 4),
    _CppCardIndex_Type()
)
cppCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppCardIndex.setStatus("current")


class _CppPacketType_Type(DisplayString):
    """Custom type cppPacketType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CppPacketType_Type.__name__ = "DisplayString"
_CppPacketType_Object = MibTableColumn
cppPacketType = _CppPacketType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1, 5),
    _CppPacketType_Type()
)
cppPacketType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppPacketType.setStatus("current")


class _CppTrafficClass_Type(Integer32):
    """Custom type cppTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTrafficClass_Type.__name__ = "Integer32"
_CppTrafficClass_Object = MibTableColumn
cppTrafficClass = _CppTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1, 6),
    _CppTrafficClass_Type()
)
cppTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTrafficClass.setStatus("current")


class _CppBandwidth_Type(Integer32):
    """Custom type cppBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppBandwidth_Type.__name__ = "Integer32"
_CppBandwidth_Object = MibTableColumn
cppBandwidth = _CppBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1, 7),
    _CppBandwidth_Type()
)
cppBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppBandwidth.setStatus("current")


class _CppRate_Type(Integer32):
    """Custom type cppRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppRate_Type.__name__ = "Integer32"
_CppRate_Object = MibTableColumn
cppRate = _CppRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1, 8),
    _CppRate_Type()
)
cppRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppRate.setStatus("current")


class _CppDrop_Type(Integer32):
    """Custom type cppDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppDrop_Type.__name__ = "Integer32"
_CppDrop_Object = MibTableColumn
cppDrop = _CppDrop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1, 9),
    _CppDrop_Type()
)
cppDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppDrop.setStatus("current")


class _CppTotal_Type(Integer32):
    """Custom type cppTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTotal_Type.__name__ = "Integer32"
_CppTotal_Object = MibTableColumn
cppTotal = _CppTotal_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1, 10),
    _CppTotal_Type()
)
cppTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTotal.setStatus("current")


class _CppTotalDrop_Type(Integer32):
    """Custom type cppTotalDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTotalDrop_Type.__name__ = "Integer32"
_CppTotalDrop_Object = MibTableColumn
cppTotalDrop = _CppTotalDrop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 1, 1, 11),
    _CppTotalDrop_Type()
)
cppTotalDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTotalDrop.setStatus("current")
_RuijieCPPTcTable_Object = MibTable
ruijieCPPTcTable = _RuijieCPPTcTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieCPPTcTable.setStatus("current")
_RuijieCPPTcEntry_Object = MibTableRow
ruijieCPPTcEntry = _RuijieCPPTcEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 2, 1)
)
ruijieCPPTcEntry.setIndexNames(
    (0, "RUIJIE-CPP-MIB", "cppTcIndex"),
)
if mibBuilder.loadTexts:
    ruijieCPPTcEntry.setStatus("current")


class _CppTcIndex_Type(Integer32):
    """Custom type cppTcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTcIndex_Type.__name__ = "Integer32"
_CppTcIndex_Object = MibTableColumn
cppTcIndex = _CppTcIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 2, 1, 1),
    _CppTcIndex_Type()
)
cppTcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTcIndex.setStatus("current")


class _CppTcDeviceId_Type(Integer32):
    """Custom type cppTcDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTcDeviceId_Type.__name__ = "Integer32"
_CppTcDeviceId_Object = MibTableColumn
cppTcDeviceId = _CppTcDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 2, 1, 2),
    _CppTcDeviceId_Type()
)
cppTcDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTcDeviceId.setStatus("current")


class _CppTcSlotId_Type(Integer32):
    """Custom type cppTcSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTcSlotId_Type.__name__ = "Integer32"
_CppTcSlotId_Object = MibTableColumn
cppTcSlotId = _CppTcSlotId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 2, 1, 3),
    _CppTcSlotId_Type()
)
cppTcSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTcSlotId.setStatus("current")


class _CppTcTrafficClass_Type(Integer32):
    """Custom type cppTcTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTcTrafficClass_Type.__name__ = "Integer32"
_CppTcTrafficClass_Object = MibTableColumn
cppTcTrafficClass = _CppTcTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 2, 1, 4),
    _CppTcTrafficClass_Type()
)
cppTcTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTcTrafficClass.setStatus("current")


class _CppTcCardIndex_Type(DisplayString):
    """Custom type cppTcCardIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CppTcCardIndex_Type.__name__ = "DisplayString"
_CppTcCardIndex_Object = MibTableColumn
cppTcCardIndex = _CppTcCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 2, 1, 5),
    _CppTcCardIndex_Type()
)
cppTcCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTcCardIndex.setStatus("current")


class _CppTcBandwidth_Type(Integer32):
    """Custom type cppTcBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTcBandwidth_Type.__name__ = "Integer32"
_CppTcBandwidth_Object = MibTableColumn
cppTcBandwidth = _CppTcBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 2, 1, 6),
    _CppTcBandwidth_Type()
)
cppTcBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTcBandwidth.setStatus("current")


class _CppTcRate_Type(Integer32):
    """Custom type cppTcRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTcRate_Type.__name__ = "Integer32"
_CppTcRate_Object = MibTableColumn
cppTcRate = _CppTcRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 2, 1, 7),
    _CppTcRate_Type()
)
cppTcRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTcRate.setStatus("current")


class _CppTcDrop_Type(Integer32):
    """Custom type cppTcDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CppTcDrop_Type.__name__ = "Integer32"
_CppTcDrop_Object = MibTableColumn
cppTcDrop = _CppTcDrop_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 2, 1, 8),
    _CppTcDrop_Type()
)
cppTcDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cppTcDrop.setStatus("current")


class _RuijieCPPMessageContent_Type(OctetString):
    """Custom type ruijieCPPMessageContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RuijieCPPMessageContent_Type.__name__ = "OctetString"
_RuijieCPPMessageContent_Object = MibScalar
ruijieCPPMessageContent = _RuijieCPPMessageContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 3),
    _RuijieCPPMessageContent_Type()
)
ruijieCPPMessageContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieCPPMessageContent.setStatus("current")


class _RuijieCPPMessagePortContent_Type(OctetString):
    """Custom type ruijieCPPMessagePortContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_RuijieCPPMessagePortContent_Type.__name__ = "OctetString"
_RuijieCPPMessagePortContent_Object = MibScalar
ruijieCPPMessagePortContent = _RuijieCPPMessagePortContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 1, 4),
    _RuijieCPPMessagePortContent_Type()
)
ruijieCPPMessagePortContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieCPPMessagePortContent.setStatus("current")
_RuijieCPPMIBNotifications_ObjectIdentity = ObjectIdentity
ruijieCPPMIBNotifications = _RuijieCPPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 2)
)
_RuijieCPPMIBPortNotifications_ObjectIdentity = ObjectIdentity
ruijieCPPMIBPortNotifications = _RuijieCPPMIBPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 3)
)

# Managed Objects groups


# Notification objects

ruijieCPPMessageGenerated = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 2, 1)
)
ruijieCPPMessageGenerated.setObjects(
    ("RUIJIE-CPP-MIB", "ruijieCPPMessageContent")
)
if mibBuilder.loadTexts:
    ruijieCPPMessageGenerated.setStatus(
        "current"
    )

ruijieCPPMessagePort = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 132, 3, 1)
)
ruijieCPPMessagePort.setObjects(
    ("RUIJIE-CPP-MIB", "ruijieCPPMessagePortContent")
)
if mibBuilder.loadTexts:
    ruijieCPPMessagePort.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-CPP-MIB",
    **{"ruijieCPPMIB": ruijieCPPMIB,
       "ruijieCPPMIBObjects": ruijieCPPMIBObjects,
       "ruijieCPPTable": ruijieCPPTable,
       "ruijieCPPEntry": ruijieCPPEntry,
       "cppIndex": cppIndex,
       "cppDeviceId": cppDeviceId,
       "cppSlotId": cppSlotId,
       "cppCardIndex": cppCardIndex,
       "cppPacketType": cppPacketType,
       "cppTrafficClass": cppTrafficClass,
       "cppBandwidth": cppBandwidth,
       "cppRate": cppRate,
       "cppDrop": cppDrop,
       "cppTotal": cppTotal,
       "cppTotalDrop": cppTotalDrop,
       "ruijieCPPTcTable": ruijieCPPTcTable,
       "ruijieCPPTcEntry": ruijieCPPTcEntry,
       "cppTcIndex": cppTcIndex,
       "cppTcDeviceId": cppTcDeviceId,
       "cppTcSlotId": cppTcSlotId,
       "cppTcTrafficClass": cppTcTrafficClass,
       "cppTcCardIndex": cppTcCardIndex,
       "cppTcBandwidth": cppTcBandwidth,
       "cppTcRate": cppTcRate,
       "cppTcDrop": cppTcDrop,
       "ruijieCPPMessageContent": ruijieCPPMessageContent,
       "ruijieCPPMessagePortContent": ruijieCPPMessagePortContent,
       "ruijieCPPMIBNotifications": ruijieCPPMIBNotifications,
       "ruijieCPPMessageGenerated": ruijieCPPMessageGenerated,
       "ruijieCPPMIBPortNotifications": ruijieCPPMIBPortNotifications,
       "ruijieCPPMessagePort": ruijieCPPMessagePort}
)
