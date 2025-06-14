# SNMP MIB module (E5-120-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/calix_6321/E5-120-TRAPS-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 17:40:54 2025
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

(iesChassisId,
 iesSlotId) = mibBuilder.importSymbols(
    "E5-120-IESCOMMON-MIB",
    "iesChassisId",
    "iesSlotId")

(e5x120,) = mibBuilder.importSymbols(
    "E5-120-MIB",
    "e5x120")

(dot1agCfmMdMdLevel,
 dot1agCfmMepIdentifier,
 dot1agCfmVlanPrimaryVid) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMdMdLevel",
    "dot1agCfmMepIdentifier",
    "dot1agCfmVlanPrimaryVid")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12)
)
_Object_ObjectIdentity = ObjectIdentity
object = _Object_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 1)
)
_EqptAlarmInputIndex_Type = Integer32
_EqptAlarmInputIndex_Object = MibScalar
eqptAlarmInputIndex = _EqptAlarmInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 1, 2),
    _EqptAlarmInputIndex_Type()
)
eqptAlarmInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptAlarmInputIndex.setStatus("current")
_EqptAlarmInputName_Type = DisplayString
_EqptAlarmInputName_Object = MibScalar
eqptAlarmInputName = _EqptAlarmInputName_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 1, 8),
    _EqptAlarmInputName_Type()
)
eqptAlarmInputName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptAlarmInputName.setStatus("current")
_SysMacAntiSpoofOrig_Type = Integer32
_SysMacAntiSpoofOrig_Object = MibScalar
sysMacAntiSpoofOrig = _SysMacAntiSpoofOrig_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 1, 9),
    _SysMacAntiSpoofOrig_Type()
)
sysMacAntiSpoofOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofOrig.setStatus("current")
_SysMacAntiSpoofNew_Type = Integer32
_SysMacAntiSpoofNew_Object = MibScalar
sysMacAntiSpoofNew = _SysMacAntiSpoofNew_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 1, 10),
    _SysMacAntiSpoofNew_Type()
)
sysMacAntiSpoofNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofNew.setStatus("current")
_SysMacAntiSpoofMAC_Type = DisplayString
_SysMacAntiSpoofMAC_Object = MibScalar
sysMacAntiSpoofMAC = _SysMacAntiSpoofMAC_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 1, 11),
    _SysMacAntiSpoofMAC_Type()
)
sysMacAntiSpoofMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacAntiSpoofMAC.setStatus("current")


class _SysAlarmOrigSeverity_Type(Integer32):
    """Custom type sysAlarmOrigSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("info", 4))
    )


_SysAlarmOrigSeverity_Type.__name__ = "Integer32"
_SysAlarmOrigSeverity_Object = MibScalar
sysAlarmOrigSeverity = _SysAlarmOrigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 1, 12),
    _SysAlarmOrigSeverity_Type()
)
sysAlarmOrigSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlarmOrigSeverity.setStatus("current")


class _SysAlarmNewSeverity_Type(Integer32):
    """Custom type sysAlarmNewSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("info", 4))
    )


_SysAlarmNewSeverity_Type.__name__ = "Integer32"
_SysAlarmNewSeverity_Object = MibScalar
sysAlarmNewSeverity = _SysAlarmNewSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 1, 13),
    _SysAlarmNewSeverity_Type()
)
sysAlarmNewSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlarmNewSeverity.setStatus("current")
_SysAlarmConfId_Type = Integer32
_SysAlarmConfId_Object = MibScalar
sysAlarmConfId = _SysAlarmConfId_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 1, 14),
    _SysAlarmConfId_Type()
)
sysAlarmConfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAlarmConfId.setStatus("current")


class _IntfCfmCcmErrorCause_Type(Integer32):
    """Custom type intfCfmCcmErrorCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noDefect", 1),
          ("rdiReceived", 2),
          ("macDownReceivedFromDownMEP", 3),
          ("lostConnectionToRemoteMEP", 4),
          ("configurationError", 5),
          ("maintenanceDomainCrossConnect", 6))
    )


_IntfCfmCcmErrorCause_Type.__name__ = "Integer32"
_IntfCfmCcmErrorCause_Object = MibScalar
intfCfmCcmErrorCause = _IntfCfmCcmErrorCause_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 1, 55),
    _IntfCfmCcmErrorCause_Type()
)
intfCfmCcmErrorCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intfCfmCcmErrorCause.setStatus("current")
_Equipment_ObjectIdentity = ObjectIdentity
equipment = _Equipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 3)
)
_Systrap_ObjectIdentity = ObjectIdentity
systrap = _Systrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 4)
)
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 8)
)
_E5Alarm_ObjectIdentity = ObjectIdentity
e5Alarm = _E5Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9)
)
_E5AlarmTable_Object = MibTable
e5AlarmTable = _E5AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1)
)
if mibBuilder.loadTexts:
    e5AlarmTable.setStatus("current")
_E5AlarmEntry_Object = MibTableRow
e5AlarmEntry = _E5AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1)
)
e5AlarmEntry.setIndexNames(
    (0, "E5-120-TRAPS-MIB", "e5AlarmObjectClass"),
    (0, "E5-120-TRAPS-MIB", "e5AlarmObjectInstance1"),
    (0, "E5-120-TRAPS-MIB", "e5AlarmObjectInstance2"),
    (0, "E5-120-TRAPS-MIB", "e5AlarmObjectInstance3"),
    (0, "E5-120-TRAPS-MIB", "e5AlarmObjectInstance4"),
    (0, "E5-120-TRAPS-MIB", "e5AlarmObjectInstance5"),
    (0, "E5-120-TRAPS-MIB", "e5AlarmObjectInstance6"),
    (0, "E5-120-TRAPS-MIB", "e5AlarmObjectInstance7"),
    (0, "E5-120-TRAPS-MIB", "e5AlarmObjectInstance8"),
    (0, "E5-120-TRAPS-MIB", "e5AlarmType"),
)
if mibBuilder.loadTexts:
    e5AlarmEntry.setStatus("current")


class _E5AlarmObjectClass_Type(Integer32):
    """Custom type e5AlarmObjectClass based on Integer32"""
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
        *(("dsl", 1),
          ("eqpt", 2),
          ("sys", 3),
          ("enet", 4),
          ("vop", 5),
          ("intf", 6),
          ("unknown", 7))
    )


_E5AlarmObjectClass_Type.__name__ = "Integer32"
_E5AlarmObjectClass_Object = MibTableColumn
e5AlarmObjectClass = _E5AlarmObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 1),
    _E5AlarmObjectClass_Type()
)
e5AlarmObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmObjectClass.setStatus("current")
_E5AlarmObjectInstance1_Type = Integer32
_E5AlarmObjectInstance1_Object = MibTableColumn
e5AlarmObjectInstance1 = _E5AlarmObjectInstance1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 2),
    _E5AlarmObjectInstance1_Type()
)
e5AlarmObjectInstance1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmObjectInstance1.setStatus("current")
_E5AlarmObjectInstance2_Type = Integer32
_E5AlarmObjectInstance2_Object = MibTableColumn
e5AlarmObjectInstance2 = _E5AlarmObjectInstance2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 3),
    _E5AlarmObjectInstance2_Type()
)
e5AlarmObjectInstance2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmObjectInstance2.setStatus("current")
_E5AlarmObjectInstance3_Type = Integer32
_E5AlarmObjectInstance3_Object = MibTableColumn
e5AlarmObjectInstance3 = _E5AlarmObjectInstance3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 4),
    _E5AlarmObjectInstance3_Type()
)
e5AlarmObjectInstance3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmObjectInstance3.setStatus("current")
_E5AlarmObjectInstance4_Type = Integer32
_E5AlarmObjectInstance4_Object = MibTableColumn
e5AlarmObjectInstance4 = _E5AlarmObjectInstance4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 5),
    _E5AlarmObjectInstance4_Type()
)
e5AlarmObjectInstance4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmObjectInstance4.setStatus("current")
_E5AlarmObjectInstance5_Type = Integer32
_E5AlarmObjectInstance5_Object = MibTableColumn
e5AlarmObjectInstance5 = _E5AlarmObjectInstance5_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 6),
    _E5AlarmObjectInstance5_Type()
)
e5AlarmObjectInstance5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmObjectInstance5.setStatus("current")
_E5AlarmObjectInstance6_Type = Integer32
_E5AlarmObjectInstance6_Object = MibTableColumn
e5AlarmObjectInstance6 = _E5AlarmObjectInstance6_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 7),
    _E5AlarmObjectInstance6_Type()
)
e5AlarmObjectInstance6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmObjectInstance6.setStatus("current")
_E5AlarmObjectInstance7_Type = Integer32
_E5AlarmObjectInstance7_Object = MibTableColumn
e5AlarmObjectInstance7 = _E5AlarmObjectInstance7_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 8),
    _E5AlarmObjectInstance7_Type()
)
e5AlarmObjectInstance7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmObjectInstance7.setStatus("current")
_E5AlarmObjectInstance8_Type = Integer32
_E5AlarmObjectInstance8_Object = MibTableColumn
e5AlarmObjectInstance8 = _E5AlarmObjectInstance8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 9),
    _E5AlarmObjectInstance8_Type()
)
e5AlarmObjectInstance8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmObjectInstance8.setStatus("current")
_E5AlarmType_Type = Integer32
_E5AlarmType_Object = MibTableColumn
e5AlarmType = _E5AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 10),
    _E5AlarmType_Type()
)
e5AlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmType.setStatus("current")


class _E5AlarmSeverity_Type(Integer32):
    """Custom type e5AlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("unknown", 5))
    )


_E5AlarmSeverity_Type.__name__ = "Integer32"
_E5AlarmSeverity_Object = MibTableColumn
e5AlarmSeverity = _E5AlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 11),
    _E5AlarmSeverity_Type()
)
e5AlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmSeverity.setStatus("current")


class _E5AlarmTimeStamp_Type(OctetString):
    """Custom type e5AlarmTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_E5AlarmTimeStamp_Type.__name__ = "OctetString"
_E5AlarmTimeStamp_Object = MibTableColumn
e5AlarmTimeStamp = _E5AlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 12),
    _E5AlarmTimeStamp_Type()
)
e5AlarmTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmTimeStamp.setStatus("current")


class _E5AlarmServiceAffecting_Type(Integer32):
    """Custom type e5AlarmServiceAffecting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_E5AlarmServiceAffecting_Type.__name__ = "Integer32"
_E5AlarmServiceAffecting_Object = MibTableColumn
e5AlarmServiceAffecting = _E5AlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 13),
    _E5AlarmServiceAffecting_Type()
)
e5AlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmServiceAffecting.setStatus("current")


class _E5AlarmLocationInfo_Type(Integer32):
    """Custom type e5AlarmLocationInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("nearEnd", 1)
    )


_E5AlarmLocationInfo_Type.__name__ = "Integer32"
_E5AlarmLocationInfo_Object = MibTableColumn
e5AlarmLocationInfo = _E5AlarmLocationInfo_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 14),
    _E5AlarmLocationInfo_Type()
)
e5AlarmLocationInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmLocationInfo.setStatus("current")
_E5AlarmText_Type = OctetString
_E5AlarmText_Object = MibTableColumn
e5AlarmText = _E5AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 15),
    _E5AlarmText_Type()
)
e5AlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmText.setStatus("current")
_E5AlarmTime_Type = Integer32
_E5AlarmTime_Object = MibTableColumn
e5AlarmTime = _E5AlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 16),
    _E5AlarmTime_Type()
)
e5AlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmTime.setStatus("current")
_E5AlarmCliObject_Type = OctetString
_E5AlarmCliObject_Object = MibTableColumn
e5AlarmCliObject = _E5AlarmCliObject_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 17),
    _E5AlarmCliObject_Type()
)
e5AlarmCliObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmCliObject.setStatus("current")
_E5AlarmSecObjectClass_Type = Integer32
_E5AlarmSecObjectClass_Object = MibTableColumn
e5AlarmSecObjectClass = _E5AlarmSecObjectClass_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 18),
    _E5AlarmSecObjectClass_Type()
)
e5AlarmSecObjectClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmSecObjectClass.setStatus("current")
_E5AlarmSecObjectInstance1_Type = Integer32
_E5AlarmSecObjectInstance1_Object = MibTableColumn
e5AlarmSecObjectInstance1 = _E5AlarmSecObjectInstance1_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 19),
    _E5AlarmSecObjectInstance1_Type()
)
e5AlarmSecObjectInstance1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmSecObjectInstance1.setStatus("current")
_E5AlarmSecObjectInstance2_Type = Integer32
_E5AlarmSecObjectInstance2_Object = MibTableColumn
e5AlarmSecObjectInstance2 = _E5AlarmSecObjectInstance2_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 20),
    _E5AlarmSecObjectInstance2_Type()
)
e5AlarmSecObjectInstance2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmSecObjectInstance2.setStatus("current")
_E5AlarmSecObjectInstance3_Type = Integer32
_E5AlarmSecObjectInstance3_Object = MibTableColumn
e5AlarmSecObjectInstance3 = _E5AlarmSecObjectInstance3_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 21),
    _E5AlarmSecObjectInstance3_Type()
)
e5AlarmSecObjectInstance3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmSecObjectInstance3.setStatus("current")
_E5AlarmSecObjectInstance4_Type = Integer32
_E5AlarmSecObjectInstance4_Object = MibTableColumn
e5AlarmSecObjectInstance4 = _E5AlarmSecObjectInstance4_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 22),
    _E5AlarmSecObjectInstance4_Type()
)
e5AlarmSecObjectInstance4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmSecObjectInstance4.setStatus("current")
_E5AlarmSecObjectInstance5_Type = Integer32
_E5AlarmSecObjectInstance5_Object = MibTableColumn
e5AlarmSecObjectInstance5 = _E5AlarmSecObjectInstance5_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 23),
    _E5AlarmSecObjectInstance5_Type()
)
e5AlarmSecObjectInstance5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmSecObjectInstance5.setStatus("current")
_E5AlarmSecObjectInstance6_Type = Integer32
_E5AlarmSecObjectInstance6_Object = MibTableColumn
e5AlarmSecObjectInstance6 = _E5AlarmSecObjectInstance6_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 24),
    _E5AlarmSecObjectInstance6_Type()
)
e5AlarmSecObjectInstance6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmSecObjectInstance6.setStatus("current")
_E5AlarmSecObjectInstance7_Type = Integer32
_E5AlarmSecObjectInstance7_Object = MibTableColumn
e5AlarmSecObjectInstance7 = _E5AlarmSecObjectInstance7_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 25),
    _E5AlarmSecObjectInstance7_Type()
)
e5AlarmSecObjectInstance7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmSecObjectInstance7.setStatus("current")
_E5AlarmSecObjectInstance8_Type = Integer32
_E5AlarmSecObjectInstance8_Object = MibTableColumn
e5AlarmSecObjectInstance8 = _E5AlarmSecObjectInstance8_Object(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 1, 1, 26),
    _E5AlarmSecObjectInstance8_Type()
)
e5AlarmSecObjectInstance8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    e5AlarmSecObjectInstance8.setStatus("current")

# Managed Objects groups


# Notification objects

eqptHWMonitorFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 3, 1)
)
if mibBuilder.loadTexts:
    eqptHWMonitorFailure.setStatus(
        "current"
    )

sysMacAntiSpoofing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 4, 1)
)
sysMacAntiSpoofing.setObjects(
      *(("E5-120-TRAPS-MIB", "sysMacAntiSpoofOrig"),
        ("E5-120-TRAPS-MIB", "sysMacAntiSpoofNew"),
        ("E5-120-TRAPS-MIB", "sysMacAntiSpoofMAC"))
)
if mibBuilder.loadTexts:
    sysMacAntiSpoofing.setStatus(
        "current"
    )

sysAlarmCutoffEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 4, 2)
)
if mibBuilder.loadTexts:
    sysAlarmCutoffEnable.setStatus(
        "current"
    )

sysAlarmClearEnable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 4, 3)
)
if mibBuilder.loadTexts:
    sysAlarmClearEnable.setStatus(
        "current"
    )

sysLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 4, 4)
)
if mibBuilder.loadTexts:
    sysLoginFailure.setStatus(
        "current"
    )

sysAlarmSvrtyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 4, 5)
)
if mibBuilder.loadTexts:
    sysAlarmSvrtyChange.setStatus(
        "current"
    )

cfmCcmError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 8, 1)
)
cfmCcmError.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMdMdLevel"),
        ("IEEE8021-CFM-MIB", "dot1agCfmVlanPrimaryVid"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
        ("E5-120-TRAPS-MIB", "intfCfmCcmErrorCause"))
)
if mibBuilder.loadTexts:
    cfmCcmError.setStatus(
        "current"
    )

e5AlarmNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 6321, 1, 2, 3, 3, 12, 9, 2)
)
e5AlarmNotify.setObjects(
      *(("E5-120-TRAPS-MIB", "e5AlarmObjectClass"),
        ("E5-120-TRAPS-MIB", "e5AlarmObjectInstance1"),
        ("E5-120-TRAPS-MIB", "e5AlarmObjectInstance2"),
        ("E5-120-TRAPS-MIB", "e5AlarmObjectInstance3"),
        ("E5-120-TRAPS-MIB", "e5AlarmObjectInstance4"),
        ("E5-120-TRAPS-MIB", "e5AlarmType"),
        ("E5-120-TRAPS-MIB", "e5AlarmSeverity"),
        ("E5-120-TRAPS-MIB", "e5AlarmTimeStamp"),
        ("E5-120-TRAPS-MIB", "e5AlarmServiceAffecting"),
        ("E5-120-TRAPS-MIB", "e5AlarmText"),
        ("E5-120-TRAPS-MIB", "e5AlarmTime"))
)
if mibBuilder.loadTexts:
    e5AlarmNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "E5-120-TRAPS-MIB",
    **{"trap": trap,
       "object": object,
       "eqptAlarmInputIndex": eqptAlarmInputIndex,
       "eqptAlarmInputName": eqptAlarmInputName,
       "sysMacAntiSpoofOrig": sysMacAntiSpoofOrig,
       "sysMacAntiSpoofNew": sysMacAntiSpoofNew,
       "sysMacAntiSpoofMAC": sysMacAntiSpoofMAC,
       "sysAlarmOrigSeverity": sysAlarmOrigSeverity,
       "sysAlarmNewSeverity": sysAlarmNewSeverity,
       "sysAlarmConfId": sysAlarmConfId,
       "intfCfmCcmErrorCause": intfCfmCcmErrorCause,
       "equipment": equipment,
       "eqptHWMonitorFailure": eqptHWMonitorFailure,
       "systrap": systrap,
       "sysMacAntiSpoofing": sysMacAntiSpoofing,
       "sysAlarmCutoffEnable": sysAlarmCutoffEnable,
       "sysAlarmClearEnable": sysAlarmClearEnable,
       "sysLoginFailure": sysLoginFailure,
       "sysAlarmSvrtyChange": sysAlarmSvrtyChange,
       "interface": interface,
       "cfmCcmError": cfmCcmError,
       "e5Alarm": e5Alarm,
       "e5AlarmTable": e5AlarmTable,
       "e5AlarmEntry": e5AlarmEntry,
       "e5AlarmObjectClass": e5AlarmObjectClass,
       "e5AlarmObjectInstance1": e5AlarmObjectInstance1,
       "e5AlarmObjectInstance2": e5AlarmObjectInstance2,
       "e5AlarmObjectInstance3": e5AlarmObjectInstance3,
       "e5AlarmObjectInstance4": e5AlarmObjectInstance4,
       "e5AlarmObjectInstance5": e5AlarmObjectInstance5,
       "e5AlarmObjectInstance6": e5AlarmObjectInstance6,
       "e5AlarmObjectInstance7": e5AlarmObjectInstance7,
       "e5AlarmObjectInstance8": e5AlarmObjectInstance8,
       "e5AlarmType": e5AlarmType,
       "e5AlarmSeverity": e5AlarmSeverity,
       "e5AlarmTimeStamp": e5AlarmTimeStamp,
       "e5AlarmServiceAffecting": e5AlarmServiceAffecting,
       "e5AlarmLocationInfo": e5AlarmLocationInfo,
       "e5AlarmText": e5AlarmText,
       "e5AlarmTime": e5AlarmTime,
       "e5AlarmCliObject": e5AlarmCliObject,
       "e5AlarmSecObjectClass": e5AlarmSecObjectClass,
       "e5AlarmSecObjectInstance1": e5AlarmSecObjectInstance1,
       "e5AlarmSecObjectInstance2": e5AlarmSecObjectInstance2,
       "e5AlarmSecObjectInstance3": e5AlarmSecObjectInstance3,
       "e5AlarmSecObjectInstance4": e5AlarmSecObjectInstance4,
       "e5AlarmSecObjectInstance5": e5AlarmSecObjectInstance5,
       "e5AlarmSecObjectInstance6": e5AlarmSecObjectInstance6,
       "e5AlarmSecObjectInstance7": e5AlarmSecObjectInstance7,
       "e5AlarmSecObjectInstance8": e5AlarmSecObjectInstance8,
       "e5AlarmNotify": e5AlarmNotify}
)
