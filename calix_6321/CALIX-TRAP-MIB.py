# SNMP MIB module (CALIX-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/CALIX-TRAP-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:36:06 2025
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

(AlarmSeverity,
 AlarmTransition,
 CondLocation,
 CondState,
 CondType,
 DatalinkType,
 InterfaceIndex,
 MonVal,
 ObjClass,
 ObjState,
 ShelfId,
 SrvEffect,
 ThLev,
 Tl1Aid,
 TmPer) = mibBuilder.importSymbols(
    "CALIX-TC",
    "AlarmSeverity",
    "AlarmTransition",
    "CondLocation",
    "CondState",
    "CondType",
    "DatalinkType",
    "InterfaceIndex",
    "MonVal",
    "ObjClass",
    "ObjState",
    "ShelfId",
    "SrvEffect",
    "ThLev",
    "Tl1Aid",
    "TmPer")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "NotificationType",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

calixTrap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 1, 4)
)
if mibBuilder.loadTexts:
    calixTrap.setRevisions(
        ("2000-08-31 00:26",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CalixTrapMIB_ObjectIdentity = ObjectIdentity
calixTrapMIB = _CalixTrapMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3)
)
_CalixTraps_ObjectIdentity = ObjectIdentity
calixTraps = _CalixTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1)
)
_CalixTrapObjects_ObjectIdentity = ObjectIdentity
calixTrapObjects = _CalixTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2)
)
_CalixTrapObjClass_Type = ObjClass
_CalixTrapObjClass_Object = MibScalar
calixTrapObjClass = _CalixTrapObjClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 1),
    _CalixTrapObjClass_Type()
)
calixTrapObjClass.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapObjClass.setStatus("current")
_CalixTrapShelfId_Type = ShelfId
_CalixTrapShelfId_Object = MibScalar
calixTrapShelfId = _CalixTrapShelfId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 2),
    _CalixTrapShelfId_Type()
)
calixTrapShelfId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapShelfId.setStatus("current")
_CalixTrapTl1Aid_Type = Tl1Aid
_CalixTrapTl1Aid_Object = MibScalar
calixTrapTl1Aid = _CalixTrapTl1Aid_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 3),
    _CalixTrapTl1Aid_Type()
)
calixTrapTl1Aid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapTl1Aid.setStatus("current")
_CalixTrapObjIndex_Type = InterfaceIndex
_CalixTrapObjIndex_Object = MibScalar
calixTrapObjIndex = _CalixTrapObjIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 4),
    _CalixTrapObjIndex_Type()
)
calixTrapObjIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapObjIndex.setStatus("current")


class _CalixTrapObjState_Type(OctetString):
    """Custom type calixTrapObjState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CalixTrapObjState_Type.__name__ = "OctetString"
_CalixTrapObjState_Object = MibScalar
calixTrapObjState = _CalixTrapObjState_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 6),
    _CalixTrapObjState_Type()
)
calixTrapObjState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapObjState.setStatus("current")


class _CalixTrapSerialNr_Type(Integer32):
    """Custom type calixTrapSerialNr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_CalixTrapSerialNr_Type.__name__ = "Integer32"
_CalixTrapSerialNr_Object = MibScalar
calixTrapSerialNr = _CalixTrapSerialNr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 7),
    _CalixTrapSerialNr_Type()
)
calixTrapSerialNr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapSerialNr.setStatus("current")
_CalixTrapAlarmTransition_Type = AlarmTransition
_CalixTrapAlarmTransition_Object = MibScalar
calixTrapAlarmTransition = _CalixTrapAlarmTransition_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 8),
    _CalixTrapAlarmTransition_Type()
)
calixTrapAlarmTransition.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapAlarmTransition.setStatus("current")
_CalixTrapAlarmSeverity_Type = AlarmSeverity
_CalixTrapAlarmSeverity_Object = MibScalar
calixTrapAlarmSeverity = _CalixTrapAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 9),
    _CalixTrapAlarmSeverity_Type()
)
calixTrapAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapAlarmSeverity.setStatus("current")
_CalixTrapAlarmType_Type = CondType
_CalixTrapAlarmType_Object = MibScalar
calixTrapAlarmType = _CalixTrapAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 10),
    _CalixTrapAlarmType_Type()
)
calixTrapAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapAlarmType.setStatus("current")
_CalixTrapCondType_Type = CondType
_CalixTrapCondType_Object = MibScalar
calixTrapCondType = _CalixTrapCondType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 11),
    _CalixTrapCondType_Type()
)
calixTrapCondType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapCondType.setStatus("current")
_CalixTrapSrvEffect_Type = SrvEffect
_CalixTrapSrvEffect_Object = MibScalar
calixTrapSrvEffect = _CalixTrapSrvEffect_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 12),
    _CalixTrapSrvEffect_Type()
)
calixTrapSrvEffect.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapSrvEffect.setStatus("current")


class _CalixTrapCondDescr_Type(OctetString):
    """Custom type calixTrapCondDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CalixTrapCondDescr_Type.__name__ = "OctetString"
_CalixTrapCondDescr_Object = MibScalar
calixTrapCondDescr = _CalixTrapCondDescr_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 13),
    _CalixTrapCondDescr_Type()
)
calixTrapCondDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapCondDescr.setStatus("current")
_CalixTrapMonValue_Type = MonVal
_CalixTrapMonValue_Object = MibScalar
calixTrapMonValue = _CalixTrapMonValue_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 14),
    _CalixTrapMonValue_Type()
)
calixTrapMonValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapMonValue.setStatus("current")
_CalixTrapThLevel_Type = ThLev
_CalixTrapThLevel_Object = MibScalar
calixTrapThLevel = _CalixTrapThLevel_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 15),
    _CalixTrapThLevel_Type()
)
calixTrapThLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapThLevel.setStatus("current")
_CalixTrapTmPeriod_Type = TmPer
_CalixTrapTmPeriod_Object = MibScalar
calixTrapTmPeriod = _CalixTrapTmPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 16),
    _CalixTrapTmPeriod_Type()
)
calixTrapTmPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapTmPeriod.setStatus("current")
_CalixTrapCondState_Type = CondState
_CalixTrapCondState_Object = MibScalar
calixTrapCondState = _CalixTrapCondState_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 17),
    _CalixTrapCondState_Type()
)
calixTrapCondState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapCondState.setStatus("current")
_CalixTrapLocation_Type = CondLocation
_CalixTrapLocation_Object = MibScalar
calixTrapLocation = _CalixTrapLocation_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 18),
    _CalixTrapLocation_Type()
)
calixTrapLocation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapLocation.setStatus("current")


class _CalixTrapStbySlot_Type(Integer32):
    """Custom type calixTrapStbySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CalixTrapStbySlot_Type.__name__ = "Integer32"
_CalixTrapStbySlot_Object = MibScalar
calixTrapStbySlot = _CalixTrapStbySlot_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 19),
    _CalixTrapStbySlot_Type()
)
calixTrapStbySlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapStbySlot.setStatus("current")


class _CalixTrapIntfGroup_Type(Integer32):
    """Custom type calixTrapIntfGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CalixTrapIntfGroup_Type.__name__ = "Integer32"
_CalixTrapIntfGroup_Object = MibScalar
calixTrapIntfGroup = _CalixTrapIntfGroup_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 20),
    _CalixTrapIntfGroup_Type()
)
calixTrapIntfGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapIntfGroup.setStatus("current")
_CalixTrapDLinkType_Type = DatalinkType
_CalixTrapDLinkType_Object = MibScalar
calixTrapDLinkType = _CalixTrapDLinkType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 21),
    _CalixTrapDLinkType_Type()
)
calixTrapDLinkType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapDLinkType.setStatus("current")


class _CalixTrapStbyIntfGroup_Type(Integer32):
    """Custom type calixTrapStbyIntfGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CalixTrapStbyIntfGroup_Type.__name__ = "Integer32"
_CalixTrapStbyIntfGroup_Object = MibScalar
calixTrapStbyIntfGroup = _CalixTrapStbyIntfGroup_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 23),
    _CalixTrapStbyIntfGroup_Type()
)
calixTrapStbyIntfGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapStbyIntfGroup.setStatus("current")
_CalixTrapStbyDLinkType_Type = DatalinkType
_CalixTrapStbyDLinkType_Object = MibScalar
calixTrapStbyDLinkType = _CalixTrapStbyDLinkType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 2, 24),
    _CalixTrapStbyDLinkType_Type()
)
calixTrapStbyDLinkType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    calixTrapStbyDLinkType.setStatus("current")

# Managed Objects groups


# Notification objects

calixTrapALARM = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 1)
)
calixTrapALARM.setObjects(
      *(("CALIX-TRAP-MIB", "calixTrapTl1Aid"),
        ("CALIX-TRAP-MIB", "calixTrapAlarmTransition"),
        ("CALIX-TRAP-MIB", "calixTrapAlarmSeverity"),
        ("CALIX-TRAP-MIB", "calixTrapAlarmType"),
        ("CALIX-TRAP-MIB", "calixTrapSrvEffect"),
        ("CALIX-TRAP-MIB", "calixTrapCondDescr"),
        ("CALIX-TRAP-MIB", "calixTrapLocation"),
        ("CALIX-TRAP-MIB", "calixTrapObjClass"),
        ("CALIX-TRAP-MIB", "calixTrapObjIndex"),
        ("CALIX-TRAP-MIB", "calixTrapSerialNr"))
)
if mibBuilder.loadTexts:
    calixTrapALARM.setStatus(
        "current"
    )

calixTrapTCAEVENT = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 2)
)
calixTrapTCAEVENT.setObjects(
      *(("CALIX-TRAP-MIB", "calixTrapTl1Aid"),
        ("CALIX-TRAP-MIB", "calixTrapCondType"),
        ("CALIX-TRAP-MIB", "calixTrapCondState"),
        ("CALIX-TRAP-MIB", "calixTrapCondDescr"),
        ("CALIX-TRAP-MIB", "calixTrapLocation"),
        ("CALIX-TRAP-MIB", "calixTrapMonValue"),
        ("CALIX-TRAP-MIB", "calixTrapThLevel"),
        ("CALIX-TRAP-MIB", "calixTrapTmPeriod"),
        ("CALIX-TRAP-MIB", "calixTrapObjClass"),
        ("CALIX-TRAP-MIB", "calixTrapObjIndex"),
        ("CALIX-TRAP-MIB", "calixTrapSerialNr"))
)
if mibBuilder.loadTexts:
    calixTrapTCAEVENT.setStatus(
        "current"
    )

calixTrapRESTORE = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 3)
)
calixTrapRESTORE.setObjects(
      *(("CALIX-TRAP-MIB", "calixTrapTl1Aid"),
        ("CALIX-TRAP-MIB", "calixTrapObjState"),
        ("CALIX-TRAP-MIB", "calixTrapObjClass"),
        ("CALIX-TRAP-MIB", "calixTrapObjIndex"),
        ("CALIX-TRAP-MIB", "calixTrapSerialNr"))
)
if mibBuilder.loadTexts:
    calixTrapRESTORE.setStatus(
        "current"
    )

calixTrapREMOVE = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 4)
)
calixTrapREMOVE.setObjects(
      *(("CALIX-TRAP-MIB", "calixTrapTl1Aid"),
        ("CALIX-TRAP-MIB", "calixTrapObjState"),
        ("CALIX-TRAP-MIB", "calixTrapObjClass"),
        ("CALIX-TRAP-MIB", "calixTrapObjIndex"),
        ("CALIX-TRAP-MIB", "calixTrapSerialNr"))
)
if mibBuilder.loadTexts:
    calixTrapREMOVE.setStatus(
        "current"
    )

calixTrapEVENT = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 2, 3, 1, 5)
)
calixTrapEVENT.setObjects(
      *(("CALIX-TRAP-MIB", "calixTrapTl1Aid"),
        ("CALIX-TRAP-MIB", "calixTrapCondType"),
        ("CALIX-TRAP-MIB", "calixTrapCondState"),
        ("CALIX-TRAP-MIB", "calixTrapCondDescr"),
        ("CALIX-TRAP-MIB", "calixTrapLocation"),
        ("CALIX-TRAP-MIB", "calixTrapObjClass"),
        ("CALIX-TRAP-MIB", "calixTrapObjIndex"),
        ("CALIX-TRAP-MIB", "calixTrapSerialNr"))
)
if mibBuilder.loadTexts:
    calixTrapEVENT.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CALIX-TRAP-MIB",
    **{"calixTrap": calixTrap,
       "calixTrapMIB": calixTrapMIB,
       "calixTraps": calixTraps,
       "calixTrapALARM": calixTrapALARM,
       "calixTrapTCAEVENT": calixTrapTCAEVENT,
       "calixTrapRESTORE": calixTrapRESTORE,
       "calixTrapREMOVE": calixTrapREMOVE,
       "calixTrapEVENT": calixTrapEVENT,
       "calixTrapObjects": calixTrapObjects,
       "calixTrapObjClass": calixTrapObjClass,
       "calixTrapShelfId": calixTrapShelfId,
       "calixTrapTl1Aid": calixTrapTl1Aid,
       "calixTrapObjIndex": calixTrapObjIndex,
       "calixTrapObjState": calixTrapObjState,
       "calixTrapSerialNr": calixTrapSerialNr,
       "calixTrapAlarmTransition": calixTrapAlarmTransition,
       "calixTrapAlarmSeverity": calixTrapAlarmSeverity,
       "calixTrapAlarmType": calixTrapAlarmType,
       "calixTrapCondType": calixTrapCondType,
       "calixTrapSrvEffect": calixTrapSrvEffect,
       "calixTrapCondDescr": calixTrapCondDescr,
       "calixTrapMonValue": calixTrapMonValue,
       "calixTrapThLevel": calixTrapThLevel,
       "calixTrapTmPeriod": calixTrapTmPeriod,
       "calixTrapCondState": calixTrapCondState,
       "calixTrapLocation": calixTrapLocation,
       "calixTrapStbySlot": calixTrapStbySlot,
       "calixTrapIntfGroup": calixTrapIntfGroup,
       "calixTrapDLinkType": calixTrapDLinkType,
       "calixTrapStbyIntfGroup": calixTrapStbyIntfGroup,
       "calixTrapStbyDLinkType": calixTrapStbyDLinkType}
)
