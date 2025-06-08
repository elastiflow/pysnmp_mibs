# SNMP MIB module (TIMETRA-CHASSIS-INTERCONNECT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nokia_6527/TIMETRA-CHASSIS-INTERCONNECT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 17:45:14 2025
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(TmnxSlotNum,
 tmnxChassisIndex,
 tmnxChassisNotifyCpmCardSlotNum,
 tmnxChassisNotifyFabricSlotNum,
 tmnxCpmCardSlotNum,
 tmnxFabricSlotNum,
 tmnxHwClass) = mibBuilder.importSymbols(
    "TIMETRA-CHASSIS-MIB",
    "TmnxSlotNum",
    "tmnxChassisIndex",
    "tmnxChassisNotifyCpmCardSlotNum",
    "tmnxChassisNotifyFabricSlotNum",
    "tmnxCpmCardSlotNum",
    "tmnxFabricSlotNum",
    "tmnxHwClass")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TmnxSFFStatus,
 tmnxDDMFailedObject,
 tmnxDDMLaneIdOrModule) = mibBuilder.importSymbols(
    "TIMETRA-PORT-MIB",
    "TmnxSFFStatus",
    "tmnxDDMFailedObject",
    "tmnxDDMLaneIdOrModule")


# MODULE-IDENTITY

timetraChassisInterconMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 94)
)
if mibBuilder.loadTexts:
    timetraChassisInterconMIBModule.setRevisions(
        ("2013-10-31 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxIcPortState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("invalidConnection", 2),
          ("noLink", 3),
          ("indeterminate", 4),
          ("unsupportedSff", 5))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxChassisInterconConformance_ObjectIdentity = ObjectIdentity
tmnxChassisInterconConformance = _TmnxChassisInterconConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 94)
)
_TmnxChassisInterconCompliances_ObjectIdentity = ObjectIdentity
tmnxChassisInterconCompliances = _TmnxChassisInterconCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 94, 1)
)
_TmnxChassisInterconGroups_ObjectIdentity = ObjectIdentity
tmnxChassisInterconGroups = _TmnxChassisInterconGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 94, 2)
)
_TmnxChassIcV12v0Groups_ObjectIdentity = ObjectIdentity
tmnxChassIcV12v0Groups = _TmnxChassIcV12v0Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 94, 2, 1)
)
_TmnxChassisInterconObjs_ObjectIdentity = ObjectIdentity
tmnxChassisInterconObjs = _TmnxChassisInterconObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94)
)
_TmnxIcPortObjs_ObjectIdentity = ObjectIdentity
tmnxIcPortObjs = _TmnxIcPortObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1)
)
_TmnxCpmIcPortTable_Object = MibTable
tmnxCpmIcPortTable = _TmnxCpmIcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxCpmIcPortTable.setStatus("current")
_TmnxCpmIcPortEntry_Object = MibTableRow
tmnxCpmIcPortEntry = _TmnxCpmIcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 1, 1)
)
tmnxCpmIcPortEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxCpmCardSlotNum"),
    (0, "TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortNum"),
)
if mibBuilder.loadTexts:
    tmnxCpmIcPortEntry.setStatus("current")


class _TmnxCpmIcPortNum_Type(Unsigned32):
    """Custom type tmnxCpmIcPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TmnxCpmIcPortNum_Type.__name__ = "Unsigned32"
_TmnxCpmIcPortNum_Object = MibTableColumn
tmnxCpmIcPortNum = _TmnxCpmIcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 1, 1, 1),
    _TmnxCpmIcPortNum_Type()
)
tmnxCpmIcPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxCpmIcPortNum.setStatus("current")
_TmnxCpmIcPortOperState_Type = TmnxIcPortState
_TmnxCpmIcPortOperState_Object = MibTableColumn
tmnxCpmIcPortOperState = _TmnxCpmIcPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 1, 1, 2),
    _TmnxCpmIcPortOperState_Type()
)
tmnxCpmIcPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmIcPortOperState.setStatus("current")
_TmnxCpmIcPortSFFEquipped_Type = TruthValue
_TmnxCpmIcPortSFFEquipped_Object = MibTableColumn
tmnxCpmIcPortSFFEquipped = _TmnxCpmIcPortSFFEquipped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 1, 1, 3),
    _TmnxCpmIcPortSFFEquipped_Type()
)
tmnxCpmIcPortSFFEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmIcPortSFFEquipped.setStatus("current")
_TmnxCpmIcPortSFFStatus_Type = TmnxSFFStatus
_TmnxCpmIcPortSFFStatus_Object = MibTableColumn
tmnxCpmIcPortSFFStatus = _TmnxCpmIcPortSFFStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 1, 1, 4),
    _TmnxCpmIcPortSFFStatus_Type()
)
tmnxCpmIcPortSFFStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxCpmIcPortSFFStatus.setStatus("current")
_TmnxSfmIcPortTable_Object = MibTable
tmnxSfmIcPortTable = _TmnxSfmIcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 2)
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortTable.setStatus("current")
_TmnxSfmIcPortEntry_Object = MibTableRow
tmnxSfmIcPortEntry = _TmnxSfmIcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 2, 1)
)
tmnxSfmIcPortEntry.setIndexNames(
    (0, "TIMETRA-CHASSIS-MIB", "tmnxChassisIndex"),
    (0, "TIMETRA-CHASSIS-MIB", "tmnxFabricSlotNum"),
    (0, "TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortNum"),
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortEntry.setStatus("current")


class _TmnxSfmIcPortNum_Type(Unsigned32):
    """Custom type tmnxSfmIcPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_TmnxSfmIcPortNum_Type.__name__ = "Unsigned32"
_TmnxSfmIcPortNum_Object = MibTableColumn
tmnxSfmIcPortNum = _TmnxSfmIcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 2, 1, 1),
    _TmnxSfmIcPortNum_Type()
)
tmnxSfmIcPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSfmIcPortNum.setStatus("current")
_TmnxSfmIcPortOperState_Type = TmnxIcPortState
_TmnxSfmIcPortOperState_Object = MibTableColumn
tmnxSfmIcPortOperState = _TmnxSfmIcPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 2, 1, 2),
    _TmnxSfmIcPortOperState_Type()
)
tmnxSfmIcPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSfmIcPortOperState.setStatus("current")
_TmnxSfmIcPortSFFEquipped_Type = TruthValue
_TmnxSfmIcPortSFFEquipped_Object = MibTableColumn
tmnxSfmIcPortSFFEquipped = _TmnxSfmIcPortSFFEquipped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 2, 1, 3),
    _TmnxSfmIcPortSFFEquipped_Type()
)
tmnxSfmIcPortSFFEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSfmIcPortSFFEquipped.setStatus("current")
_TmnxSfmIcPortSFFStatus_Type = TmnxSFFStatus
_TmnxSfmIcPortSFFStatus_Object = MibTableColumn
tmnxSfmIcPortSFFStatus = _TmnxSfmIcPortSFFStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 2, 1, 4),
    _TmnxSfmIcPortSFFStatus_Type()
)
tmnxSfmIcPortSFFStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSfmIcPortSFFStatus.setStatus("current")


class _TmnxSfmIcPortDegradeState_Type(Integer32):
    """Custom type tmnxSfmIcPortDegradeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("degraded", 2))
    )


_TmnxSfmIcPortDegradeState_Type.__name__ = "Integer32"
_TmnxSfmIcPortDegradeState_Object = MibTableColumn
tmnxSfmIcPortDegradeState = _TmnxSfmIcPortDegradeState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 2, 1, 5),
    _TmnxSfmIcPortDegradeState_Type()
)
tmnxSfmIcPortDegradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSfmIcPortDegradeState.setStatus("current")
_TmnxSfmIcPortMisconSfm_Type = Unsigned32
_TmnxSfmIcPortMisconSfm_Object = MibTableColumn
tmnxSfmIcPortMisconSfm = _TmnxSfmIcPortMisconSfm_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 2, 1, 6),
    _TmnxSfmIcPortMisconSfm_Type()
)
tmnxSfmIcPortMisconSfm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSfmIcPortMisconSfm.setStatus("current")
_TmnxSfmIcPortMisconSfmIcPort_Type = Unsigned32
_TmnxSfmIcPortMisconSfmIcPort_Object = MibTableColumn
tmnxSfmIcPortMisconSfmIcPort = _TmnxSfmIcPortMisconSfmIcPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 1, 2, 1, 7),
    _TmnxSfmIcPortMisconSfmIcPort_Type()
)
tmnxSfmIcPortMisconSfmIcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSfmIcPortMisconSfmIcPort.setStatus("current")
_TmnxChassIcNotifObjs_ObjectIdentity = ObjectIdentity
tmnxChassIcNotifObjs = _TmnxChassIcNotifObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 2)
)
_TmnxNotifyIcPortNum_Type = Unsigned32
_TmnxNotifyIcPortNum_Object = MibScalar
tmnxNotifyIcPortNum = _TmnxNotifyIcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 94, 2, 1),
    _TmnxNotifyIcPortNum_Type()
)
tmnxNotifyIcPortNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxNotifyIcPortNum.setStatus("current")
_TmnxChassisInterconNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxChassisInterconNotifyPrefix = _TmnxChassisInterconNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94)
)
_TmnxChassisInterconNotification_ObjectIdentity = ObjectIdentity
tmnxChassisInterconNotification = _TmnxChassisInterconNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0)
)
_TmnxInterChassisNotifications_ObjectIdentity = ObjectIdentity
tmnxInterChassisNotifications = _TmnxInterChassisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 1)
)
_TmnxCpmIcPortNotifications_ObjectIdentity = ObjectIdentity
tmnxCpmIcPortNotifications = _TmnxCpmIcPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 2)
)
_TmnxSfmIcPortNotifications_ObjectIdentity = ObjectIdentity
tmnxSfmIcPortNotifications = _TmnxSfmIcPortNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 3)
)

# Managed Objects groups

tmnxChassIcNotifyObjsV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 94, 2, 1, 2)
)
tmnxChassIcNotifyObjsV12v0Group.setObjects(
    ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxNotifyIcPortNum")
)
if mibBuilder.loadTexts:
    tmnxChassIcNotifyObjsV12v0Group.setStatus("current")

tmnxCpmIcPortV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 94, 2, 1, 3)
)
tmnxCpmIcPortV12v0Group.setObjects(
      *(("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortOperState"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortSFFEquipped"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortSFFStatus"))
)
if mibBuilder.loadTexts:
    tmnxCpmIcPortV12v0Group.setStatus("current")

tmnxSfmIcPortV12v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 94, 2, 1, 5)
)
tmnxSfmIcPortV12v0Group.setObjects(
      *(("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortOperState"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortSFFEquipped"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortSFFStatus"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortDegradeState"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortMisconSfm"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortMisconSfmIcPort"))
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortV12v0Group.setStatus("current")


# Notification objects

tmnxInterChassisCommsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 1, 1)
)
tmnxInterChassisCommsDown.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxInterChassisCommsDown.setStatus(
        "current"
    )

tmnxInterChassisCommsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 1, 2)
)
tmnxInterChassisCommsUp.setObjects(
    ("TIMETRA-CHASSIS-MIB", "tmnxHwClass")
)
if mibBuilder.loadTexts:
    tmnxInterChassisCommsUp.setStatus(
        "current"
    )

tmnxCpmIcPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 2, 1)
)
tmnxCpmIcPortDown.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortOperState"))
)
if mibBuilder.loadTexts:
    tmnxCpmIcPortDown.setStatus(
        "current"
    )

tmnxCpmIcPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 2, 2)
)
tmnxCpmIcPortUp.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortOperState"))
)
if mibBuilder.loadTexts:
    tmnxCpmIcPortUp.setStatus(
        "current"
    )

tmnxCpmIcPortSFFInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 2, 3)
)
tmnxCpmIcPortSFFInserted.setObjects(
    ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortSFFEquipped")
)
if mibBuilder.loadTexts:
    tmnxCpmIcPortSFFInserted.setStatus(
        "current"
    )

tmnxCpmIcPortSFFRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 2, 4)
)
tmnxCpmIcPortSFFRemoved.setObjects(
    ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortSFFEquipped")
)
if mibBuilder.loadTexts:
    tmnxCpmIcPortSFFRemoved.setStatus(
        "current"
    )

tmnxCpmNoLocalIcPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 2, 5)
)
tmnxCpmNoLocalIcPort.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCpmCardSlotNum"))
)
if mibBuilder.loadTexts:
    tmnxCpmNoLocalIcPort.setStatus(
        "current"
    )

tmnxCpmLocalIcPortAvail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 2, 6)
)
tmnxCpmLocalIcPortAvail.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCpmCardSlotNum"))
)
if mibBuilder.loadTexts:
    tmnxCpmLocalIcPortAvail.setStatus(
        "current"
    )

tmnxCpmIcPortSFFStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 2, 7)
)
tmnxCpmIcPortSFFStatusFailure.setObjects(
    ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortSFFStatus")
)
if mibBuilder.loadTexts:
    tmnxCpmIcPortSFFStatusFailure.setStatus(
        "current"
    )

tmnxCpmIcPortDDMFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 2, 8)
)
tmnxCpmIcPortDDMFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCpmCardSlotNum"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxNotifyIcPortNum"),
        ("TIMETRA-PORT-MIB", "tmnxDDMFailedObject"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneIdOrModule"))
)
if mibBuilder.loadTexts:
    tmnxCpmIcPortDDMFailure.setStatus(
        "current"
    )

tmnxCpmIcPortDDMClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 2, 9)
)
tmnxCpmIcPortDDMClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyCpmCardSlotNum"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxNotifyIcPortNum"),
        ("TIMETRA-PORT-MIB", "tmnxDDMFailedObject"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneIdOrModule"))
)
if mibBuilder.loadTexts:
    tmnxCpmIcPortDDMClear.setStatus(
        "current"
    )

tmnxSfmIcPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 3, 1)
)
tmnxSfmIcPortDown.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortOperState"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortMisconSfm"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortMisconSfmIcPort"))
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortDown.setStatus(
        "current"
    )

tmnxSfmIcPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 3, 2)
)
tmnxSfmIcPortUp.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxHwClass"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortOperState"))
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortUp.setStatus(
        "current"
    )

tmnxSfmIcPortSFFInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 3, 3)
)
tmnxSfmIcPortSFFInserted.setObjects(
    ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortSFFEquipped")
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortSFFInserted.setStatus(
        "current"
    )

tmnxSfmIcPortSFFRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 3, 4)
)
tmnxSfmIcPortSFFRemoved.setObjects(
    ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortSFFEquipped")
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortSFFRemoved.setStatus(
        "current"
    )

tmnxSfmIcPortSFFStatusFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 3, 5)
)
tmnxSfmIcPortSFFStatusFailure.setObjects(
    ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortSFFStatus")
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortSFFStatusFailure.setStatus(
        "current"
    )

tmnxSfmIcPortDDMFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 3, 6)
)
tmnxSfmIcPortDDMFailure.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyFabricSlotNum"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxNotifyIcPortNum"),
        ("TIMETRA-PORT-MIB", "tmnxDDMFailedObject"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneIdOrModule"))
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortDDMFailure.setStatus(
        "current"
    )

tmnxSfmIcPortDDMClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 3, 7)
)
tmnxSfmIcPortDDMClear.setObjects(
      *(("TIMETRA-CHASSIS-MIB", "tmnxChassisNotifyFabricSlotNum"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxNotifyIcPortNum"),
        ("TIMETRA-PORT-MIB", "tmnxDDMFailedObject"),
        ("TIMETRA-PORT-MIB", "tmnxDDMLaneIdOrModule"))
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortDDMClear.setStatus(
        "current"
    )

tmnxSfmIcPortDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 3, 8)
)
tmnxSfmIcPortDegraded.setObjects(
    ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortDegradeState")
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortDegraded.setStatus(
        "current"
    )

tmnxSfmIcPortDegradedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 94, 0, 3, 9)
)
tmnxSfmIcPortDegradedClear.setObjects(
    ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortDegradeState")
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortDegradedClear.setStatus(
        "current"
    )


# Notifications groups

tmnxChassIcNotifV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 94, 2, 1, 1)
)
tmnxChassIcNotifV12v0Group.setObjects(
      *(("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxInterChassisCommsDown"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxInterChassisCommsUp"))
)
if mibBuilder.loadTexts:
    tmnxChassIcNotifV12v0Group.setStatus(
        "current"
    )

tmnxCpmIcPortNotifV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 94, 2, 1, 4)
)
tmnxCpmIcPortNotifV12v0Group.setObjects(
      *(("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortDown"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortUp"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortSFFInserted"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortSFFRemoved"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmNoLocalIcPort"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmLocalIcPortAvail"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortSFFStatusFailure"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortDDMFailure"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortDDMClear"))
)
if mibBuilder.loadTexts:
    tmnxCpmIcPortNotifV12v0Group.setStatus(
        "current"
    )

tmnxSfmIcPortNotifV12v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 94, 2, 1, 6)
)
tmnxSfmIcPortNotifV12v0Group.setObjects(
      *(("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortDown"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortUp"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortSFFInserted"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortSFFRemoved"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortSFFStatusFailure"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortDDMFailure"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortDDMClear"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortDegraded"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortDegradedClear"))
)
if mibBuilder.loadTexts:
    tmnxSfmIcPortNotifV12v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxChassisInterconCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 94, 1, 1)
)
tmnxChassisInterconCompliance.setObjects(
      *(("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxChassIcNotifV12v0Group"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxChassIcNotifyObjsV12v0Group"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortV12v0Group"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxCpmIcPortNotifV12v0Group"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortV12v0Group"),
        ("TIMETRA-CHASSIS-INTERCONNECT-MIB", "tmnxSfmIcPortNotifV12v0Group"))
)
if mibBuilder.loadTexts:
    tmnxChassisInterconCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-CHASSIS-INTERCONNECT-MIB",
    **{"TmnxIcPortState": TmnxIcPortState,
       "timetraChassisInterconMIBModule": timetraChassisInterconMIBModule,
       "tmnxChassisInterconConformance": tmnxChassisInterconConformance,
       "tmnxChassisInterconCompliances": tmnxChassisInterconCompliances,
       "tmnxChassisInterconCompliance": tmnxChassisInterconCompliance,
       "tmnxChassisInterconGroups": tmnxChassisInterconGroups,
       "tmnxChassIcV12v0Groups": tmnxChassIcV12v0Groups,
       "tmnxChassIcNotifV12v0Group": tmnxChassIcNotifV12v0Group,
       "tmnxChassIcNotifyObjsV12v0Group": tmnxChassIcNotifyObjsV12v0Group,
       "tmnxCpmIcPortV12v0Group": tmnxCpmIcPortV12v0Group,
       "tmnxCpmIcPortNotifV12v0Group": tmnxCpmIcPortNotifV12v0Group,
       "tmnxSfmIcPortV12v0Group": tmnxSfmIcPortV12v0Group,
       "tmnxSfmIcPortNotifV12v0Group": tmnxSfmIcPortNotifV12v0Group,
       "tmnxChassisInterconObjs": tmnxChassisInterconObjs,
       "tmnxIcPortObjs": tmnxIcPortObjs,
       "tmnxCpmIcPortTable": tmnxCpmIcPortTable,
       "tmnxCpmIcPortEntry": tmnxCpmIcPortEntry,
       "tmnxCpmIcPortNum": tmnxCpmIcPortNum,
       "tmnxCpmIcPortOperState": tmnxCpmIcPortOperState,
       "tmnxCpmIcPortSFFEquipped": tmnxCpmIcPortSFFEquipped,
       "tmnxCpmIcPortSFFStatus": tmnxCpmIcPortSFFStatus,
       "tmnxSfmIcPortTable": tmnxSfmIcPortTable,
       "tmnxSfmIcPortEntry": tmnxSfmIcPortEntry,
       "tmnxSfmIcPortNum": tmnxSfmIcPortNum,
       "tmnxSfmIcPortOperState": tmnxSfmIcPortOperState,
       "tmnxSfmIcPortSFFEquipped": tmnxSfmIcPortSFFEquipped,
       "tmnxSfmIcPortSFFStatus": tmnxSfmIcPortSFFStatus,
       "tmnxSfmIcPortDegradeState": tmnxSfmIcPortDegradeState,
       "tmnxSfmIcPortMisconSfm": tmnxSfmIcPortMisconSfm,
       "tmnxSfmIcPortMisconSfmIcPort": tmnxSfmIcPortMisconSfmIcPort,
       "tmnxChassIcNotifObjs": tmnxChassIcNotifObjs,
       "tmnxNotifyIcPortNum": tmnxNotifyIcPortNum,
       "tmnxChassisInterconNotifyPrefix": tmnxChassisInterconNotifyPrefix,
       "tmnxChassisInterconNotification": tmnxChassisInterconNotification,
       "tmnxInterChassisNotifications": tmnxInterChassisNotifications,
       "tmnxInterChassisCommsDown": tmnxInterChassisCommsDown,
       "tmnxInterChassisCommsUp": tmnxInterChassisCommsUp,
       "tmnxCpmIcPortNotifications": tmnxCpmIcPortNotifications,
       "tmnxCpmIcPortDown": tmnxCpmIcPortDown,
       "tmnxCpmIcPortUp": tmnxCpmIcPortUp,
       "tmnxCpmIcPortSFFInserted": tmnxCpmIcPortSFFInserted,
       "tmnxCpmIcPortSFFRemoved": tmnxCpmIcPortSFFRemoved,
       "tmnxCpmNoLocalIcPort": tmnxCpmNoLocalIcPort,
       "tmnxCpmLocalIcPortAvail": tmnxCpmLocalIcPortAvail,
       "tmnxCpmIcPortSFFStatusFailure": tmnxCpmIcPortSFFStatusFailure,
       "tmnxCpmIcPortDDMFailure": tmnxCpmIcPortDDMFailure,
       "tmnxCpmIcPortDDMClear": tmnxCpmIcPortDDMClear,
       "tmnxSfmIcPortNotifications": tmnxSfmIcPortNotifications,
       "tmnxSfmIcPortDown": tmnxSfmIcPortDown,
       "tmnxSfmIcPortUp": tmnxSfmIcPortUp,
       "tmnxSfmIcPortSFFInserted": tmnxSfmIcPortSFFInserted,
       "tmnxSfmIcPortSFFRemoved": tmnxSfmIcPortSFFRemoved,
       "tmnxSfmIcPortSFFStatusFailure": tmnxSfmIcPortSFFStatusFailure,
       "tmnxSfmIcPortDDMFailure": tmnxSfmIcPortDDMFailure,
       "tmnxSfmIcPortDDMClear": tmnxSfmIcPortDDMClear,
       "tmnxSfmIcPortDegraded": tmnxSfmIcPortDegraded,
       "tmnxSfmIcPortDegradedClear": tmnxSfmIcPortDegradedClear}
)
