# SNMP MIB module (RUIJIE-TRAP-FORMAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-TRAP-FORMAT-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 10:59:06 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ruijieTrapFormatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97)
)
if mibBuilder.loadTexts:
    ruijieTrapFormatMIB.setRevisions(
        ("2011-05-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieTrapFormatMIBObjects_ObjectIdentity = ObjectIdentity
ruijieTrapFormatMIBObjects = _RuijieTrapFormatMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1)
)


class _RuijieTrapFormatTrapSerialNo_Type(DisplayString):
    """Custom type ruijieTrapFormatTrapSerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieTrapFormatTrapSerialNo_Type.__name__ = "DisplayString"
_RuijieTrapFormatTrapSerialNo_Object = MibScalar
ruijieTrapFormatTrapSerialNo = _RuijieTrapFormatTrapSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 1),
    _RuijieTrapFormatTrapSerialNo_Type()
)
ruijieTrapFormatTrapSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapSerialNo.setStatus("current")


class _RuijieTrapFormatTrapLevel_Type(DisplayString):
    """Custom type ruijieTrapFormatTrapLevel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieTrapFormatTrapLevel_Type.__name__ = "DisplayString"
_RuijieTrapFormatTrapLevel_Object = MibScalar
ruijieTrapFormatTrapLevel = _RuijieTrapFormatTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 2),
    _RuijieTrapFormatTrapLevel_Type()
)
ruijieTrapFormatTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapLevel.setStatus("current")


class _RuijieTrapFormatTrapType_Type(DisplayString):
    """Custom type ruijieTrapFormatTrapType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuijieTrapFormatTrapType_Type.__name__ = "DisplayString"
_RuijieTrapFormatTrapType_Object = MibScalar
ruijieTrapFormatTrapType = _RuijieTrapFormatTrapType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 3),
    _RuijieTrapFormatTrapType_Type()
)
ruijieTrapFormatTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapType.setStatus("current")
_RuijieTrapFormatTrapReasonNo_Type = Integer32
_RuijieTrapFormatTrapReasonNo_Object = MibScalar
ruijieTrapFormatTrapReasonNo = _RuijieTrapFormatTrapReasonNo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 4),
    _RuijieTrapFormatTrapReasonNo_Type()
)
ruijieTrapFormatTrapReasonNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapReasonNo.setStatus("current")


class _RuijieTrapFormatTrapReasons_Type(DisplayString):
    """Custom type ruijieTrapFormatTrapReasons based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieTrapFormatTrapReasons_Type.__name__ = "DisplayString"
_RuijieTrapFormatTrapReasons_Object = MibScalar
ruijieTrapFormatTrapReasons = _RuijieTrapFormatTrapReasons_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 5),
    _RuijieTrapFormatTrapReasons_Type()
)
ruijieTrapFormatTrapReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapReasons.setStatus("current")
_RuijieTrapFormatTrapStatus_Type = Integer32
_RuijieTrapFormatTrapStatus_Object = MibScalar
ruijieTrapFormatTrapStatus = _RuijieTrapFormatTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 6),
    _RuijieTrapFormatTrapStatus_Type()
)
ruijieTrapFormatTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapStatus.setStatus("current")


class _RuijieTrapFormatTrapTitle_Type(DisplayString):
    """Custom type ruijieTrapFormatTrapTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieTrapFormatTrapTitle_Type.__name__ = "DisplayString"
_RuijieTrapFormatTrapTitle_Object = MibScalar
ruijieTrapFormatTrapTitle = _RuijieTrapFormatTrapTitle_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 7),
    _RuijieTrapFormatTrapTitle_Type()
)
ruijieTrapFormatTrapTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapTitle.setStatus("current")


class _RuijieTrapFormatTrapContent_Type(DisplayString):
    """Custom type ruijieTrapFormatTrapContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieTrapFormatTrapContent_Type.__name__ = "DisplayString"
_RuijieTrapFormatTrapContent_Object = MibScalar
ruijieTrapFormatTrapContent = _RuijieTrapFormatTrapContent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 8),
    _RuijieTrapFormatTrapContent_Type()
)
ruijieTrapFormatTrapContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapContent.setStatus("current")
_RuijieTrapFormatTrapTime_Type = Counter32
_RuijieTrapFormatTrapTime_Object = MibScalar
ruijieTrapFormatTrapTime = _RuijieTrapFormatTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 9),
    _RuijieTrapFormatTrapTime_Type()
)
ruijieTrapFormatTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapTime.setStatus("current")
_RuijieTrapFormatTrapSlotInfo_Type = DisplayString
_RuijieTrapFormatTrapSlotInfo_Object = MibScalar
ruijieTrapFormatTrapSlotInfo = _RuijieTrapFormatTrapSlotInfo_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 10),
    _RuijieTrapFormatTrapSlotInfo_Type()
)
ruijieTrapFormatTrapSlotInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapSlotInfo.setStatus("current")
_RuijieTrapFormatTrapVendorId_Type = Integer32
_RuijieTrapFormatTrapVendorId_Object = MibScalar
ruijieTrapFormatTrapVendorId = _RuijieTrapFormatTrapVendorId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 11),
    _RuijieTrapFormatTrapVendorId_Type()
)
ruijieTrapFormatTrapVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapVendorId.setStatus("current")


class _RuijieTrapFormatTrapSerialNum_Type(DisplayString):
    """Custom type ruijieTrapFormatTrapSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieTrapFormatTrapSerialNum_Type.__name__ = "DisplayString"
_RuijieTrapFormatTrapSerialNum_Object = MibScalar
ruijieTrapFormatTrapSerialNum = _RuijieTrapFormatTrapSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 12),
    _RuijieTrapFormatTrapSerialNum_Type()
)
ruijieTrapFormatTrapSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapSerialNum.setStatus("current")


class _RuijieTrapFormatTrapDateTime_Type(DisplayString):
    """Custom type ruijieTrapFormatTrapDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuijieTrapFormatTrapDateTime_Type.__name__ = "DisplayString"
_RuijieTrapFormatTrapDateTime_Object = MibScalar
ruijieTrapFormatTrapDateTime = _RuijieTrapFormatTrapDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 1, 13),
    _RuijieTrapFormatTrapDateTime_Type()
)
ruijieTrapFormatTrapDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieTrapFormatTrapDateTime.setStatus("current")
_RuijieTrapFormatMIBConformance_ObjectIdentity = ObjectIdentity
ruijieTrapFormatMIBConformance = _RuijieTrapFormatMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 2)
)
_RuijieTrapFormatMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieTrapFormatMIBCompliances = _RuijieTrapFormatMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 2, 1)
)
_RuijieTrapFormatMIBGroups_ObjectIdentity = ObjectIdentity
ruijieTrapFormatMIBGroups = _RuijieTrapFormatMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 2, 2)
)

# Managed Objects groups

ruijieTrapFormatMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 2, 2, 1)
)
ruijieTrapFormatMIBGroup.setObjects(
      *(("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapSerialNo"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapLevel"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapType"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapReasonNo"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapReasons"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapStatus"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapTitle"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapContent"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapTime"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapSlotInfo"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapVendorId"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapSerialNum"),
        ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatTrapDateTime"))
)
if mibBuilder.loadTexts:
    ruijieTrapFormatMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ruijieTrapFormatMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 97, 2, 1, 1)
)
ruijieTrapFormatMIBCompliance.setObjects(
    ("RUIJIE-TRAP-FORMAT-MIB", "ruijieTrapFormatMIBGroup")
)
if mibBuilder.loadTexts:
    ruijieTrapFormatMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-TRAP-FORMAT-MIB",
    **{"ruijieTrapFormatMIB": ruijieTrapFormatMIB,
       "ruijieTrapFormatMIBObjects": ruijieTrapFormatMIBObjects,
       "ruijieTrapFormatTrapSerialNo": ruijieTrapFormatTrapSerialNo,
       "ruijieTrapFormatTrapLevel": ruijieTrapFormatTrapLevel,
       "ruijieTrapFormatTrapType": ruijieTrapFormatTrapType,
       "ruijieTrapFormatTrapReasonNo": ruijieTrapFormatTrapReasonNo,
       "ruijieTrapFormatTrapReasons": ruijieTrapFormatTrapReasons,
       "ruijieTrapFormatTrapStatus": ruijieTrapFormatTrapStatus,
       "ruijieTrapFormatTrapTitle": ruijieTrapFormatTrapTitle,
       "ruijieTrapFormatTrapContent": ruijieTrapFormatTrapContent,
       "ruijieTrapFormatTrapTime": ruijieTrapFormatTrapTime,
       "ruijieTrapFormatTrapSlotInfo": ruijieTrapFormatTrapSlotInfo,
       "ruijieTrapFormatTrapVendorId": ruijieTrapFormatTrapVendorId,
       "ruijieTrapFormatTrapSerialNum": ruijieTrapFormatTrapSerialNum,
       "ruijieTrapFormatTrapDateTime": ruijieTrapFormatTrapDateTime,
       "ruijieTrapFormatMIBConformance": ruijieTrapFormatMIBConformance,
       "ruijieTrapFormatMIBCompliances": ruijieTrapFormatMIBCompliances,
       "ruijieTrapFormatMIBCompliance": ruijieTrapFormatMIBCompliance,
       "ruijieTrapFormatMIBGroups": ruijieTrapFormatMIBGroups,
       "ruijieTrapFormatMIBGroup": ruijieTrapFormatMIBGroup}
)
