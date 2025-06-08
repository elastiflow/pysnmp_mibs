# SNMP MIB module (CALIX-FAULT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/CALIX-FAULT-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:18:56 2025
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

(calixManagement,
 calixModules) = mibBuilder.importSymbols(
    "CALIX-SMI",
    "calixManagement",
    "calixModules")

(AlarmCntIndex,
 AlarmSeverity,
 CondCntIndex,
 CondLocation,
 CondSeverity,
 CondState,
 CondType,
 InterfaceIndex,
 ObjClass,
 ObjectIndex,
 SrvEffect,
 Tl1Aid) = mibBuilder.importSymbols(
    "CALIX-TC",
    "AlarmCntIndex",
    "AlarmSeverity",
    "CondCntIndex",
    "CondLocation",
    "CondSeverity",
    "CondState",
    "CondType",
    "InterfaceIndex",
    "ObjClass",
    "ObjectIndex",
    "SrvEffect",
    "Tl1Aid")

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

(DateAndTime,
 DisplayString,
 NotificationType,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "NotificationType",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

calixFault = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 1, 3)
)
if mibBuilder.loadTexts:
    calixFault.setRevisions(
        ("2002-03-28 00:26",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CalixFaultMIB_ObjectIdentity = ObjectIdentity
calixFaultMIB = _CalixFaultMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2)
)
_CalixAlarm_ObjectIdentity = ObjectIdentity
calixAlarm = _CalixAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1)
)
_CalixEqptAlarmTable_Object = MibTable
calixEqptAlarmTable = _CalixEqptAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    calixEqptAlarmTable.setStatus("current")
_CalixEqptAlarmEntry_Object = MibTableRow
calixEqptAlarmEntry = _CalixEqptAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1)
)
calixEqptAlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixEqptAlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixEqptAlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixEqptAlarmEntry.setStatus("current")
_CalixEqptAlarmObjIndex_Type = ObjectIndex
_CalixEqptAlarmObjIndex_Object = MibTableColumn
calixEqptAlarmObjIndex = _CalixEqptAlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1, 1),
    _CalixEqptAlarmObjIndex_Type()
)
calixEqptAlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptAlarmObjIndex.setStatus("current")
_CalixEqptAlarmCntIndex_Type = AlarmCntIndex
_CalixEqptAlarmCntIndex_Object = MibTableColumn
calixEqptAlarmCntIndex = _CalixEqptAlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1, 2),
    _CalixEqptAlarmCntIndex_Type()
)
calixEqptAlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptAlarmCntIndex.setStatus("current")
_CalixEqptAlarmObjTl1Aid_Type = Tl1Aid
_CalixEqptAlarmObjTl1Aid_Object = MibTableColumn
calixEqptAlarmObjTl1Aid = _CalixEqptAlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1, 3),
    _CalixEqptAlarmObjTl1Aid_Type()
)
calixEqptAlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptAlarmObjTl1Aid.setStatus("current")
_CalixEqptAlarmObjClass_Type = ObjClass
_CalixEqptAlarmObjClass_Object = MibTableColumn
calixEqptAlarmObjClass = _CalixEqptAlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1, 4),
    _CalixEqptAlarmObjClass_Type()
)
calixEqptAlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptAlarmObjClass.setStatus("current")
_CalixEqptAlarmSeverity_Type = AlarmSeverity
_CalixEqptAlarmSeverity_Object = MibTableColumn
calixEqptAlarmSeverity = _CalixEqptAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1, 5),
    _CalixEqptAlarmSeverity_Type()
)
calixEqptAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptAlarmSeverity.setStatus("current")
_CalixEqptAlarmType_Type = CondType
_CalixEqptAlarmType_Object = MibTableColumn
calixEqptAlarmType = _CalixEqptAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1, 6),
    _CalixEqptAlarmType_Type()
)
calixEqptAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptAlarmType.setStatus("current")


class _CalixEqptAlarmDescr_Type(OctetString):
    """Custom type calixEqptAlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixEqptAlarmDescr_Type.__name__ = "OctetString"
_CalixEqptAlarmDescr_Object = MibTableColumn
calixEqptAlarmDescr = _CalixEqptAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1, 7),
    _CalixEqptAlarmDescr_Type()
)
calixEqptAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptAlarmDescr.setStatus("current")
_CalixEqptAlarmSrvEffect_Type = SrvEffect
_CalixEqptAlarmSrvEffect_Object = MibTableColumn
calixEqptAlarmSrvEffect = _CalixEqptAlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1, 8),
    _CalixEqptAlarmSrvEffect_Type()
)
calixEqptAlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptAlarmSrvEffect.setStatus("current")
_CalixEqptAlarmLocation_Type = CondLocation
_CalixEqptAlarmLocation_Object = MibTableColumn
calixEqptAlarmLocation = _CalixEqptAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1, 9),
    _CalixEqptAlarmLocation_Type()
)
calixEqptAlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptAlarmLocation.setStatus("current")
_CalixEqptAlarmDateTime_Type = DateAndTime
_CalixEqptAlarmDateTime_Object = MibTableColumn
calixEqptAlarmDateTime = _CalixEqptAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1, 10),
    _CalixEqptAlarmDateTime_Type()
)
calixEqptAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptAlarmDateTime.setStatus("current")
_CalixEqptAlarmTimeStamp_Type = TimeStamp
_CalixEqptAlarmTimeStamp_Object = MibTableColumn
calixEqptAlarmTimeStamp = _CalixEqptAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 1, 1, 11),
    _CalixEqptAlarmTimeStamp_Type()
)
calixEqptAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptAlarmTimeStamp.setStatus("current")
_CalixAdslAlarmTable_Object = MibTable
calixAdslAlarmTable = _CalixAdslAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    calixAdslAlarmTable.setStatus("current")
_CalixAdslAlarmEntry_Object = MibTableRow
calixAdslAlarmEntry = _CalixAdslAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1)
)
calixAdslAlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixAdslAlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixAdslAlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixAdslAlarmEntry.setStatus("current")
_CalixAdslAlarmObjIndex_Type = ObjectIndex
_CalixAdslAlarmObjIndex_Object = MibTableColumn
calixAdslAlarmObjIndex = _CalixAdslAlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1, 1),
    _CalixAdslAlarmObjIndex_Type()
)
calixAdslAlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslAlarmObjIndex.setStatus("current")
_CalixAdslAlarmCntIndex_Type = AlarmCntIndex
_CalixAdslAlarmCntIndex_Object = MibTableColumn
calixAdslAlarmCntIndex = _CalixAdslAlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1, 2),
    _CalixAdslAlarmCntIndex_Type()
)
calixAdslAlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslAlarmCntIndex.setStatus("current")
_CalixAdslAlarmObjTl1Aid_Type = Tl1Aid
_CalixAdslAlarmObjTl1Aid_Object = MibTableColumn
calixAdslAlarmObjTl1Aid = _CalixAdslAlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1, 3),
    _CalixAdslAlarmObjTl1Aid_Type()
)
calixAdslAlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslAlarmObjTl1Aid.setStatus("current")
_CalixAdslAlarmObjClass_Type = ObjClass
_CalixAdslAlarmObjClass_Object = MibTableColumn
calixAdslAlarmObjClass = _CalixAdslAlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1, 4),
    _CalixAdslAlarmObjClass_Type()
)
calixAdslAlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslAlarmObjClass.setStatus("current")
_CalixAdslAlarmSeverity_Type = AlarmSeverity
_CalixAdslAlarmSeverity_Object = MibTableColumn
calixAdslAlarmSeverity = _CalixAdslAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1, 5),
    _CalixAdslAlarmSeverity_Type()
)
calixAdslAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslAlarmSeverity.setStatus("current")
_CalixAdslAlarmType_Type = CondType
_CalixAdslAlarmType_Object = MibTableColumn
calixAdslAlarmType = _CalixAdslAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1, 6),
    _CalixAdslAlarmType_Type()
)
calixAdslAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslAlarmType.setStatus("current")


class _CalixAdslAlarmDescr_Type(OctetString):
    """Custom type calixAdslAlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixAdslAlarmDescr_Type.__name__ = "OctetString"
_CalixAdslAlarmDescr_Object = MibTableColumn
calixAdslAlarmDescr = _CalixAdslAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1, 7),
    _CalixAdslAlarmDescr_Type()
)
calixAdslAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslAlarmDescr.setStatus("current")
_CalixAdslAlarmSrvEffect_Type = SrvEffect
_CalixAdslAlarmSrvEffect_Object = MibTableColumn
calixAdslAlarmSrvEffect = _CalixAdslAlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1, 8),
    _CalixAdslAlarmSrvEffect_Type()
)
calixAdslAlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslAlarmSrvEffect.setStatus("current")
_CalixAdslAlarmLocation_Type = CondLocation
_CalixAdslAlarmLocation_Object = MibTableColumn
calixAdslAlarmLocation = _CalixAdslAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1, 9),
    _CalixAdslAlarmLocation_Type()
)
calixAdslAlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslAlarmLocation.setStatus("current")
_CalixAdslAlarmDateTime_Type = DateAndTime
_CalixAdslAlarmDateTime_Object = MibTableColumn
calixAdslAlarmDateTime = _CalixAdslAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1, 10),
    _CalixAdslAlarmDateTime_Type()
)
calixAdslAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslAlarmDateTime.setStatus("current")
_CalixAdslAlarmTimeStamp_Type = TimeStamp
_CalixAdslAlarmTimeStamp_Object = MibTableColumn
calixAdslAlarmTimeStamp = _CalixAdslAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 2, 1, 11),
    _CalixAdslAlarmTimeStamp_Type()
)
calixAdslAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslAlarmTimeStamp.setStatus("current")
_CalixDs0AlarmTable_Object = MibTable
calixDs0AlarmTable = _CalixDs0AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    calixDs0AlarmTable.setStatus("current")
_CalixDs0AlarmEntry_Object = MibTableRow
calixDs0AlarmEntry = _CalixDs0AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1)
)
calixDs0AlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixDs0AlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixDs0AlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixDs0AlarmEntry.setStatus("current")
_CalixDs0AlarmObjIndex_Type = ObjectIndex
_CalixDs0AlarmObjIndex_Object = MibTableColumn
calixDs0AlarmObjIndex = _CalixDs0AlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1, 1),
    _CalixDs0AlarmObjIndex_Type()
)
calixDs0AlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0AlarmObjIndex.setStatus("current")
_CalixDs0AlarmCntIndex_Type = AlarmCntIndex
_CalixDs0AlarmCntIndex_Object = MibTableColumn
calixDs0AlarmCntIndex = _CalixDs0AlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1, 2),
    _CalixDs0AlarmCntIndex_Type()
)
calixDs0AlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0AlarmCntIndex.setStatus("current")
_CalixDs0AlarmObjTl1Aid_Type = Tl1Aid
_CalixDs0AlarmObjTl1Aid_Object = MibTableColumn
calixDs0AlarmObjTl1Aid = _CalixDs0AlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1, 3),
    _CalixDs0AlarmObjTl1Aid_Type()
)
calixDs0AlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0AlarmObjTl1Aid.setStatus("current")
_CalixDs0AlarmObjClass_Type = ObjClass
_CalixDs0AlarmObjClass_Object = MibTableColumn
calixDs0AlarmObjClass = _CalixDs0AlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1, 4),
    _CalixDs0AlarmObjClass_Type()
)
calixDs0AlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0AlarmObjClass.setStatus("current")
_CalixDs0AlarmSeverity_Type = AlarmSeverity
_CalixDs0AlarmSeverity_Object = MibTableColumn
calixDs0AlarmSeverity = _CalixDs0AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1, 5),
    _CalixDs0AlarmSeverity_Type()
)
calixDs0AlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0AlarmSeverity.setStatus("current")
_CalixDs0AlarmType_Type = CondType
_CalixDs0AlarmType_Object = MibTableColumn
calixDs0AlarmType = _CalixDs0AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1, 6),
    _CalixDs0AlarmType_Type()
)
calixDs0AlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0AlarmType.setStatus("current")


class _CalixDs0AlarmDescr_Type(OctetString):
    """Custom type calixDs0AlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixDs0AlarmDescr_Type.__name__ = "OctetString"
_CalixDs0AlarmDescr_Object = MibTableColumn
calixDs0AlarmDescr = _CalixDs0AlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1, 7),
    _CalixDs0AlarmDescr_Type()
)
calixDs0AlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0AlarmDescr.setStatus("current")
_CalixDs0AlarmSrvEffect_Type = SrvEffect
_CalixDs0AlarmSrvEffect_Object = MibTableColumn
calixDs0AlarmSrvEffect = _CalixDs0AlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1, 8),
    _CalixDs0AlarmSrvEffect_Type()
)
calixDs0AlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0AlarmSrvEffect.setStatus("current")
_CalixDs0AlarmLocation_Type = CondLocation
_CalixDs0AlarmLocation_Object = MibTableColumn
calixDs0AlarmLocation = _CalixDs0AlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1, 9),
    _CalixDs0AlarmLocation_Type()
)
calixDs0AlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0AlarmLocation.setStatus("current")
_CalixDs0AlarmDateTime_Type = DateAndTime
_CalixDs0AlarmDateTime_Object = MibTableColumn
calixDs0AlarmDateTime = _CalixDs0AlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1, 10),
    _CalixDs0AlarmDateTime_Type()
)
calixDs0AlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0AlarmDateTime.setStatus("current")
_CalixDs0AlarmTimeStamp_Type = TimeStamp
_CalixDs0AlarmTimeStamp_Object = MibTableColumn
calixDs0AlarmTimeStamp = _CalixDs0AlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 3, 1, 11),
    _CalixDs0AlarmTimeStamp_Type()
)
calixDs0AlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0AlarmTimeStamp.setStatus("current")
_CalixDs1AlarmTable_Object = MibTable
calixDs1AlarmTable = _CalixDs1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    calixDs1AlarmTable.setStatus("current")
_CalixDs1AlarmEntry_Object = MibTableRow
calixDs1AlarmEntry = _CalixDs1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1)
)
calixDs1AlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixDs1AlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixDs1AlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixDs1AlarmEntry.setStatus("current")
_CalixDs1AlarmObjIndex_Type = ObjectIndex
_CalixDs1AlarmObjIndex_Object = MibTableColumn
calixDs1AlarmObjIndex = _CalixDs1AlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1, 1),
    _CalixDs1AlarmObjIndex_Type()
)
calixDs1AlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1AlarmObjIndex.setStatus("current")
_CalixDs1AlarmCntIndex_Type = AlarmCntIndex
_CalixDs1AlarmCntIndex_Object = MibTableColumn
calixDs1AlarmCntIndex = _CalixDs1AlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1, 2),
    _CalixDs1AlarmCntIndex_Type()
)
calixDs1AlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1AlarmCntIndex.setStatus("current")
_CalixDs1AlarmObjTl1Aid_Type = Tl1Aid
_CalixDs1AlarmObjTl1Aid_Object = MibTableColumn
calixDs1AlarmObjTl1Aid = _CalixDs1AlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1, 3),
    _CalixDs1AlarmObjTl1Aid_Type()
)
calixDs1AlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1AlarmObjTl1Aid.setStatus("current")
_CalixDs1AlarmObjClass_Type = ObjClass
_CalixDs1AlarmObjClass_Object = MibTableColumn
calixDs1AlarmObjClass = _CalixDs1AlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1, 4),
    _CalixDs1AlarmObjClass_Type()
)
calixDs1AlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1AlarmObjClass.setStatus("current")
_CalixDs1AlarmSeverity_Type = AlarmSeverity
_CalixDs1AlarmSeverity_Object = MibTableColumn
calixDs1AlarmSeverity = _CalixDs1AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1, 5),
    _CalixDs1AlarmSeverity_Type()
)
calixDs1AlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1AlarmSeverity.setStatus("current")
_CalixDs1AlarmType_Type = CondType
_CalixDs1AlarmType_Object = MibTableColumn
calixDs1AlarmType = _CalixDs1AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1, 6),
    _CalixDs1AlarmType_Type()
)
calixDs1AlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1AlarmType.setStatus("current")


class _CalixDs1AlarmDescr_Type(OctetString):
    """Custom type calixDs1AlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixDs1AlarmDescr_Type.__name__ = "OctetString"
_CalixDs1AlarmDescr_Object = MibTableColumn
calixDs1AlarmDescr = _CalixDs1AlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1, 7),
    _CalixDs1AlarmDescr_Type()
)
calixDs1AlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1AlarmDescr.setStatus("current")
_CalixDs1AlarmSrvEffect_Type = SrvEffect
_CalixDs1AlarmSrvEffect_Object = MibTableColumn
calixDs1AlarmSrvEffect = _CalixDs1AlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1, 8),
    _CalixDs1AlarmSrvEffect_Type()
)
calixDs1AlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1AlarmSrvEffect.setStatus("current")
_CalixDs1AlarmLocation_Type = CondLocation
_CalixDs1AlarmLocation_Object = MibTableColumn
calixDs1AlarmLocation = _CalixDs1AlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1, 9),
    _CalixDs1AlarmLocation_Type()
)
calixDs1AlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1AlarmLocation.setStatus("current")
_CalixDs1AlarmDateTime_Type = DateAndTime
_CalixDs1AlarmDateTime_Object = MibTableColumn
calixDs1AlarmDateTime = _CalixDs1AlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1, 10),
    _CalixDs1AlarmDateTime_Type()
)
calixDs1AlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1AlarmDateTime.setStatus("current")
_CalixDs1AlarmTimeStamp_Type = TimeStamp
_CalixDs1AlarmTimeStamp_Object = MibTableColumn
calixDs1AlarmTimeStamp = _CalixDs1AlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 4, 1, 11),
    _CalixDs1AlarmTimeStamp_Type()
)
calixDs1AlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1AlarmTimeStamp.setStatus("current")
_CalixDs3AlarmTable_Object = MibTable
calixDs3AlarmTable = _CalixDs3AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    calixDs3AlarmTable.setStatus("current")
_CalixDs3AlarmEntry_Object = MibTableRow
calixDs3AlarmEntry = _CalixDs3AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1)
)
calixDs3AlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixDs3AlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixDs3AlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixDs3AlarmEntry.setStatus("current")
_CalixDs3AlarmObjIndex_Type = ObjectIndex
_CalixDs3AlarmObjIndex_Object = MibTableColumn
calixDs3AlarmObjIndex = _CalixDs3AlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1, 1),
    _CalixDs3AlarmObjIndex_Type()
)
calixDs3AlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3AlarmObjIndex.setStatus("current")
_CalixDs3AlarmCntIndex_Type = AlarmCntIndex
_CalixDs3AlarmCntIndex_Object = MibTableColumn
calixDs3AlarmCntIndex = _CalixDs3AlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1, 2),
    _CalixDs3AlarmCntIndex_Type()
)
calixDs3AlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3AlarmCntIndex.setStatus("current")
_CalixDs3AlarmObjTl1Aid_Type = Tl1Aid
_CalixDs3AlarmObjTl1Aid_Object = MibTableColumn
calixDs3AlarmObjTl1Aid = _CalixDs3AlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1, 3),
    _CalixDs3AlarmObjTl1Aid_Type()
)
calixDs3AlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3AlarmObjTl1Aid.setStatus("current")
_CalixDs3AlarmObjClass_Type = ObjClass
_CalixDs3AlarmObjClass_Object = MibTableColumn
calixDs3AlarmObjClass = _CalixDs3AlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1, 4),
    _CalixDs3AlarmObjClass_Type()
)
calixDs3AlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3AlarmObjClass.setStatus("current")
_CalixDs3AlarmSeverity_Type = AlarmSeverity
_CalixDs3AlarmSeverity_Object = MibTableColumn
calixDs3AlarmSeverity = _CalixDs3AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1, 5),
    _CalixDs3AlarmSeverity_Type()
)
calixDs3AlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3AlarmSeverity.setStatus("current")
_CalixDs3AlarmType_Type = CondType
_CalixDs3AlarmType_Object = MibTableColumn
calixDs3AlarmType = _CalixDs3AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1, 6),
    _CalixDs3AlarmType_Type()
)
calixDs3AlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3AlarmType.setStatus("current")


class _CalixDs3AlarmDescr_Type(OctetString):
    """Custom type calixDs3AlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixDs3AlarmDescr_Type.__name__ = "OctetString"
_CalixDs3AlarmDescr_Object = MibTableColumn
calixDs3AlarmDescr = _CalixDs3AlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1, 7),
    _CalixDs3AlarmDescr_Type()
)
calixDs3AlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3AlarmDescr.setStatus("current")
_CalixDs3AlarmSrvEffect_Type = SrvEffect
_CalixDs3AlarmSrvEffect_Object = MibTableColumn
calixDs3AlarmSrvEffect = _CalixDs3AlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1, 8),
    _CalixDs3AlarmSrvEffect_Type()
)
calixDs3AlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3AlarmSrvEffect.setStatus("current")
_CalixDs3AlarmLocation_Type = CondLocation
_CalixDs3AlarmLocation_Object = MibTableColumn
calixDs3AlarmLocation = _CalixDs3AlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1, 9),
    _CalixDs3AlarmLocation_Type()
)
calixDs3AlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3AlarmLocation.setStatus("current")
_CalixDs3AlarmDateTime_Type = DateAndTime
_CalixDs3AlarmDateTime_Object = MibTableColumn
calixDs3AlarmDateTime = _CalixDs3AlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1, 10),
    _CalixDs3AlarmDateTime_Type()
)
calixDs3AlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3AlarmDateTime.setStatus("current")
_CalixDs3AlarmTimeStamp_Type = TimeStamp
_CalixDs3AlarmTimeStamp_Object = MibTableColumn
calixDs3AlarmTimeStamp = _CalixDs3AlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 5, 1, 11),
    _CalixDs3AlarmTimeStamp_Type()
)
calixDs3AlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3AlarmTimeStamp.setStatus("current")
_CalixOcAlarmTable_Object = MibTable
calixOcAlarmTable = _CalixOcAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6)
)
if mibBuilder.loadTexts:
    calixOcAlarmTable.setStatus("current")
_CalixOcAlarmEntry_Object = MibTableRow
calixOcAlarmEntry = _CalixOcAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1)
)
calixOcAlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixOcAlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixOcAlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixOcAlarmEntry.setStatus("current")
_CalixOcAlarmObjIndex_Type = ObjectIndex
_CalixOcAlarmObjIndex_Object = MibTableColumn
calixOcAlarmObjIndex = _CalixOcAlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1, 1),
    _CalixOcAlarmObjIndex_Type()
)
calixOcAlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcAlarmObjIndex.setStatus("current")
_CalixOcAlarmCntIndex_Type = AlarmCntIndex
_CalixOcAlarmCntIndex_Object = MibTableColumn
calixOcAlarmCntIndex = _CalixOcAlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1, 2),
    _CalixOcAlarmCntIndex_Type()
)
calixOcAlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcAlarmCntIndex.setStatus("current")
_CalixOcAlarmObjTl1Aid_Type = Tl1Aid
_CalixOcAlarmObjTl1Aid_Object = MibTableColumn
calixOcAlarmObjTl1Aid = _CalixOcAlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1, 3),
    _CalixOcAlarmObjTl1Aid_Type()
)
calixOcAlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcAlarmObjTl1Aid.setStatus("current")
_CalixOcAlarmObjClass_Type = ObjClass
_CalixOcAlarmObjClass_Object = MibTableColumn
calixOcAlarmObjClass = _CalixOcAlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1, 4),
    _CalixOcAlarmObjClass_Type()
)
calixOcAlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcAlarmObjClass.setStatus("current")
_CalixOcAlarmSeverity_Type = AlarmSeverity
_CalixOcAlarmSeverity_Object = MibTableColumn
calixOcAlarmSeverity = _CalixOcAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1, 5),
    _CalixOcAlarmSeverity_Type()
)
calixOcAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcAlarmSeverity.setStatus("current")
_CalixOcAlarmType_Type = CondType
_CalixOcAlarmType_Object = MibTableColumn
calixOcAlarmType = _CalixOcAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1, 6),
    _CalixOcAlarmType_Type()
)
calixOcAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcAlarmType.setStatus("current")


class _CalixOcAlarmDescr_Type(OctetString):
    """Custom type calixOcAlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixOcAlarmDescr_Type.__name__ = "OctetString"
_CalixOcAlarmDescr_Object = MibTableColumn
calixOcAlarmDescr = _CalixOcAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1, 7),
    _CalixOcAlarmDescr_Type()
)
calixOcAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcAlarmDescr.setStatus("current")
_CalixOcAlarmSrvEffect_Type = SrvEffect
_CalixOcAlarmSrvEffect_Object = MibTableColumn
calixOcAlarmSrvEffect = _CalixOcAlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1, 8),
    _CalixOcAlarmSrvEffect_Type()
)
calixOcAlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcAlarmSrvEffect.setStatus("current")
_CalixOcAlarmLocation_Type = CondLocation
_CalixOcAlarmLocation_Object = MibTableColumn
calixOcAlarmLocation = _CalixOcAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1, 9),
    _CalixOcAlarmLocation_Type()
)
calixOcAlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcAlarmLocation.setStatus("current")
_CalixOcAlarmDateTime_Type = DateAndTime
_CalixOcAlarmDateTime_Object = MibTableColumn
calixOcAlarmDateTime = _CalixOcAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1, 10),
    _CalixOcAlarmDateTime_Type()
)
calixOcAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcAlarmDateTime.setStatus("current")
_CalixOcAlarmTimeStamp_Type = TimeStamp
_CalixOcAlarmTimeStamp_Object = MibTableColumn
calixOcAlarmTimeStamp = _CalixOcAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 6, 1, 11),
    _CalixOcAlarmTimeStamp_Type()
)
calixOcAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcAlarmTimeStamp.setStatus("current")
_CalixStsAlarmTable_Object = MibTable
calixStsAlarmTable = _CalixStsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7)
)
if mibBuilder.loadTexts:
    calixStsAlarmTable.setStatus("current")
_CalixStsAlarmEntry_Object = MibTableRow
calixStsAlarmEntry = _CalixStsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1)
)
calixStsAlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixStsAlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixStsAlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixStsAlarmEntry.setStatus("current")
_CalixStsAlarmObjIndex_Type = ObjectIndex
_CalixStsAlarmObjIndex_Object = MibTableColumn
calixStsAlarmObjIndex = _CalixStsAlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1, 1),
    _CalixStsAlarmObjIndex_Type()
)
calixStsAlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsAlarmObjIndex.setStatus("current")
_CalixStsAlarmCntIndex_Type = AlarmCntIndex
_CalixStsAlarmCntIndex_Object = MibTableColumn
calixStsAlarmCntIndex = _CalixStsAlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1, 2),
    _CalixStsAlarmCntIndex_Type()
)
calixStsAlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsAlarmCntIndex.setStatus("current")
_CalixStsAlarmObjTl1Aid_Type = Tl1Aid
_CalixStsAlarmObjTl1Aid_Object = MibTableColumn
calixStsAlarmObjTl1Aid = _CalixStsAlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1, 3),
    _CalixStsAlarmObjTl1Aid_Type()
)
calixStsAlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsAlarmObjTl1Aid.setStatus("current")
_CalixStsAlarmObjClass_Type = ObjClass
_CalixStsAlarmObjClass_Object = MibTableColumn
calixStsAlarmObjClass = _CalixStsAlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1, 4),
    _CalixStsAlarmObjClass_Type()
)
calixStsAlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsAlarmObjClass.setStatus("current")
_CalixStsAlarmSeverity_Type = AlarmSeverity
_CalixStsAlarmSeverity_Object = MibTableColumn
calixStsAlarmSeverity = _CalixStsAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1, 5),
    _CalixStsAlarmSeverity_Type()
)
calixStsAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsAlarmSeverity.setStatus("current")
_CalixStsAlarmType_Type = CondType
_CalixStsAlarmType_Object = MibTableColumn
calixStsAlarmType = _CalixStsAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1, 6),
    _CalixStsAlarmType_Type()
)
calixStsAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsAlarmType.setStatus("current")


class _CalixStsAlarmDescr_Type(OctetString):
    """Custom type calixStsAlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixStsAlarmDescr_Type.__name__ = "OctetString"
_CalixStsAlarmDescr_Object = MibTableColumn
calixStsAlarmDescr = _CalixStsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1, 7),
    _CalixStsAlarmDescr_Type()
)
calixStsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsAlarmDescr.setStatus("current")
_CalixStsAlarmSrvEffect_Type = SrvEffect
_CalixStsAlarmSrvEffect_Object = MibTableColumn
calixStsAlarmSrvEffect = _CalixStsAlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1, 8),
    _CalixStsAlarmSrvEffect_Type()
)
calixStsAlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsAlarmSrvEffect.setStatus("current")
_CalixStsAlarmLocation_Type = CondLocation
_CalixStsAlarmLocation_Object = MibTableColumn
calixStsAlarmLocation = _CalixStsAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1, 9),
    _CalixStsAlarmLocation_Type()
)
calixStsAlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsAlarmLocation.setStatus("current")
_CalixStsAlarmDateTime_Type = DateAndTime
_CalixStsAlarmDateTime_Object = MibTableColumn
calixStsAlarmDateTime = _CalixStsAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1, 10),
    _CalixStsAlarmDateTime_Type()
)
calixStsAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsAlarmDateTime.setStatus("current")
_CalixStsAlarmTimeStamp_Type = TimeStamp
_CalixStsAlarmTimeStamp_Object = MibTableColumn
calixStsAlarmTimeStamp = _CalixStsAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 7, 1, 11),
    _CalixStsAlarmTimeStamp_Type()
)
calixStsAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsAlarmTimeStamp.setStatus("current")
_CalixEnvAlarmTable_Object = MibTable
calixEnvAlarmTable = _CalixEnvAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8)
)
if mibBuilder.loadTexts:
    calixEnvAlarmTable.setStatus("current")
_CalixEnvAlarmEntry_Object = MibTableRow
calixEnvAlarmEntry = _CalixEnvAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1)
)
calixEnvAlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixEnvAlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixEnvAlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixEnvAlarmEntry.setStatus("current")
_CalixEnvAlarmObjIndex_Type = ObjectIndex
_CalixEnvAlarmObjIndex_Object = MibTableColumn
calixEnvAlarmObjIndex = _CalixEnvAlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1, 1),
    _CalixEnvAlarmObjIndex_Type()
)
calixEnvAlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvAlarmObjIndex.setStatus("current")
_CalixEnvAlarmCntIndex_Type = AlarmCntIndex
_CalixEnvAlarmCntIndex_Object = MibTableColumn
calixEnvAlarmCntIndex = _CalixEnvAlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1, 2),
    _CalixEnvAlarmCntIndex_Type()
)
calixEnvAlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvAlarmCntIndex.setStatus("current")
_CalixEnvAlarmObjTl1Aid_Type = Tl1Aid
_CalixEnvAlarmObjTl1Aid_Object = MibTableColumn
calixEnvAlarmObjTl1Aid = _CalixEnvAlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1, 3),
    _CalixEnvAlarmObjTl1Aid_Type()
)
calixEnvAlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvAlarmObjTl1Aid.setStatus("current")
_CalixEnvAlarmObjClass_Type = ObjClass
_CalixEnvAlarmObjClass_Object = MibTableColumn
calixEnvAlarmObjClass = _CalixEnvAlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1, 4),
    _CalixEnvAlarmObjClass_Type()
)
calixEnvAlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvAlarmObjClass.setStatus("current")
_CalixEnvAlarmSeverity_Type = AlarmSeverity
_CalixEnvAlarmSeverity_Object = MibTableColumn
calixEnvAlarmSeverity = _CalixEnvAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1, 5),
    _CalixEnvAlarmSeverity_Type()
)
calixEnvAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvAlarmSeverity.setStatus("current")
_CalixEnvAlarmType_Type = CondType
_CalixEnvAlarmType_Object = MibTableColumn
calixEnvAlarmType = _CalixEnvAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1, 6),
    _CalixEnvAlarmType_Type()
)
calixEnvAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvAlarmType.setStatus("current")


class _CalixEnvAlarmDescr_Type(OctetString):
    """Custom type calixEnvAlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixEnvAlarmDescr_Type.__name__ = "OctetString"
_CalixEnvAlarmDescr_Object = MibTableColumn
calixEnvAlarmDescr = _CalixEnvAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1, 7),
    _CalixEnvAlarmDescr_Type()
)
calixEnvAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvAlarmDescr.setStatus("current")
_CalixEnvAlarmSrvEffect_Type = SrvEffect
_CalixEnvAlarmSrvEffect_Object = MibTableColumn
calixEnvAlarmSrvEffect = _CalixEnvAlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1, 8),
    _CalixEnvAlarmSrvEffect_Type()
)
calixEnvAlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvAlarmSrvEffect.setStatus("current")
_CalixEnvAlarmLocation_Type = CondLocation
_CalixEnvAlarmLocation_Object = MibTableColumn
calixEnvAlarmLocation = _CalixEnvAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1, 9),
    _CalixEnvAlarmLocation_Type()
)
calixEnvAlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvAlarmLocation.setStatus("current")
_CalixEnvAlarmDateTime_Type = DateAndTime
_CalixEnvAlarmDateTime_Object = MibTableColumn
calixEnvAlarmDateTime = _CalixEnvAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1, 10),
    _CalixEnvAlarmDateTime_Type()
)
calixEnvAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvAlarmDateTime.setStatus("current")
_CalixEnvAlarmTimeStamp_Type = TimeStamp
_CalixEnvAlarmTimeStamp_Object = MibTableColumn
calixEnvAlarmTimeStamp = _CalixEnvAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 8, 1, 11),
    _CalixEnvAlarmTimeStamp_Type()
)
calixEnvAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvAlarmTimeStamp.setStatus("current")
_CalixImaGroupAlarmTable_Object = MibTable
calixImaGroupAlarmTable = _CalixImaGroupAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9)
)
if mibBuilder.loadTexts:
    calixImaGroupAlarmTable.setStatus("current")
_CalixImaGroupAlarmEntry_Object = MibTableRow
calixImaGroupAlarmEntry = _CalixImaGroupAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1)
)
calixImaGroupAlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixImaGroupAlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixImaGroupAlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixImaGroupAlarmEntry.setStatus("current")
_CalixImaGroupAlarmObjIndex_Type = ObjectIndex
_CalixImaGroupAlarmObjIndex_Object = MibTableColumn
calixImaGroupAlarmObjIndex = _CalixImaGroupAlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1, 1),
    _CalixImaGroupAlarmObjIndex_Type()
)
calixImaGroupAlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupAlarmObjIndex.setStatus("current")
_CalixImaGroupAlarmCntIndex_Type = AlarmCntIndex
_CalixImaGroupAlarmCntIndex_Object = MibTableColumn
calixImaGroupAlarmCntIndex = _CalixImaGroupAlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1, 2),
    _CalixImaGroupAlarmCntIndex_Type()
)
calixImaGroupAlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupAlarmCntIndex.setStatus("current")
_CalixImaGroupAlarmObjTl1Aid_Type = Tl1Aid
_CalixImaGroupAlarmObjTl1Aid_Object = MibTableColumn
calixImaGroupAlarmObjTl1Aid = _CalixImaGroupAlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1, 3),
    _CalixImaGroupAlarmObjTl1Aid_Type()
)
calixImaGroupAlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupAlarmObjTl1Aid.setStatus("current")
_CalixImaGroupAlarmObjClass_Type = ObjClass
_CalixImaGroupAlarmObjClass_Object = MibTableColumn
calixImaGroupAlarmObjClass = _CalixImaGroupAlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1, 4),
    _CalixImaGroupAlarmObjClass_Type()
)
calixImaGroupAlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupAlarmObjClass.setStatus("current")
_CalixImaGroupAlarmSeverity_Type = AlarmSeverity
_CalixImaGroupAlarmSeverity_Object = MibTableColumn
calixImaGroupAlarmSeverity = _CalixImaGroupAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1, 5),
    _CalixImaGroupAlarmSeverity_Type()
)
calixImaGroupAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupAlarmSeverity.setStatus("current")
_CalixImaGroupAlarmType_Type = CondType
_CalixImaGroupAlarmType_Object = MibTableColumn
calixImaGroupAlarmType = _CalixImaGroupAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1, 6),
    _CalixImaGroupAlarmType_Type()
)
calixImaGroupAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupAlarmType.setStatus("current")


class _CalixImaGroupAlarmDescr_Type(OctetString):
    """Custom type calixImaGroupAlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixImaGroupAlarmDescr_Type.__name__ = "OctetString"
_CalixImaGroupAlarmDescr_Object = MibTableColumn
calixImaGroupAlarmDescr = _CalixImaGroupAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1, 7),
    _CalixImaGroupAlarmDescr_Type()
)
calixImaGroupAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupAlarmDescr.setStatus("current")
_CalixImaGroupAlarmSrvEffect_Type = SrvEffect
_CalixImaGroupAlarmSrvEffect_Object = MibTableColumn
calixImaGroupAlarmSrvEffect = _CalixImaGroupAlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1, 8),
    _CalixImaGroupAlarmSrvEffect_Type()
)
calixImaGroupAlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupAlarmSrvEffect.setStatus("current")
_CalixImaGroupAlarmLocation_Type = CondLocation
_CalixImaGroupAlarmLocation_Object = MibTableColumn
calixImaGroupAlarmLocation = _CalixImaGroupAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1, 9),
    _CalixImaGroupAlarmLocation_Type()
)
calixImaGroupAlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupAlarmLocation.setStatus("current")
_CalixImaGroupAlarmDateTime_Type = DateAndTime
_CalixImaGroupAlarmDateTime_Object = MibTableColumn
calixImaGroupAlarmDateTime = _CalixImaGroupAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1, 10),
    _CalixImaGroupAlarmDateTime_Type()
)
calixImaGroupAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupAlarmDateTime.setStatus("current")
_CalixImaGroupAlarmTimeStamp_Type = TimeStamp
_CalixImaGroupAlarmTimeStamp_Object = MibTableColumn
calixImaGroupAlarmTimeStamp = _CalixImaGroupAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 9, 1, 11),
    _CalixImaGroupAlarmTimeStamp_Type()
)
calixImaGroupAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupAlarmTimeStamp.setStatus("current")
_CalixImaLinkAlarmTable_Object = MibTable
calixImaLinkAlarmTable = _CalixImaLinkAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10)
)
if mibBuilder.loadTexts:
    calixImaLinkAlarmTable.setStatus("current")
_CalixImaLinkAlarmEntry_Object = MibTableRow
calixImaLinkAlarmEntry = _CalixImaLinkAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1)
)
calixImaLinkAlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixImaLinkAlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixImaLinkAlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixImaLinkAlarmEntry.setStatus("current")
_CalixImaLinkAlarmObjIndex_Type = ObjectIndex
_CalixImaLinkAlarmObjIndex_Object = MibTableColumn
calixImaLinkAlarmObjIndex = _CalixImaLinkAlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1, 1),
    _CalixImaLinkAlarmObjIndex_Type()
)
calixImaLinkAlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkAlarmObjIndex.setStatus("current")
_CalixImaLinkAlarmCntIndex_Type = AlarmCntIndex
_CalixImaLinkAlarmCntIndex_Object = MibTableColumn
calixImaLinkAlarmCntIndex = _CalixImaLinkAlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1, 2),
    _CalixImaLinkAlarmCntIndex_Type()
)
calixImaLinkAlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkAlarmCntIndex.setStatus("current")
_CalixImaLinkAlarmObjTl1Aid_Type = Tl1Aid
_CalixImaLinkAlarmObjTl1Aid_Object = MibTableColumn
calixImaLinkAlarmObjTl1Aid = _CalixImaLinkAlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1, 3),
    _CalixImaLinkAlarmObjTl1Aid_Type()
)
calixImaLinkAlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkAlarmObjTl1Aid.setStatus("current")
_CalixImaLinkAlarmObjClass_Type = ObjClass
_CalixImaLinkAlarmObjClass_Object = MibTableColumn
calixImaLinkAlarmObjClass = _CalixImaLinkAlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1, 4),
    _CalixImaLinkAlarmObjClass_Type()
)
calixImaLinkAlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkAlarmObjClass.setStatus("current")
_CalixImaLinkAlarmSeverity_Type = AlarmSeverity
_CalixImaLinkAlarmSeverity_Object = MibTableColumn
calixImaLinkAlarmSeverity = _CalixImaLinkAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1, 5),
    _CalixImaLinkAlarmSeverity_Type()
)
calixImaLinkAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkAlarmSeverity.setStatus("current")
_CalixImaLinkAlarmType_Type = CondType
_CalixImaLinkAlarmType_Object = MibTableColumn
calixImaLinkAlarmType = _CalixImaLinkAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1, 6),
    _CalixImaLinkAlarmType_Type()
)
calixImaLinkAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkAlarmType.setStatus("current")


class _CalixImaLinkAlarmDescr_Type(OctetString):
    """Custom type calixImaLinkAlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixImaLinkAlarmDescr_Type.__name__ = "OctetString"
_CalixImaLinkAlarmDescr_Object = MibTableColumn
calixImaLinkAlarmDescr = _CalixImaLinkAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1, 7),
    _CalixImaLinkAlarmDescr_Type()
)
calixImaLinkAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkAlarmDescr.setStatus("current")
_CalixImaLinkAlarmSrvEffect_Type = SrvEffect
_CalixImaLinkAlarmSrvEffect_Object = MibTableColumn
calixImaLinkAlarmSrvEffect = _CalixImaLinkAlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1, 8),
    _CalixImaLinkAlarmSrvEffect_Type()
)
calixImaLinkAlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkAlarmSrvEffect.setStatus("current")
_CalixImaLinkAlarmLocation_Type = CondLocation
_CalixImaLinkAlarmLocation_Object = MibTableColumn
calixImaLinkAlarmLocation = _CalixImaLinkAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1, 9),
    _CalixImaLinkAlarmLocation_Type()
)
calixImaLinkAlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkAlarmLocation.setStatus("current")
_CalixImaLinkAlarmDateTime_Type = DateAndTime
_CalixImaLinkAlarmDateTime_Object = MibTableColumn
calixImaLinkAlarmDateTime = _CalixImaLinkAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1, 10),
    _CalixImaLinkAlarmDateTime_Type()
)
calixImaLinkAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkAlarmDateTime.setStatus("current")
_CalixImaLinkAlarmTimeStamp_Type = TimeStamp
_CalixImaLinkAlarmTimeStamp_Object = MibTableColumn
calixImaLinkAlarmTimeStamp = _CalixImaLinkAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 10, 1, 11),
    _CalixImaLinkAlarmTimeStamp_Type()
)
calixImaLinkAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkAlarmTimeStamp.setStatus("current")
_CalixEthernetAlarmTable_Object = MibTable
calixEthernetAlarmTable = _CalixEthernetAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11)
)
if mibBuilder.loadTexts:
    calixEthernetAlarmTable.setStatus("current")
_CalixEthernetAlarmEntry_Object = MibTableRow
calixEthernetAlarmEntry = _CalixEthernetAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1)
)
calixEthernetAlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixEthernetAlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixEthernetAlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixEthernetAlarmEntry.setStatus("current")
_CalixEthernetAlarmObjIndex_Type = ObjectIndex
_CalixEthernetAlarmObjIndex_Object = MibTableColumn
calixEthernetAlarmObjIndex = _CalixEthernetAlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1, 1),
    _CalixEthernetAlarmObjIndex_Type()
)
calixEthernetAlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetAlarmObjIndex.setStatus("current")
_CalixEthernetAlarmCntIndex_Type = AlarmCntIndex
_CalixEthernetAlarmCntIndex_Object = MibTableColumn
calixEthernetAlarmCntIndex = _CalixEthernetAlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1, 2),
    _CalixEthernetAlarmCntIndex_Type()
)
calixEthernetAlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetAlarmCntIndex.setStatus("current")
_CalixEthernetAlarmObjTl1Aid_Type = Tl1Aid
_CalixEthernetAlarmObjTl1Aid_Object = MibTableColumn
calixEthernetAlarmObjTl1Aid = _CalixEthernetAlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1, 3),
    _CalixEthernetAlarmObjTl1Aid_Type()
)
calixEthernetAlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetAlarmObjTl1Aid.setStatus("current")
_CalixEthernetAlarmObjClass_Type = ObjClass
_CalixEthernetAlarmObjClass_Object = MibTableColumn
calixEthernetAlarmObjClass = _CalixEthernetAlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1, 4),
    _CalixEthernetAlarmObjClass_Type()
)
calixEthernetAlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetAlarmObjClass.setStatus("current")
_CalixEthernetAlarmSeverity_Type = AlarmSeverity
_CalixEthernetAlarmSeverity_Object = MibTableColumn
calixEthernetAlarmSeverity = _CalixEthernetAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1, 5),
    _CalixEthernetAlarmSeverity_Type()
)
calixEthernetAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetAlarmSeverity.setStatus("current")
_CalixEthernetAlarmType_Type = CondType
_CalixEthernetAlarmType_Object = MibTableColumn
calixEthernetAlarmType = _CalixEthernetAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1, 6),
    _CalixEthernetAlarmType_Type()
)
calixEthernetAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetAlarmType.setStatus("current")


class _CalixEthernetAlarmDescr_Type(OctetString):
    """Custom type calixEthernetAlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixEthernetAlarmDescr_Type.__name__ = "OctetString"
_CalixEthernetAlarmDescr_Object = MibTableColumn
calixEthernetAlarmDescr = _CalixEthernetAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1, 7),
    _CalixEthernetAlarmDescr_Type()
)
calixEthernetAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetAlarmDescr.setStatus("current")
_CalixEthernetAlarmSrvEffect_Type = SrvEffect
_CalixEthernetAlarmSrvEffect_Object = MibTableColumn
calixEthernetAlarmSrvEffect = _CalixEthernetAlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1, 8),
    _CalixEthernetAlarmSrvEffect_Type()
)
calixEthernetAlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetAlarmSrvEffect.setStatus("current")
_CalixEthernetAlarmLocation_Type = CondLocation
_CalixEthernetAlarmLocation_Object = MibTableColumn
calixEthernetAlarmLocation = _CalixEthernetAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1, 9),
    _CalixEthernetAlarmLocation_Type()
)
calixEthernetAlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetAlarmLocation.setStatus("current")
_CalixEthernetAlarmDateTime_Type = DateAndTime
_CalixEthernetAlarmDateTime_Object = MibTableColumn
calixEthernetAlarmDateTime = _CalixEthernetAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1, 10),
    _CalixEthernetAlarmDateTime_Type()
)
calixEthernetAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetAlarmDateTime.setStatus("current")
_CalixEthernetAlarmTimeStamp_Type = TimeStamp
_CalixEthernetAlarmTimeStamp_Object = MibTableColumn
calixEthernetAlarmTimeStamp = _CalixEthernetAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 11, 1, 11),
    _CalixEthernetAlarmTimeStamp_Type()
)
calixEthernetAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetAlarmTimeStamp.setStatus("current")
_CalixAllAlarmTable_Object = MibTable
calixAllAlarmTable = _CalixAllAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12)
)
if mibBuilder.loadTexts:
    calixAllAlarmTable.setStatus("current")
_CalixAllAlarmEntry_Object = MibTableRow
calixAllAlarmEntry = _CalixAllAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1)
)
calixAllAlarmEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixAllAlarmObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixAllAlarmCntIndex"),
)
if mibBuilder.loadTexts:
    calixAllAlarmEntry.setStatus("current")
_CalixAllAlarmObjIndex_Type = ObjectIndex
_CalixAllAlarmObjIndex_Object = MibTableColumn
calixAllAlarmObjIndex = _CalixAllAlarmObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1, 1),
    _CalixAllAlarmObjIndex_Type()
)
calixAllAlarmObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAllAlarmObjIndex.setStatus("current")
_CalixAllAlarmCntIndex_Type = AlarmCntIndex
_CalixAllAlarmCntIndex_Object = MibTableColumn
calixAllAlarmCntIndex = _CalixAllAlarmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1, 2),
    _CalixAllAlarmCntIndex_Type()
)
calixAllAlarmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAllAlarmCntIndex.setStatus("current")
_CalixAllAlarmObjTl1Aid_Type = Tl1Aid
_CalixAllAlarmObjTl1Aid_Object = MibTableColumn
calixAllAlarmObjTl1Aid = _CalixAllAlarmObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1, 3),
    _CalixAllAlarmObjTl1Aid_Type()
)
calixAllAlarmObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAllAlarmObjTl1Aid.setStatus("current")
_CalixAllAlarmObjClass_Type = ObjClass
_CalixAllAlarmObjClass_Object = MibTableColumn
calixAllAlarmObjClass = _CalixAllAlarmObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1, 4),
    _CalixAllAlarmObjClass_Type()
)
calixAllAlarmObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAllAlarmObjClass.setStatus("current")
_CalixAllAlarmSeverity_Type = AlarmSeverity
_CalixAllAlarmSeverity_Object = MibTableColumn
calixAllAlarmSeverity = _CalixAllAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1, 5),
    _CalixAllAlarmSeverity_Type()
)
calixAllAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAllAlarmSeverity.setStatus("current")
_CalixAllAlarmType_Type = CondType
_CalixAllAlarmType_Object = MibTableColumn
calixAllAlarmType = _CalixAllAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1, 6),
    _CalixAllAlarmType_Type()
)
calixAllAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAllAlarmType.setStatus("current")


class _CalixAllAlarmDescr_Type(OctetString):
    """Custom type calixAllAlarmDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixAllAlarmDescr_Type.__name__ = "OctetString"
_CalixAllAlarmDescr_Object = MibTableColumn
calixAllAlarmDescr = _CalixAllAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1, 7),
    _CalixAllAlarmDescr_Type()
)
calixAllAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAllAlarmDescr.setStatus("current")
_CalixAllAlarmSrvEffect_Type = SrvEffect
_CalixAllAlarmSrvEffect_Object = MibTableColumn
calixAllAlarmSrvEffect = _CalixAllAlarmSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1, 8),
    _CalixAllAlarmSrvEffect_Type()
)
calixAllAlarmSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAllAlarmSrvEffect.setStatus("current")
_CalixAllAlarmLocation_Type = CondLocation
_CalixAllAlarmLocation_Object = MibTableColumn
calixAllAlarmLocation = _CalixAllAlarmLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1, 9),
    _CalixAllAlarmLocation_Type()
)
calixAllAlarmLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAllAlarmLocation.setStatus("current")
_CalixAllAlarmDateTime_Type = DateAndTime
_CalixAllAlarmDateTime_Object = MibTableColumn
calixAllAlarmDateTime = _CalixAllAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1, 10),
    _CalixAllAlarmDateTime_Type()
)
calixAllAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAllAlarmDateTime.setStatus("current")
_CalixAllAlarmTimeStamp_Type = TimeStamp
_CalixAllAlarmTimeStamp_Object = MibTableColumn
calixAllAlarmTimeStamp = _CalixAllAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 1, 12, 1, 11),
    _CalixAllAlarmTimeStamp_Type()
)
calixAllAlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAllAlarmTimeStamp.setStatus("current")
_CalixCond_ObjectIdentity = ObjectIdentity
calixCond = _CalixCond_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2)
)
_CalixEqptCondTable_Object = MibTable
calixEqptCondTable = _CalixEqptCondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    calixEqptCondTable.setStatus("current")
_CalixEqptCondEntry_Object = MibTableRow
calixEqptCondEntry = _CalixEqptCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1)
)
calixEqptCondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixEqptCondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixEqptCondCntIndex"),
)
if mibBuilder.loadTexts:
    calixEqptCondEntry.setStatus("current")
_CalixEqptCondObjIndex_Type = ObjectIndex
_CalixEqptCondObjIndex_Object = MibTableColumn
calixEqptCondObjIndex = _CalixEqptCondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1, 1),
    _CalixEqptCondObjIndex_Type()
)
calixEqptCondObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptCondObjIndex.setStatus("current")
_CalixEqptCondCntIndex_Type = CondCntIndex
_CalixEqptCondCntIndex_Object = MibTableColumn
calixEqptCondCntIndex = _CalixEqptCondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1, 2),
    _CalixEqptCondCntIndex_Type()
)
calixEqptCondCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptCondCntIndex.setStatus("current")
_CalixEqptCondObjTl1Aid_Type = Tl1Aid
_CalixEqptCondObjTl1Aid_Object = MibTableColumn
calixEqptCondObjTl1Aid = _CalixEqptCondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1, 3),
    _CalixEqptCondObjTl1Aid_Type()
)
calixEqptCondObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptCondObjTl1Aid.setStatus("current")
_CalixEqptCondObjClass_Type = ObjClass
_CalixEqptCondObjClass_Object = MibTableColumn
calixEqptCondObjClass = _CalixEqptCondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1, 4),
    _CalixEqptCondObjClass_Type()
)
calixEqptCondObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptCondObjClass.setStatus("current")
_CalixEqptCondSeverity_Type = CondSeverity
_CalixEqptCondSeverity_Object = MibTableColumn
calixEqptCondSeverity = _CalixEqptCondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1, 5),
    _CalixEqptCondSeverity_Type()
)
calixEqptCondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptCondSeverity.setStatus("current")
_CalixEqptCondType_Type = CondType
_CalixEqptCondType_Object = MibTableColumn
calixEqptCondType = _CalixEqptCondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1, 6),
    _CalixEqptCondType_Type()
)
calixEqptCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptCondType.setStatus("current")


class _CalixEqptCondDescr_Type(OctetString):
    """Custom type calixEqptCondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixEqptCondDescr_Type.__name__ = "OctetString"
_CalixEqptCondDescr_Object = MibTableColumn
calixEqptCondDescr = _CalixEqptCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1, 7),
    _CalixEqptCondDescr_Type()
)
calixEqptCondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptCondDescr.setStatus("current")
_CalixEqptCondSrvEffect_Type = SrvEffect
_CalixEqptCondSrvEffect_Object = MibTableColumn
calixEqptCondSrvEffect = _CalixEqptCondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1, 8),
    _CalixEqptCondSrvEffect_Type()
)
calixEqptCondSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptCondSrvEffect.setStatus("current")
_CalixEqptCondLocation_Type = CondLocation
_CalixEqptCondLocation_Object = MibTableColumn
calixEqptCondLocation = _CalixEqptCondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1, 9),
    _CalixEqptCondLocation_Type()
)
calixEqptCondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptCondLocation.setStatus("current")
_CalixEqptCondDateTime_Type = DateAndTime
_CalixEqptCondDateTime_Object = MibTableColumn
calixEqptCondDateTime = _CalixEqptCondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1, 10),
    _CalixEqptCondDateTime_Type()
)
calixEqptCondDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptCondDateTime.setStatus("current")
_CalixEqptCondTimeStamp_Type = TimeStamp
_CalixEqptCondTimeStamp_Object = MibTableColumn
calixEqptCondTimeStamp = _CalixEqptCondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 1, 1, 11),
    _CalixEqptCondTimeStamp_Type()
)
calixEqptCondTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEqptCondTimeStamp.setStatus("current")
_CalixAdslCondTable_Object = MibTable
calixAdslCondTable = _CalixAdslCondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    calixAdslCondTable.setStatus("current")
_CalixAdslCondEntry_Object = MibTableRow
calixAdslCondEntry = _CalixAdslCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1)
)
calixAdslCondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixAdslCondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixAdslCondCntIndex"),
)
if mibBuilder.loadTexts:
    calixAdslCondEntry.setStatus("current")
_CalixAdslCondObjIndex_Type = ObjectIndex
_CalixAdslCondObjIndex_Object = MibTableColumn
calixAdslCondObjIndex = _CalixAdslCondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1, 1),
    _CalixAdslCondObjIndex_Type()
)
calixAdslCondObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslCondObjIndex.setStatus("current")
_CalixAdslCondCntIndex_Type = CondCntIndex
_CalixAdslCondCntIndex_Object = MibTableColumn
calixAdslCondCntIndex = _CalixAdslCondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1, 2),
    _CalixAdslCondCntIndex_Type()
)
calixAdslCondCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslCondCntIndex.setStatus("current")
_CalixAdslCondObjTl1Aid_Type = Tl1Aid
_CalixAdslCondObjTl1Aid_Object = MibTableColumn
calixAdslCondObjTl1Aid = _CalixAdslCondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1, 3),
    _CalixAdslCondObjTl1Aid_Type()
)
calixAdslCondObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslCondObjTl1Aid.setStatus("current")
_CalixAdslCondObjClass_Type = ObjClass
_CalixAdslCondObjClass_Object = MibTableColumn
calixAdslCondObjClass = _CalixAdslCondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1, 4),
    _CalixAdslCondObjClass_Type()
)
calixAdslCondObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslCondObjClass.setStatus("current")
_CalixAdslCondSeverity_Type = CondSeverity
_CalixAdslCondSeverity_Object = MibTableColumn
calixAdslCondSeverity = _CalixAdslCondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1, 5),
    _CalixAdslCondSeverity_Type()
)
calixAdslCondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslCondSeverity.setStatus("current")
_CalixAdslCondType_Type = CondType
_CalixAdslCondType_Object = MibTableColumn
calixAdslCondType = _CalixAdslCondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1, 6),
    _CalixAdslCondType_Type()
)
calixAdslCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslCondType.setStatus("current")


class _CalixAdslCondDescr_Type(OctetString):
    """Custom type calixAdslCondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixAdslCondDescr_Type.__name__ = "OctetString"
_CalixAdslCondDescr_Object = MibTableColumn
calixAdslCondDescr = _CalixAdslCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1, 7),
    _CalixAdslCondDescr_Type()
)
calixAdslCondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslCondDescr.setStatus("current")
_CalixAdslCondSrvEffect_Type = SrvEffect
_CalixAdslCondSrvEffect_Object = MibTableColumn
calixAdslCondSrvEffect = _CalixAdslCondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1, 8),
    _CalixAdslCondSrvEffect_Type()
)
calixAdslCondSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslCondSrvEffect.setStatus("current")
_CalixAdslCondLocation_Type = CondLocation
_CalixAdslCondLocation_Object = MibTableColumn
calixAdslCondLocation = _CalixAdslCondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1, 9),
    _CalixAdslCondLocation_Type()
)
calixAdslCondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslCondLocation.setStatus("current")
_CalixAdslCondDateTime_Type = DateAndTime
_CalixAdslCondDateTime_Object = MibTableColumn
calixAdslCondDateTime = _CalixAdslCondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1, 10),
    _CalixAdslCondDateTime_Type()
)
calixAdslCondDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslCondDateTime.setStatus("current")
_CalixAdslCondTimeStamp_Type = TimeStamp
_CalixAdslCondTimeStamp_Object = MibTableColumn
calixAdslCondTimeStamp = _CalixAdslCondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 2, 1, 11),
    _CalixAdslCondTimeStamp_Type()
)
calixAdslCondTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixAdslCondTimeStamp.setStatus("current")
_CalixDs0CondTable_Object = MibTable
calixDs0CondTable = _CalixDs0CondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    calixDs0CondTable.setStatus("current")
_CalixDs0CondEntry_Object = MibTableRow
calixDs0CondEntry = _CalixDs0CondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1)
)
calixDs0CondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixDs0CondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixDs0CondCntIndex"),
)
if mibBuilder.loadTexts:
    calixDs0CondEntry.setStatus("current")
_CalixDs0CondObjIndex_Type = ObjectIndex
_CalixDs0CondObjIndex_Object = MibTableColumn
calixDs0CondObjIndex = _CalixDs0CondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1, 1),
    _CalixDs0CondObjIndex_Type()
)
calixDs0CondObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0CondObjIndex.setStatus("current")
_CalixDs0CondCntIndex_Type = CondCntIndex
_CalixDs0CondCntIndex_Object = MibTableColumn
calixDs0CondCntIndex = _CalixDs0CondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1, 2),
    _CalixDs0CondCntIndex_Type()
)
calixDs0CondCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0CondCntIndex.setStatus("current")
_CalixDs0CondObjTl1Aid_Type = Tl1Aid
_CalixDs0CondObjTl1Aid_Object = MibTableColumn
calixDs0CondObjTl1Aid = _CalixDs0CondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1, 3),
    _CalixDs0CondObjTl1Aid_Type()
)
calixDs0CondObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0CondObjTl1Aid.setStatus("current")
_CalixDs0CondObjClass_Type = ObjClass
_CalixDs0CondObjClass_Object = MibTableColumn
calixDs0CondObjClass = _CalixDs0CondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1, 4),
    _CalixDs0CondObjClass_Type()
)
calixDs0CondObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0CondObjClass.setStatus("current")
_CalixDs0CondSeverity_Type = CondSeverity
_CalixDs0CondSeverity_Object = MibTableColumn
calixDs0CondSeverity = _CalixDs0CondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1, 5),
    _CalixDs0CondSeverity_Type()
)
calixDs0CondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0CondSeverity.setStatus("current")
_CalixDs0CondType_Type = CondType
_CalixDs0CondType_Object = MibTableColumn
calixDs0CondType = _CalixDs0CondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1, 6),
    _CalixDs0CondType_Type()
)
calixDs0CondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0CondType.setStatus("current")


class _CalixDs0CondDescr_Type(OctetString):
    """Custom type calixDs0CondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixDs0CondDescr_Type.__name__ = "OctetString"
_CalixDs0CondDescr_Object = MibTableColumn
calixDs0CondDescr = _CalixDs0CondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1, 7),
    _CalixDs0CondDescr_Type()
)
calixDs0CondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0CondDescr.setStatus("current")
_CalixDs0CondSrvEffect_Type = SrvEffect
_CalixDs0CondSrvEffect_Object = MibTableColumn
calixDs0CondSrvEffect = _CalixDs0CondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1, 8),
    _CalixDs0CondSrvEffect_Type()
)
calixDs0CondSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0CondSrvEffect.setStatus("current")
_CalixDs0CondLocation_Type = CondLocation
_CalixDs0CondLocation_Object = MibTableColumn
calixDs0CondLocation = _CalixDs0CondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1, 9),
    _CalixDs0CondLocation_Type()
)
calixDs0CondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0CondLocation.setStatus("current")
_CalixDs0CondDateTime_Type = DateAndTime
_CalixDs0CondDateTime_Object = MibTableColumn
calixDs0CondDateTime = _CalixDs0CondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1, 10),
    _CalixDs0CondDateTime_Type()
)
calixDs0CondDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0CondDateTime.setStatus("current")
_CalixDs0CondTimeStamp_Type = TimeStamp
_CalixDs0CondTimeStamp_Object = MibTableColumn
calixDs0CondTimeStamp = _CalixDs0CondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 3, 1, 11),
    _CalixDs0CondTimeStamp_Type()
)
calixDs0CondTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs0CondTimeStamp.setStatus("current")
_CalixDs1CondTable_Object = MibTable
calixDs1CondTable = _CalixDs1CondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    calixDs1CondTable.setStatus("current")
_CalixDs1CondEntry_Object = MibTableRow
calixDs1CondEntry = _CalixDs1CondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1)
)
calixDs1CondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixDs1CondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixDs1CondCntIndex"),
)
if mibBuilder.loadTexts:
    calixDs1CondEntry.setStatus("current")
_CalixDs1CondObjIndex_Type = ObjectIndex
_CalixDs1CondObjIndex_Object = MibTableColumn
calixDs1CondObjIndex = _CalixDs1CondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1, 1),
    _CalixDs1CondObjIndex_Type()
)
calixDs1CondObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1CondObjIndex.setStatus("current")
_CalixDs1CondCntIndex_Type = CondCntIndex
_CalixDs1CondCntIndex_Object = MibTableColumn
calixDs1CondCntIndex = _CalixDs1CondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1, 2),
    _CalixDs1CondCntIndex_Type()
)
calixDs1CondCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1CondCntIndex.setStatus("current")
_CalixDs1CondObjTl1Aid_Type = Tl1Aid
_CalixDs1CondObjTl1Aid_Object = MibTableColumn
calixDs1CondObjTl1Aid = _CalixDs1CondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1, 3),
    _CalixDs1CondObjTl1Aid_Type()
)
calixDs1CondObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1CondObjTl1Aid.setStatus("current")
_CalixDs1CondObjClass_Type = ObjClass
_CalixDs1CondObjClass_Object = MibTableColumn
calixDs1CondObjClass = _CalixDs1CondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1, 4),
    _CalixDs1CondObjClass_Type()
)
calixDs1CondObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1CondObjClass.setStatus("current")
_CalixDs1CondSeverity_Type = CondSeverity
_CalixDs1CondSeverity_Object = MibTableColumn
calixDs1CondSeverity = _CalixDs1CondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1, 5),
    _CalixDs1CondSeverity_Type()
)
calixDs1CondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1CondSeverity.setStatus("current")
_CalixDs1CondType_Type = CondType
_CalixDs1CondType_Object = MibTableColumn
calixDs1CondType = _CalixDs1CondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1, 6),
    _CalixDs1CondType_Type()
)
calixDs1CondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1CondType.setStatus("current")


class _CalixDs1CondDescr_Type(OctetString):
    """Custom type calixDs1CondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixDs1CondDescr_Type.__name__ = "OctetString"
_CalixDs1CondDescr_Object = MibTableColumn
calixDs1CondDescr = _CalixDs1CondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1, 7),
    _CalixDs1CondDescr_Type()
)
calixDs1CondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1CondDescr.setStatus("current")
_CalixDs1CondSrvEffect_Type = SrvEffect
_CalixDs1CondSrvEffect_Object = MibTableColumn
calixDs1CondSrvEffect = _CalixDs1CondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1, 8),
    _CalixDs1CondSrvEffect_Type()
)
calixDs1CondSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1CondSrvEffect.setStatus("current")
_CalixDs1CondLocation_Type = CondLocation
_CalixDs1CondLocation_Object = MibTableColumn
calixDs1CondLocation = _CalixDs1CondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1, 9),
    _CalixDs1CondLocation_Type()
)
calixDs1CondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1CondLocation.setStatus("current")
_CalixDs1CondDateTime_Type = DateAndTime
_CalixDs1CondDateTime_Object = MibTableColumn
calixDs1CondDateTime = _CalixDs1CondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1, 10),
    _CalixDs1CondDateTime_Type()
)
calixDs1CondDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1CondDateTime.setStatus("current")
_CalixDs1CondTimeStamp_Type = TimeStamp
_CalixDs1CondTimeStamp_Object = MibTableColumn
calixDs1CondTimeStamp = _CalixDs1CondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 4, 1, 11),
    _CalixDs1CondTimeStamp_Type()
)
calixDs1CondTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs1CondTimeStamp.setStatus("current")
_CalixDs3CondTable_Object = MibTable
calixDs3CondTable = _CalixDs3CondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5)
)
if mibBuilder.loadTexts:
    calixDs3CondTable.setStatus("current")
_CalixDs3CondEntry_Object = MibTableRow
calixDs3CondEntry = _CalixDs3CondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1)
)
calixDs3CondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixDs3CondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixDs3CondCntIndex"),
)
if mibBuilder.loadTexts:
    calixDs3CondEntry.setStatus("current")
_CalixDs3CondObjIndex_Type = ObjectIndex
_CalixDs3CondObjIndex_Object = MibTableColumn
calixDs3CondObjIndex = _CalixDs3CondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1, 1),
    _CalixDs3CondObjIndex_Type()
)
calixDs3CondObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3CondObjIndex.setStatus("current")
_CalixDs3CondCntIndex_Type = CondCntIndex
_CalixDs3CondCntIndex_Object = MibTableColumn
calixDs3CondCntIndex = _CalixDs3CondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1, 2),
    _CalixDs3CondCntIndex_Type()
)
calixDs3CondCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3CondCntIndex.setStatus("current")
_CalixDs3CondObjTl1Aid_Type = Tl1Aid
_CalixDs3CondObjTl1Aid_Object = MibTableColumn
calixDs3CondObjTl1Aid = _CalixDs3CondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1, 3),
    _CalixDs3CondObjTl1Aid_Type()
)
calixDs3CondObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3CondObjTl1Aid.setStatus("current")
_CalixDs3CondObjClass_Type = ObjClass
_CalixDs3CondObjClass_Object = MibTableColumn
calixDs3CondObjClass = _CalixDs3CondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1, 4),
    _CalixDs3CondObjClass_Type()
)
calixDs3CondObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3CondObjClass.setStatus("current")
_CalixDs3CondSeverity_Type = CondSeverity
_CalixDs3CondSeverity_Object = MibTableColumn
calixDs3CondSeverity = _CalixDs3CondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1, 5),
    _CalixDs3CondSeverity_Type()
)
calixDs3CondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3CondSeverity.setStatus("current")
_CalixDs3CondType_Type = CondType
_CalixDs3CondType_Object = MibTableColumn
calixDs3CondType = _CalixDs3CondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1, 6),
    _CalixDs3CondType_Type()
)
calixDs3CondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3CondType.setStatus("current")


class _CalixDs3CondDescr_Type(OctetString):
    """Custom type calixDs3CondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixDs3CondDescr_Type.__name__ = "OctetString"
_CalixDs3CondDescr_Object = MibTableColumn
calixDs3CondDescr = _CalixDs3CondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1, 7),
    _CalixDs3CondDescr_Type()
)
calixDs3CondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3CondDescr.setStatus("current")
_CalixDs3CondSrvEffect_Type = SrvEffect
_CalixDs3CondSrvEffect_Object = MibTableColumn
calixDs3CondSrvEffect = _CalixDs3CondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1, 8),
    _CalixDs3CondSrvEffect_Type()
)
calixDs3CondSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3CondSrvEffect.setStatus("current")
_CalixDs3CondLocation_Type = CondLocation
_CalixDs3CondLocation_Object = MibTableColumn
calixDs3CondLocation = _CalixDs3CondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1, 9),
    _CalixDs3CondLocation_Type()
)
calixDs3CondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3CondLocation.setStatus("current")
_CalixDs3CondDateTime_Type = DateAndTime
_CalixDs3CondDateTime_Object = MibTableColumn
calixDs3CondDateTime = _CalixDs3CondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1, 10),
    _CalixDs3CondDateTime_Type()
)
calixDs3CondDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3CondDateTime.setStatus("current")
_CalixDs3CondTimeStamp_Type = TimeStamp
_CalixDs3CondTimeStamp_Object = MibTableColumn
calixDs3CondTimeStamp = _CalixDs3CondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 5, 1, 11),
    _CalixDs3CondTimeStamp_Type()
)
calixDs3CondTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixDs3CondTimeStamp.setStatus("current")
_CalixOcCondTable_Object = MibTable
calixOcCondTable = _CalixOcCondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    calixOcCondTable.setStatus("current")
_CalixOcCondEntry_Object = MibTableRow
calixOcCondEntry = _CalixOcCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1)
)
calixOcCondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixOcCondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixOcCondCntIndex"),
)
if mibBuilder.loadTexts:
    calixOcCondEntry.setStatus("current")
_CalixOcCondObjIndex_Type = ObjectIndex
_CalixOcCondObjIndex_Object = MibTableColumn
calixOcCondObjIndex = _CalixOcCondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1, 1),
    _CalixOcCondObjIndex_Type()
)
calixOcCondObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcCondObjIndex.setStatus("current")
_CalixOcCondCntIndex_Type = CondCntIndex
_CalixOcCondCntIndex_Object = MibTableColumn
calixOcCondCntIndex = _CalixOcCondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1, 2),
    _CalixOcCondCntIndex_Type()
)
calixOcCondCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcCondCntIndex.setStatus("current")
_CalixOcCondObjTl1Aid_Type = Tl1Aid
_CalixOcCondObjTl1Aid_Object = MibTableColumn
calixOcCondObjTl1Aid = _CalixOcCondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1, 3),
    _CalixOcCondObjTl1Aid_Type()
)
calixOcCondObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcCondObjTl1Aid.setStatus("current")
_CalixOcCondObjClass_Type = ObjClass
_CalixOcCondObjClass_Object = MibTableColumn
calixOcCondObjClass = _CalixOcCondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1, 4),
    _CalixOcCondObjClass_Type()
)
calixOcCondObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcCondObjClass.setStatus("current")
_CalixOcCondSeverity_Type = CondSeverity
_CalixOcCondSeverity_Object = MibTableColumn
calixOcCondSeverity = _CalixOcCondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1, 5),
    _CalixOcCondSeverity_Type()
)
calixOcCondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcCondSeverity.setStatus("current")
_CalixOcCondType_Type = CondType
_CalixOcCondType_Object = MibTableColumn
calixOcCondType = _CalixOcCondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1, 6),
    _CalixOcCondType_Type()
)
calixOcCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcCondType.setStatus("current")


class _CalixOcCondDescr_Type(OctetString):
    """Custom type calixOcCondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixOcCondDescr_Type.__name__ = "OctetString"
_CalixOcCondDescr_Object = MibTableColumn
calixOcCondDescr = _CalixOcCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1, 7),
    _CalixOcCondDescr_Type()
)
calixOcCondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcCondDescr.setStatus("current")
_CalixOcCondSrvEffect_Type = SrvEffect
_CalixOcCondSrvEffect_Object = MibTableColumn
calixOcCondSrvEffect = _CalixOcCondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1, 8),
    _CalixOcCondSrvEffect_Type()
)
calixOcCondSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcCondSrvEffect.setStatus("current")
_CalixOcCondLocation_Type = CondLocation
_CalixOcCondLocation_Object = MibTableColumn
calixOcCondLocation = _CalixOcCondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1, 9),
    _CalixOcCondLocation_Type()
)
calixOcCondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcCondLocation.setStatus("current")
_CalixOcCondDateTime_Type = DateAndTime
_CalixOcCondDateTime_Object = MibTableColumn
calixOcCondDateTime = _CalixOcCondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1, 10),
    _CalixOcCondDateTime_Type()
)
calixOcCondDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcCondDateTime.setStatus("current")
_CalixOcCondTimeStamp_Type = TimeStamp
_CalixOcCondTimeStamp_Object = MibTableColumn
calixOcCondTimeStamp = _CalixOcCondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 6, 1, 11),
    _CalixOcCondTimeStamp_Type()
)
calixOcCondTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixOcCondTimeStamp.setStatus("current")
_CalixStsCondTable_Object = MibTable
calixStsCondTable = _CalixStsCondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7)
)
if mibBuilder.loadTexts:
    calixStsCondTable.setStatus("current")
_CalixStsCondEntry_Object = MibTableRow
calixStsCondEntry = _CalixStsCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1)
)
calixStsCondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixStsCondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixStsCondCntIndex"),
)
if mibBuilder.loadTexts:
    calixStsCondEntry.setStatus("current")
_CalixStsCondObjIndex_Type = ObjectIndex
_CalixStsCondObjIndex_Object = MibTableColumn
calixStsCondObjIndex = _CalixStsCondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1, 1),
    _CalixStsCondObjIndex_Type()
)
calixStsCondObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsCondObjIndex.setStatus("current")
_CalixStsCondCntIndex_Type = CondCntIndex
_CalixStsCondCntIndex_Object = MibTableColumn
calixStsCondCntIndex = _CalixStsCondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1, 2),
    _CalixStsCondCntIndex_Type()
)
calixStsCondCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsCondCntIndex.setStatus("current")
_CalixStsCondObjTl1Aid_Type = Tl1Aid
_CalixStsCondObjTl1Aid_Object = MibTableColumn
calixStsCondObjTl1Aid = _CalixStsCondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1, 3),
    _CalixStsCondObjTl1Aid_Type()
)
calixStsCondObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsCondObjTl1Aid.setStatus("current")
_CalixStsCondObjClass_Type = ObjClass
_CalixStsCondObjClass_Object = MibTableColumn
calixStsCondObjClass = _CalixStsCondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1, 4),
    _CalixStsCondObjClass_Type()
)
calixStsCondObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsCondObjClass.setStatus("current")
_CalixStsCondSeverity_Type = CondSeverity
_CalixStsCondSeverity_Object = MibTableColumn
calixStsCondSeverity = _CalixStsCondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1, 5),
    _CalixStsCondSeverity_Type()
)
calixStsCondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsCondSeverity.setStatus("current")
_CalixStsCondType_Type = CondType
_CalixStsCondType_Object = MibTableColumn
calixStsCondType = _CalixStsCondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1, 6),
    _CalixStsCondType_Type()
)
calixStsCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsCondType.setStatus("current")


class _CalixStsCondDescr_Type(OctetString):
    """Custom type calixStsCondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixStsCondDescr_Type.__name__ = "OctetString"
_CalixStsCondDescr_Object = MibTableColumn
calixStsCondDescr = _CalixStsCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1, 7),
    _CalixStsCondDescr_Type()
)
calixStsCondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsCondDescr.setStatus("current")
_CalixStsCondSrvEffect_Type = SrvEffect
_CalixStsCondSrvEffect_Object = MibTableColumn
calixStsCondSrvEffect = _CalixStsCondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1, 8),
    _CalixStsCondSrvEffect_Type()
)
calixStsCondSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsCondSrvEffect.setStatus("current")
_CalixStsCondLocation_Type = CondLocation
_CalixStsCondLocation_Object = MibTableColumn
calixStsCondLocation = _CalixStsCondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1, 9),
    _CalixStsCondLocation_Type()
)
calixStsCondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsCondLocation.setStatus("current")
_CalixStsCondDateTime_Type = DateAndTime
_CalixStsCondDateTime_Object = MibTableColumn
calixStsCondDateTime = _CalixStsCondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1, 10),
    _CalixStsCondDateTime_Type()
)
calixStsCondDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsCondDateTime.setStatus("current")
_CalixStsCondTimeStamp_Type = TimeStamp
_CalixStsCondTimeStamp_Object = MibTableColumn
calixStsCondTimeStamp = _CalixStsCondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 7, 1, 11),
    _CalixStsCondTimeStamp_Type()
)
calixStsCondTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixStsCondTimeStamp.setStatus("current")
_CalixEnvCondTable_Object = MibTable
calixEnvCondTable = _CalixEnvCondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8)
)
if mibBuilder.loadTexts:
    calixEnvCondTable.setStatus("current")
_CalixEnvCondEntry_Object = MibTableRow
calixEnvCondEntry = _CalixEnvCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1)
)
calixEnvCondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixEnvCondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixEnvCondCntIndex"),
)
if mibBuilder.loadTexts:
    calixEnvCondEntry.setStatus("current")
_CalixEnvCondObjIndex_Type = ObjectIndex
_CalixEnvCondObjIndex_Object = MibTableColumn
calixEnvCondObjIndex = _CalixEnvCondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1, 1),
    _CalixEnvCondObjIndex_Type()
)
calixEnvCondObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvCondObjIndex.setStatus("current")
_CalixEnvCondCntIndex_Type = CondCntIndex
_CalixEnvCondCntIndex_Object = MibTableColumn
calixEnvCondCntIndex = _CalixEnvCondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1, 2),
    _CalixEnvCondCntIndex_Type()
)
calixEnvCondCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvCondCntIndex.setStatus("current")
_CalixEnvCondObjTl1Aid_Type = Tl1Aid
_CalixEnvCondObjTl1Aid_Object = MibTableColumn
calixEnvCondObjTl1Aid = _CalixEnvCondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1, 3),
    _CalixEnvCondObjTl1Aid_Type()
)
calixEnvCondObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvCondObjTl1Aid.setStatus("current")
_CalixEnvCondObjClass_Type = ObjClass
_CalixEnvCondObjClass_Object = MibTableColumn
calixEnvCondObjClass = _CalixEnvCondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1, 4),
    _CalixEnvCondObjClass_Type()
)
calixEnvCondObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvCondObjClass.setStatus("current")
_CalixEnvCondSeverity_Type = CondSeverity
_CalixEnvCondSeverity_Object = MibTableColumn
calixEnvCondSeverity = _CalixEnvCondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1, 5),
    _CalixEnvCondSeverity_Type()
)
calixEnvCondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvCondSeverity.setStatus("current")
_CalixEnvCondType_Type = CondType
_CalixEnvCondType_Object = MibTableColumn
calixEnvCondType = _CalixEnvCondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1, 6),
    _CalixEnvCondType_Type()
)
calixEnvCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvCondType.setStatus("current")


class _CalixEnvCondDescr_Type(OctetString):
    """Custom type calixEnvCondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixEnvCondDescr_Type.__name__ = "OctetString"
_CalixEnvCondDescr_Object = MibTableColumn
calixEnvCondDescr = _CalixEnvCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1, 7),
    _CalixEnvCondDescr_Type()
)
calixEnvCondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvCondDescr.setStatus("current")
_CalixEnvCondSrvEffect_Type = SrvEffect
_CalixEnvCondSrvEffect_Object = MibTableColumn
calixEnvCondSrvEffect = _CalixEnvCondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1, 8),
    _CalixEnvCondSrvEffect_Type()
)
calixEnvCondSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvCondSrvEffect.setStatus("current")
_CalixEnvCondLocation_Type = CondLocation
_CalixEnvCondLocation_Object = MibTableColumn
calixEnvCondLocation = _CalixEnvCondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1, 9),
    _CalixEnvCondLocation_Type()
)
calixEnvCondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvCondLocation.setStatus("current")
_CalixEnvCondDateTime_Type = DateAndTime
_CalixEnvCondDateTime_Object = MibTableColumn
calixEnvCondDateTime = _CalixEnvCondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1, 10),
    _CalixEnvCondDateTime_Type()
)
calixEnvCondDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvCondDateTime.setStatus("current")
_CalixEnvCondTimeStamp_Type = TimeStamp
_CalixEnvCondTimeStamp_Object = MibTableColumn
calixEnvCondTimeStamp = _CalixEnvCondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 8, 1, 11),
    _CalixEnvCondTimeStamp_Type()
)
calixEnvCondTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEnvCondTimeStamp.setStatus("current")
_CalixImaGroupCondTable_Object = MibTable
calixImaGroupCondTable = _CalixImaGroupCondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9)
)
if mibBuilder.loadTexts:
    calixImaGroupCondTable.setStatus("current")
_CalixImaGroupCondEntry_Object = MibTableRow
calixImaGroupCondEntry = _CalixImaGroupCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1)
)
calixImaGroupCondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixImaGroupCondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixImaGroupCondCntIndex"),
)
if mibBuilder.loadTexts:
    calixImaGroupCondEntry.setStatus("current")
_CalixImaGroupCondObjIndex_Type = ObjectIndex
_CalixImaGroupCondObjIndex_Object = MibTableColumn
calixImaGroupCondObjIndex = _CalixImaGroupCondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1, 1),
    _CalixImaGroupCondObjIndex_Type()
)
calixImaGroupCondObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupCondObjIndex.setStatus("current")
_CalixImaGroupCondCntIndex_Type = CondCntIndex
_CalixImaGroupCondCntIndex_Object = MibTableColumn
calixImaGroupCondCntIndex = _CalixImaGroupCondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1, 2),
    _CalixImaGroupCondCntIndex_Type()
)
calixImaGroupCondCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupCondCntIndex.setStatus("current")
_CalixImaGroupCondObjTl1Aid_Type = Tl1Aid
_CalixImaGroupCondObjTl1Aid_Object = MibTableColumn
calixImaGroupCondObjTl1Aid = _CalixImaGroupCondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1, 3),
    _CalixImaGroupCondObjTl1Aid_Type()
)
calixImaGroupCondObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupCondObjTl1Aid.setStatus("current")
_CalixImaGroupCondObjClass_Type = ObjClass
_CalixImaGroupCondObjClass_Object = MibTableColumn
calixImaGroupCondObjClass = _CalixImaGroupCondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1, 4),
    _CalixImaGroupCondObjClass_Type()
)
calixImaGroupCondObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupCondObjClass.setStatus("current")
_CalixImaGroupCondSeverity_Type = CondSeverity
_CalixImaGroupCondSeverity_Object = MibTableColumn
calixImaGroupCondSeverity = _CalixImaGroupCondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1, 5),
    _CalixImaGroupCondSeverity_Type()
)
calixImaGroupCondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupCondSeverity.setStatus("current")
_CalixImaGroupCondType_Type = CondType
_CalixImaGroupCondType_Object = MibTableColumn
calixImaGroupCondType = _CalixImaGroupCondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1, 6),
    _CalixImaGroupCondType_Type()
)
calixImaGroupCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupCondType.setStatus("current")


class _CalixImaGroupCondDescr_Type(OctetString):
    """Custom type calixImaGroupCondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixImaGroupCondDescr_Type.__name__ = "OctetString"
_CalixImaGroupCondDescr_Object = MibTableColumn
calixImaGroupCondDescr = _CalixImaGroupCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1, 7),
    _CalixImaGroupCondDescr_Type()
)
calixImaGroupCondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupCondDescr.setStatus("current")
_CalixImaGroupCondSrvEffect_Type = SrvEffect
_CalixImaGroupCondSrvEffect_Object = MibTableColumn
calixImaGroupCondSrvEffect = _CalixImaGroupCondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1, 8),
    _CalixImaGroupCondSrvEffect_Type()
)
calixImaGroupCondSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupCondSrvEffect.setStatus("current")
_CalixImaGroupCondLocation_Type = CondLocation
_CalixImaGroupCondLocation_Object = MibTableColumn
calixImaGroupCondLocation = _CalixImaGroupCondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1, 9),
    _CalixImaGroupCondLocation_Type()
)
calixImaGroupCondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupCondLocation.setStatus("current")
_CalixImaGroupCondDateTime_Type = DateAndTime
_CalixImaGroupCondDateTime_Object = MibTableColumn
calixImaGroupCondDateTime = _CalixImaGroupCondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1, 10),
    _CalixImaGroupCondDateTime_Type()
)
calixImaGroupCondDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupCondDateTime.setStatus("current")
_CalixImaGroupCondTimeStamp_Type = TimeStamp
_CalixImaGroupCondTimeStamp_Object = MibTableColumn
calixImaGroupCondTimeStamp = _CalixImaGroupCondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 9, 1, 11),
    _CalixImaGroupCondTimeStamp_Type()
)
calixImaGroupCondTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaGroupCondTimeStamp.setStatus("current")
_CalixImaLinkCondTable_Object = MibTable
calixImaLinkCondTable = _CalixImaLinkCondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10)
)
if mibBuilder.loadTexts:
    calixImaLinkCondTable.setStatus("current")
_CalixImaLinkCondEntry_Object = MibTableRow
calixImaLinkCondEntry = _CalixImaLinkCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1)
)
calixImaLinkCondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixImaLinkCondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixImaLinkCondCntIndex"),
)
if mibBuilder.loadTexts:
    calixImaLinkCondEntry.setStatus("current")
_CalixImaLinkCondObjIndex_Type = ObjectIndex
_CalixImaLinkCondObjIndex_Object = MibTableColumn
calixImaLinkCondObjIndex = _CalixImaLinkCondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1, 1),
    _CalixImaLinkCondObjIndex_Type()
)
calixImaLinkCondObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkCondObjIndex.setStatus("current")
_CalixImaLinkCondCntIndex_Type = CondCntIndex
_CalixImaLinkCondCntIndex_Object = MibTableColumn
calixImaLinkCondCntIndex = _CalixImaLinkCondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1, 2),
    _CalixImaLinkCondCntIndex_Type()
)
calixImaLinkCondCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkCondCntIndex.setStatus("current")
_CalixImaLinkCondObjTl1Aid_Type = Tl1Aid
_CalixImaLinkCondObjTl1Aid_Object = MibTableColumn
calixImaLinkCondObjTl1Aid = _CalixImaLinkCondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1, 3),
    _CalixImaLinkCondObjTl1Aid_Type()
)
calixImaLinkCondObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkCondObjTl1Aid.setStatus("current")
_CalixImaLinkCondObjClass_Type = ObjClass
_CalixImaLinkCondObjClass_Object = MibTableColumn
calixImaLinkCondObjClass = _CalixImaLinkCondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1, 4),
    _CalixImaLinkCondObjClass_Type()
)
calixImaLinkCondObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkCondObjClass.setStatus("current")
_CalixImaLinkCondSeverity_Type = CondSeverity
_CalixImaLinkCondSeverity_Object = MibTableColumn
calixImaLinkCondSeverity = _CalixImaLinkCondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1, 5),
    _CalixImaLinkCondSeverity_Type()
)
calixImaLinkCondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkCondSeverity.setStatus("current")
_CalixImaLinkCondType_Type = CondType
_CalixImaLinkCondType_Object = MibTableColumn
calixImaLinkCondType = _CalixImaLinkCondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1, 6),
    _CalixImaLinkCondType_Type()
)
calixImaLinkCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkCondType.setStatus("current")


class _CalixImaLinkCondDescr_Type(OctetString):
    """Custom type calixImaLinkCondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixImaLinkCondDescr_Type.__name__ = "OctetString"
_CalixImaLinkCondDescr_Object = MibTableColumn
calixImaLinkCondDescr = _CalixImaLinkCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1, 7),
    _CalixImaLinkCondDescr_Type()
)
calixImaLinkCondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkCondDescr.setStatus("current")
_CalixImaLinkCondSrvEffect_Type = SrvEffect
_CalixImaLinkCondSrvEffect_Object = MibTableColumn
calixImaLinkCondSrvEffect = _CalixImaLinkCondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1, 8),
    _CalixImaLinkCondSrvEffect_Type()
)
calixImaLinkCondSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkCondSrvEffect.setStatus("current")
_CalixImaLinkCondLocation_Type = CondLocation
_CalixImaLinkCondLocation_Object = MibTableColumn
calixImaLinkCondLocation = _CalixImaLinkCondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1, 9),
    _CalixImaLinkCondLocation_Type()
)
calixImaLinkCondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkCondLocation.setStatus("current")
_CalixImaLinkCondDateTime_Type = DateAndTime
_CalixImaLinkCondDateTime_Object = MibTableColumn
calixImaLinkCondDateTime = _CalixImaLinkCondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1, 10),
    _CalixImaLinkCondDateTime_Type()
)
calixImaLinkCondDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkCondDateTime.setStatus("current")
_CalixImaLinkCondTimeStamp_Type = TimeStamp
_CalixImaLinkCondTimeStamp_Object = MibTableColumn
calixImaLinkCondTimeStamp = _CalixImaLinkCondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 10, 1, 11),
    _CalixImaLinkCondTimeStamp_Type()
)
calixImaLinkCondTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixImaLinkCondTimeStamp.setStatus("current")
_CalixEthernetCondTable_Object = MibTable
calixEthernetCondTable = _CalixEthernetCondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11)
)
if mibBuilder.loadTexts:
    calixEthernetCondTable.setStatus("current")
_CalixEthernetCondEntry_Object = MibTableRow
calixEthernetCondEntry = _CalixEthernetCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1)
)
calixEthernetCondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixEthernetCondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixEthernetCondCntIndex"),
)
if mibBuilder.loadTexts:
    calixEthernetCondEntry.setStatus("current")
_CalixEthernetCondObjIndex_Type = ObjectIndex
_CalixEthernetCondObjIndex_Object = MibTableColumn
calixEthernetCondObjIndex = _CalixEthernetCondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1, 1),
    _CalixEthernetCondObjIndex_Type()
)
calixEthernetCondObjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetCondObjIndex.setStatus("current")
_CalixEthernetCondCntIndex_Type = CondCntIndex
_CalixEthernetCondCntIndex_Object = MibTableColumn
calixEthernetCondCntIndex = _CalixEthernetCondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1, 2),
    _CalixEthernetCondCntIndex_Type()
)
calixEthernetCondCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetCondCntIndex.setStatus("current")
_CalixEthernetCondObjTl1Aid_Type = Tl1Aid
_CalixEthernetCondObjTl1Aid_Object = MibTableColumn
calixEthernetCondObjTl1Aid = _CalixEthernetCondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1, 3),
    _CalixEthernetCondObjTl1Aid_Type()
)
calixEthernetCondObjTl1Aid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetCondObjTl1Aid.setStatus("current")
_CalixEthernetCondObjClass_Type = ObjClass
_CalixEthernetCondObjClass_Object = MibTableColumn
calixEthernetCondObjClass = _CalixEthernetCondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1, 4),
    _CalixEthernetCondObjClass_Type()
)
calixEthernetCondObjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetCondObjClass.setStatus("current")
_CalixEthernetCondSeverity_Type = CondSeverity
_CalixEthernetCondSeverity_Object = MibTableColumn
calixEthernetCondSeverity = _CalixEthernetCondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1, 5),
    _CalixEthernetCondSeverity_Type()
)
calixEthernetCondSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetCondSeverity.setStatus("current")
_CalixEthernetCondType_Type = CondType
_CalixEthernetCondType_Object = MibTableColumn
calixEthernetCondType = _CalixEthernetCondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1, 6),
    _CalixEthernetCondType_Type()
)
calixEthernetCondType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetCondType.setStatus("current")


class _CalixEthernetCondDescr_Type(OctetString):
    """Custom type calixEthernetCondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixEthernetCondDescr_Type.__name__ = "OctetString"
_CalixEthernetCondDescr_Object = MibTableColumn
calixEthernetCondDescr = _CalixEthernetCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1, 7),
    _CalixEthernetCondDescr_Type()
)
calixEthernetCondDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetCondDescr.setStatus("current")
_CalixEthernetCondSrvEffect_Type = SrvEffect
_CalixEthernetCondSrvEffect_Object = MibTableColumn
calixEthernetCondSrvEffect = _CalixEthernetCondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1, 8),
    _CalixEthernetCondSrvEffect_Type()
)
calixEthernetCondSrvEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetCondSrvEffect.setStatus("current")
_CalixEthernetCondLocation_Type = CondLocation
_CalixEthernetCondLocation_Object = MibTableColumn
calixEthernetCondLocation = _CalixEthernetCondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1, 9),
    _CalixEthernetCondLocation_Type()
)
calixEthernetCondLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetCondLocation.setStatus("current")
_CalixEthernetCondDateTime_Type = DateAndTime
_CalixEthernetCondDateTime_Object = MibTableColumn
calixEthernetCondDateTime = _CalixEthernetCondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1, 10),
    _CalixEthernetCondDateTime_Type()
)
calixEthernetCondDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetCondDateTime.setStatus("current")
_CalixEthernetCondTimeStamp_Type = TimeStamp
_CalixEthernetCondTimeStamp_Object = MibTableColumn
calixEthernetCondTimeStamp = _CalixEthernetCondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 11, 1, 11),
    _CalixEthernetCondTimeStamp_Type()
)
calixEthernetCondTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    calixEthernetCondTimeStamp.setStatus("current")
_CalixAllCondTable_Object = MibTable
calixAllCondTable = _CalixAllCondTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12)
)
if mibBuilder.loadTexts:
    calixAllCondTable.setStatus("current")
_CalixAllCondEntry_Object = MibTableRow
calixAllCondEntry = _CalixAllCondEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12, 1)
)
calixAllCondEntry.setIndexNames(
    (0, "CALIX-FAULT-MIB", "calixAllCondObjIndex"),
    (0, "CALIX-FAULT-MIB", "calixAllCondCntIndex"),
)
if mibBuilder.loadTexts:
    calixAllCondEntry.setStatus("current")
_CalixAllCondObjIndex_Type = ObjectIndex
_CalixAllCondObjIndex_Object = MibTableColumn
calixAllCondObjIndex = _CalixAllCondObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12, 1, 1),
    _CalixAllCondObjIndex_Type()
)
calixAllCondObjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixAllCondObjIndex.setStatus("current")
_CalixAllCondCntIndex_Type = CondCntIndex
_CalixAllCondCntIndex_Object = MibTableColumn
calixAllCondCntIndex = _CalixAllCondCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12, 1, 2),
    _CalixAllCondCntIndex_Type()
)
calixAllCondCntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixAllCondCntIndex.setStatus("current")
_CalixAllCondObjTl1Aid_Type = Tl1Aid
_CalixAllCondObjTl1Aid_Object = MibTableColumn
calixAllCondObjTl1Aid = _CalixAllCondObjTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12, 1, 3),
    _CalixAllCondObjTl1Aid_Type()
)
calixAllCondObjTl1Aid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixAllCondObjTl1Aid.setStatus("current")
_CalixAllCondObjClass_Type = ObjClass
_CalixAllCondObjClass_Object = MibTableColumn
calixAllCondObjClass = _CalixAllCondObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12, 1, 4),
    _CalixAllCondObjClass_Type()
)
calixAllCondObjClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixAllCondObjClass.setStatus("current")
_CalixAllCondSeverity_Type = CondSeverity
_CalixAllCondSeverity_Object = MibTableColumn
calixAllCondSeverity = _CalixAllCondSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12, 1, 5),
    _CalixAllCondSeverity_Type()
)
calixAllCondSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixAllCondSeverity.setStatus("current")
_CalixAllCondType_Type = CondType
_CalixAllCondType_Object = MibTableColumn
calixAllCondType = _CalixAllCondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12, 1, 6),
    _CalixAllCondType_Type()
)
calixAllCondType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixAllCondType.setStatus("current")
_CalixAllCondSrvEffect_Type = SrvEffect
_CalixAllCondSrvEffect_Object = MibTableColumn
calixAllCondSrvEffect = _CalixAllCondSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12, 1, 7),
    _CalixAllCondSrvEffect_Type()
)
calixAllCondSrvEffect.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixAllCondSrvEffect.setStatus("current")
_CalixAllCondLocation_Type = CondLocation
_CalixAllCondLocation_Object = MibTableColumn
calixAllCondLocation = _CalixAllCondLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12, 1, 8),
    _CalixAllCondLocation_Type()
)
calixAllCondLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixAllCondLocation.setStatus("current")
_CalixAllCondDateTime_Type = DateAndTime
_CalixAllCondDateTime_Object = MibTableColumn
calixAllCondDateTime = _CalixAllCondDateTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12, 1, 9),
    _CalixAllCondDateTime_Type()
)
calixAllCondDateTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixAllCondDateTime.setStatus("current")
_CalixAllCondTimeStamp_Type = TimeStamp
_CalixAllCondTimeStamp_Object = MibTableColumn
calixAllCondTimeStamp = _CalixAllCondTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 2, 2, 12, 1, 10),
    _CalixAllCondTimeStamp_Type()
)
calixAllCondTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    calixAllCondTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-FAULT-MIB",
    **{"calixFault": calixFault,
       "calixFaultMIB": calixFaultMIB,
       "calixAlarm": calixAlarm,
       "calixEqptAlarmTable": calixEqptAlarmTable,
       "calixEqptAlarmEntry": calixEqptAlarmEntry,
       "calixEqptAlarmObjIndex": calixEqptAlarmObjIndex,
       "calixEqptAlarmCntIndex": calixEqptAlarmCntIndex,
       "calixEqptAlarmObjTl1Aid": calixEqptAlarmObjTl1Aid,
       "calixEqptAlarmObjClass": calixEqptAlarmObjClass,
       "calixEqptAlarmSeverity": calixEqptAlarmSeverity,
       "calixEqptAlarmType": calixEqptAlarmType,
       "calixEqptAlarmDescr": calixEqptAlarmDescr,
       "calixEqptAlarmSrvEffect": calixEqptAlarmSrvEffect,
       "calixEqptAlarmLocation": calixEqptAlarmLocation,
       "calixEqptAlarmDateTime": calixEqptAlarmDateTime,
       "calixEqptAlarmTimeStamp": calixEqptAlarmTimeStamp,
       "calixAdslAlarmTable": calixAdslAlarmTable,
       "calixAdslAlarmEntry": calixAdslAlarmEntry,
       "calixAdslAlarmObjIndex": calixAdslAlarmObjIndex,
       "calixAdslAlarmCntIndex": calixAdslAlarmCntIndex,
       "calixAdslAlarmObjTl1Aid": calixAdslAlarmObjTl1Aid,
       "calixAdslAlarmObjClass": calixAdslAlarmObjClass,
       "calixAdslAlarmSeverity": calixAdslAlarmSeverity,
       "calixAdslAlarmType": calixAdslAlarmType,
       "calixAdslAlarmDescr": calixAdslAlarmDescr,
       "calixAdslAlarmSrvEffect": calixAdslAlarmSrvEffect,
       "calixAdslAlarmLocation": calixAdslAlarmLocation,
       "calixAdslAlarmDateTime": calixAdslAlarmDateTime,
       "calixAdslAlarmTimeStamp": calixAdslAlarmTimeStamp,
       "calixDs0AlarmTable": calixDs0AlarmTable,
       "calixDs0AlarmEntry": calixDs0AlarmEntry,
       "calixDs0AlarmObjIndex": calixDs0AlarmObjIndex,
       "calixDs0AlarmCntIndex": calixDs0AlarmCntIndex,
       "calixDs0AlarmObjTl1Aid": calixDs0AlarmObjTl1Aid,
       "calixDs0AlarmObjClass": calixDs0AlarmObjClass,
       "calixDs0AlarmSeverity": calixDs0AlarmSeverity,
       "calixDs0AlarmType": calixDs0AlarmType,
       "calixDs0AlarmDescr": calixDs0AlarmDescr,
       "calixDs0AlarmSrvEffect": calixDs0AlarmSrvEffect,
       "calixDs0AlarmLocation": calixDs0AlarmLocation,
       "calixDs0AlarmDateTime": calixDs0AlarmDateTime,
       "calixDs0AlarmTimeStamp": calixDs0AlarmTimeStamp,
       "calixDs1AlarmTable": calixDs1AlarmTable,
       "calixDs1AlarmEntry": calixDs1AlarmEntry,
       "calixDs1AlarmObjIndex": calixDs1AlarmObjIndex,
       "calixDs1AlarmCntIndex": calixDs1AlarmCntIndex,
       "calixDs1AlarmObjTl1Aid": calixDs1AlarmObjTl1Aid,
       "calixDs1AlarmObjClass": calixDs1AlarmObjClass,
       "calixDs1AlarmSeverity": calixDs1AlarmSeverity,
       "calixDs1AlarmType": calixDs1AlarmType,
       "calixDs1AlarmDescr": calixDs1AlarmDescr,
       "calixDs1AlarmSrvEffect": calixDs1AlarmSrvEffect,
       "calixDs1AlarmLocation": calixDs1AlarmLocation,
       "calixDs1AlarmDateTime": calixDs1AlarmDateTime,
       "calixDs1AlarmTimeStamp": calixDs1AlarmTimeStamp,
       "calixDs3AlarmTable": calixDs3AlarmTable,
       "calixDs3AlarmEntry": calixDs3AlarmEntry,
       "calixDs3AlarmObjIndex": calixDs3AlarmObjIndex,
       "calixDs3AlarmCntIndex": calixDs3AlarmCntIndex,
       "calixDs3AlarmObjTl1Aid": calixDs3AlarmObjTl1Aid,
       "calixDs3AlarmObjClass": calixDs3AlarmObjClass,
       "calixDs3AlarmSeverity": calixDs3AlarmSeverity,
       "calixDs3AlarmType": calixDs3AlarmType,
       "calixDs3AlarmDescr": calixDs3AlarmDescr,
       "calixDs3AlarmSrvEffect": calixDs3AlarmSrvEffect,
       "calixDs3AlarmLocation": calixDs3AlarmLocation,
       "calixDs3AlarmDateTime": calixDs3AlarmDateTime,
       "calixDs3AlarmTimeStamp": calixDs3AlarmTimeStamp,
       "calixOcAlarmTable": calixOcAlarmTable,
       "calixOcAlarmEntry": calixOcAlarmEntry,
       "calixOcAlarmObjIndex": calixOcAlarmObjIndex,
       "calixOcAlarmCntIndex": calixOcAlarmCntIndex,
       "calixOcAlarmObjTl1Aid": calixOcAlarmObjTl1Aid,
       "calixOcAlarmObjClass": calixOcAlarmObjClass,
       "calixOcAlarmSeverity": calixOcAlarmSeverity,
       "calixOcAlarmType": calixOcAlarmType,
       "calixOcAlarmDescr": calixOcAlarmDescr,
       "calixOcAlarmSrvEffect": calixOcAlarmSrvEffect,
       "calixOcAlarmLocation": calixOcAlarmLocation,
       "calixOcAlarmDateTime": calixOcAlarmDateTime,
       "calixOcAlarmTimeStamp": calixOcAlarmTimeStamp,
       "calixStsAlarmTable": calixStsAlarmTable,
       "calixStsAlarmEntry": calixStsAlarmEntry,
       "calixStsAlarmObjIndex": calixStsAlarmObjIndex,
       "calixStsAlarmCntIndex": calixStsAlarmCntIndex,
       "calixStsAlarmObjTl1Aid": calixStsAlarmObjTl1Aid,
       "calixStsAlarmObjClass": calixStsAlarmObjClass,
       "calixStsAlarmSeverity": calixStsAlarmSeverity,
       "calixStsAlarmType": calixStsAlarmType,
       "calixStsAlarmDescr": calixStsAlarmDescr,
       "calixStsAlarmSrvEffect": calixStsAlarmSrvEffect,
       "calixStsAlarmLocation": calixStsAlarmLocation,
       "calixStsAlarmDateTime": calixStsAlarmDateTime,
       "calixStsAlarmTimeStamp": calixStsAlarmTimeStamp,
       "calixEnvAlarmTable": calixEnvAlarmTable,
       "calixEnvAlarmEntry": calixEnvAlarmEntry,
       "calixEnvAlarmObjIndex": calixEnvAlarmObjIndex,
       "calixEnvAlarmCntIndex": calixEnvAlarmCntIndex,
       "calixEnvAlarmObjTl1Aid": calixEnvAlarmObjTl1Aid,
       "calixEnvAlarmObjClass": calixEnvAlarmObjClass,
       "calixEnvAlarmSeverity": calixEnvAlarmSeverity,
       "calixEnvAlarmType": calixEnvAlarmType,
       "calixEnvAlarmDescr": calixEnvAlarmDescr,
       "calixEnvAlarmSrvEffect": calixEnvAlarmSrvEffect,
       "calixEnvAlarmLocation": calixEnvAlarmLocation,
       "calixEnvAlarmDateTime": calixEnvAlarmDateTime,
       "calixEnvAlarmTimeStamp": calixEnvAlarmTimeStamp,
       "calixImaGroupAlarmTable": calixImaGroupAlarmTable,
       "calixImaGroupAlarmEntry": calixImaGroupAlarmEntry,
       "calixImaGroupAlarmObjIndex": calixImaGroupAlarmObjIndex,
       "calixImaGroupAlarmCntIndex": calixImaGroupAlarmCntIndex,
       "calixImaGroupAlarmObjTl1Aid": calixImaGroupAlarmObjTl1Aid,
       "calixImaGroupAlarmObjClass": calixImaGroupAlarmObjClass,
       "calixImaGroupAlarmSeverity": calixImaGroupAlarmSeverity,
       "calixImaGroupAlarmType": calixImaGroupAlarmType,
       "calixImaGroupAlarmDescr": calixImaGroupAlarmDescr,
       "calixImaGroupAlarmSrvEffect": calixImaGroupAlarmSrvEffect,
       "calixImaGroupAlarmLocation": calixImaGroupAlarmLocation,
       "calixImaGroupAlarmDateTime": calixImaGroupAlarmDateTime,
       "calixImaGroupAlarmTimeStamp": calixImaGroupAlarmTimeStamp,
       "calixImaLinkAlarmTable": calixImaLinkAlarmTable,
       "calixImaLinkAlarmEntry": calixImaLinkAlarmEntry,
       "calixImaLinkAlarmObjIndex": calixImaLinkAlarmObjIndex,
       "calixImaLinkAlarmCntIndex": calixImaLinkAlarmCntIndex,
       "calixImaLinkAlarmObjTl1Aid": calixImaLinkAlarmObjTl1Aid,
       "calixImaLinkAlarmObjClass": calixImaLinkAlarmObjClass,
       "calixImaLinkAlarmSeverity": calixImaLinkAlarmSeverity,
       "calixImaLinkAlarmType": calixImaLinkAlarmType,
       "calixImaLinkAlarmDescr": calixImaLinkAlarmDescr,
       "calixImaLinkAlarmSrvEffect": calixImaLinkAlarmSrvEffect,
       "calixImaLinkAlarmLocation": calixImaLinkAlarmLocation,
       "calixImaLinkAlarmDateTime": calixImaLinkAlarmDateTime,
       "calixImaLinkAlarmTimeStamp": calixImaLinkAlarmTimeStamp,
       "calixEthernetAlarmTable": calixEthernetAlarmTable,
       "calixEthernetAlarmEntry": calixEthernetAlarmEntry,
       "calixEthernetAlarmObjIndex": calixEthernetAlarmObjIndex,
       "calixEthernetAlarmCntIndex": calixEthernetAlarmCntIndex,
       "calixEthernetAlarmObjTl1Aid": calixEthernetAlarmObjTl1Aid,
       "calixEthernetAlarmObjClass": calixEthernetAlarmObjClass,
       "calixEthernetAlarmSeverity": calixEthernetAlarmSeverity,
       "calixEthernetAlarmType": calixEthernetAlarmType,
       "calixEthernetAlarmDescr": calixEthernetAlarmDescr,
       "calixEthernetAlarmSrvEffect": calixEthernetAlarmSrvEffect,
       "calixEthernetAlarmLocation": calixEthernetAlarmLocation,
       "calixEthernetAlarmDateTime": calixEthernetAlarmDateTime,
       "calixEthernetAlarmTimeStamp": calixEthernetAlarmTimeStamp,
       "calixAllAlarmTable": calixAllAlarmTable,
       "calixAllAlarmEntry": calixAllAlarmEntry,
       "calixAllAlarmObjIndex": calixAllAlarmObjIndex,
       "calixAllAlarmCntIndex": calixAllAlarmCntIndex,
       "calixAllAlarmObjTl1Aid": calixAllAlarmObjTl1Aid,
       "calixAllAlarmObjClass": calixAllAlarmObjClass,
       "calixAllAlarmSeverity": calixAllAlarmSeverity,
       "calixAllAlarmType": calixAllAlarmType,
       "calixAllAlarmDescr": calixAllAlarmDescr,
       "calixAllAlarmSrvEffect": calixAllAlarmSrvEffect,
       "calixAllAlarmLocation": calixAllAlarmLocation,
       "calixAllAlarmDateTime": calixAllAlarmDateTime,
       "calixAllAlarmTimeStamp": calixAllAlarmTimeStamp,
       "calixCond": calixCond,
       "calixEqptCondTable": calixEqptCondTable,
       "calixEqptCondEntry": calixEqptCondEntry,
       "calixEqptCondObjIndex": calixEqptCondObjIndex,
       "calixEqptCondCntIndex": calixEqptCondCntIndex,
       "calixEqptCondObjTl1Aid": calixEqptCondObjTl1Aid,
       "calixEqptCondObjClass": calixEqptCondObjClass,
       "calixEqptCondSeverity": calixEqptCondSeverity,
       "calixEqptCondType": calixEqptCondType,
       "calixEqptCondDescr": calixEqptCondDescr,
       "calixEqptCondSrvEffect": calixEqptCondSrvEffect,
       "calixEqptCondLocation": calixEqptCondLocation,
       "calixEqptCondDateTime": calixEqptCondDateTime,
       "calixEqptCondTimeStamp": calixEqptCondTimeStamp,
       "calixAdslCondTable": calixAdslCondTable,
       "calixAdslCondEntry": calixAdslCondEntry,
       "calixAdslCondObjIndex": calixAdslCondObjIndex,
       "calixAdslCondCntIndex": calixAdslCondCntIndex,
       "calixAdslCondObjTl1Aid": calixAdslCondObjTl1Aid,
       "calixAdslCondObjClass": calixAdslCondObjClass,
       "calixAdslCondSeverity": calixAdslCondSeverity,
       "calixAdslCondType": calixAdslCondType,
       "calixAdslCondDescr": calixAdslCondDescr,
       "calixAdslCondSrvEffect": calixAdslCondSrvEffect,
       "calixAdslCondLocation": calixAdslCondLocation,
       "calixAdslCondDateTime": calixAdslCondDateTime,
       "calixAdslCondTimeStamp": calixAdslCondTimeStamp,
       "calixDs0CondTable": calixDs0CondTable,
       "calixDs0CondEntry": calixDs0CondEntry,
       "calixDs0CondObjIndex": calixDs0CondObjIndex,
       "calixDs0CondCntIndex": calixDs0CondCntIndex,
       "calixDs0CondObjTl1Aid": calixDs0CondObjTl1Aid,
       "calixDs0CondObjClass": calixDs0CondObjClass,
       "calixDs0CondSeverity": calixDs0CondSeverity,
       "calixDs0CondType": calixDs0CondType,
       "calixDs0CondDescr": calixDs0CondDescr,
       "calixDs0CondSrvEffect": calixDs0CondSrvEffect,
       "calixDs0CondLocation": calixDs0CondLocation,
       "calixDs0CondDateTime": calixDs0CondDateTime,
       "calixDs0CondTimeStamp": calixDs0CondTimeStamp,
       "calixDs1CondTable": calixDs1CondTable,
       "calixDs1CondEntry": calixDs1CondEntry,
       "calixDs1CondObjIndex": calixDs1CondObjIndex,
       "calixDs1CondCntIndex": calixDs1CondCntIndex,
       "calixDs1CondObjTl1Aid": calixDs1CondObjTl1Aid,
       "calixDs1CondObjClass": calixDs1CondObjClass,
       "calixDs1CondSeverity": calixDs1CondSeverity,
       "calixDs1CondType": calixDs1CondType,
       "calixDs1CondDescr": calixDs1CondDescr,
       "calixDs1CondSrvEffect": calixDs1CondSrvEffect,
       "calixDs1CondLocation": calixDs1CondLocation,
       "calixDs1CondDateTime": calixDs1CondDateTime,
       "calixDs1CondTimeStamp": calixDs1CondTimeStamp,
       "calixDs3CondTable": calixDs3CondTable,
       "calixDs3CondEntry": calixDs3CondEntry,
       "calixDs3CondObjIndex": calixDs3CondObjIndex,
       "calixDs3CondCntIndex": calixDs3CondCntIndex,
       "calixDs3CondObjTl1Aid": calixDs3CondObjTl1Aid,
       "calixDs3CondObjClass": calixDs3CondObjClass,
       "calixDs3CondSeverity": calixDs3CondSeverity,
       "calixDs3CondType": calixDs3CondType,
       "calixDs3CondDescr": calixDs3CondDescr,
       "calixDs3CondSrvEffect": calixDs3CondSrvEffect,
       "calixDs3CondLocation": calixDs3CondLocation,
       "calixDs3CondDateTime": calixDs3CondDateTime,
       "calixDs3CondTimeStamp": calixDs3CondTimeStamp,
       "calixOcCondTable": calixOcCondTable,
       "calixOcCondEntry": calixOcCondEntry,
       "calixOcCondObjIndex": calixOcCondObjIndex,
       "calixOcCondCntIndex": calixOcCondCntIndex,
       "calixOcCondObjTl1Aid": calixOcCondObjTl1Aid,
       "calixOcCondObjClass": calixOcCondObjClass,
       "calixOcCondSeverity": calixOcCondSeverity,
       "calixOcCondType": calixOcCondType,
       "calixOcCondDescr": calixOcCondDescr,
       "calixOcCondSrvEffect": calixOcCondSrvEffect,
       "calixOcCondLocation": calixOcCondLocation,
       "calixOcCondDateTime": calixOcCondDateTime,
       "calixOcCondTimeStamp": calixOcCondTimeStamp,
       "calixStsCondTable": calixStsCondTable,
       "calixStsCondEntry": calixStsCondEntry,
       "calixStsCondObjIndex": calixStsCondObjIndex,
       "calixStsCondCntIndex": calixStsCondCntIndex,
       "calixStsCondObjTl1Aid": calixStsCondObjTl1Aid,
       "calixStsCondObjClass": calixStsCondObjClass,
       "calixStsCondSeverity": calixStsCondSeverity,
       "calixStsCondType": calixStsCondType,
       "calixStsCondDescr": calixStsCondDescr,
       "calixStsCondSrvEffect": calixStsCondSrvEffect,
       "calixStsCondLocation": calixStsCondLocation,
       "calixStsCondDateTime": calixStsCondDateTime,
       "calixStsCondTimeStamp": calixStsCondTimeStamp,
       "calixEnvCondTable": calixEnvCondTable,
       "calixEnvCondEntry": calixEnvCondEntry,
       "calixEnvCondObjIndex": calixEnvCondObjIndex,
       "calixEnvCondCntIndex": calixEnvCondCntIndex,
       "calixEnvCondObjTl1Aid": calixEnvCondObjTl1Aid,
       "calixEnvCondObjClass": calixEnvCondObjClass,
       "calixEnvCondSeverity": calixEnvCondSeverity,
       "calixEnvCondType": calixEnvCondType,
       "calixEnvCondDescr": calixEnvCondDescr,
       "calixEnvCondSrvEffect": calixEnvCondSrvEffect,
       "calixEnvCondLocation": calixEnvCondLocation,
       "calixEnvCondDateTime": calixEnvCondDateTime,
       "calixEnvCondTimeStamp": calixEnvCondTimeStamp,
       "calixImaGroupCondTable": calixImaGroupCondTable,
       "calixImaGroupCondEntry": calixImaGroupCondEntry,
       "calixImaGroupCondObjIndex": calixImaGroupCondObjIndex,
       "calixImaGroupCondCntIndex": calixImaGroupCondCntIndex,
       "calixImaGroupCondObjTl1Aid": calixImaGroupCondObjTl1Aid,
       "calixImaGroupCondObjClass": calixImaGroupCondObjClass,
       "calixImaGroupCondSeverity": calixImaGroupCondSeverity,
       "calixImaGroupCondType": calixImaGroupCondType,
       "calixImaGroupCondDescr": calixImaGroupCondDescr,
       "calixImaGroupCondSrvEffect": calixImaGroupCondSrvEffect,
       "calixImaGroupCondLocation": calixImaGroupCondLocation,
       "calixImaGroupCondDateTime": calixImaGroupCondDateTime,
       "calixImaGroupCondTimeStamp": calixImaGroupCondTimeStamp,
       "calixImaLinkCondTable": calixImaLinkCondTable,
       "calixImaLinkCondEntry": calixImaLinkCondEntry,
       "calixImaLinkCondObjIndex": calixImaLinkCondObjIndex,
       "calixImaLinkCondCntIndex": calixImaLinkCondCntIndex,
       "calixImaLinkCondObjTl1Aid": calixImaLinkCondObjTl1Aid,
       "calixImaLinkCondObjClass": calixImaLinkCondObjClass,
       "calixImaLinkCondSeverity": calixImaLinkCondSeverity,
       "calixImaLinkCondType": calixImaLinkCondType,
       "calixImaLinkCondDescr": calixImaLinkCondDescr,
       "calixImaLinkCondSrvEffect": calixImaLinkCondSrvEffect,
       "calixImaLinkCondLocation": calixImaLinkCondLocation,
       "calixImaLinkCondDateTime": calixImaLinkCondDateTime,
       "calixImaLinkCondTimeStamp": calixImaLinkCondTimeStamp,
       "calixEthernetCondTable": calixEthernetCondTable,
       "calixEthernetCondEntry": calixEthernetCondEntry,
       "calixEthernetCondObjIndex": calixEthernetCondObjIndex,
       "calixEthernetCondCntIndex": calixEthernetCondCntIndex,
       "calixEthernetCondObjTl1Aid": calixEthernetCondObjTl1Aid,
       "calixEthernetCondObjClass": calixEthernetCondObjClass,
       "calixEthernetCondSeverity": calixEthernetCondSeverity,
       "calixEthernetCondType": calixEthernetCondType,
       "calixEthernetCondDescr": calixEthernetCondDescr,
       "calixEthernetCondSrvEffect": calixEthernetCondSrvEffect,
       "calixEthernetCondLocation": calixEthernetCondLocation,
       "calixEthernetCondDateTime": calixEthernetCondDateTime,
       "calixEthernetCondTimeStamp": calixEthernetCondTimeStamp,
       "calixAllCondTable": calixAllCondTable,
       "calixAllCondEntry": calixAllCondEntry,
       "calixAllCondObjIndex": calixAllCondObjIndex,
       "calixAllCondCntIndex": calixAllCondCntIndex,
       "calixAllCondObjTl1Aid": calixAllCondObjTl1Aid,
       "calixAllCondObjClass": calixAllCondObjClass,
       "calixAllCondSeverity": calixAllCondSeverity,
       "calixAllCondType": calixAllCondType,
       "calixAllCondSrvEffect": calixAllCondSrvEffect,
       "calixAllCondLocation": calixAllCondLocation,
       "calixAllCondDateTime": calixAllCondDateTime,
       "calixAllCondTimeStamp": calixAllCondTimeStamp}
)
