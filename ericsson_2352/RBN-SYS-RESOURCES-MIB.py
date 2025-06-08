# SNMP MIB module (RBN-SYS-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-SYS-RESOURCES-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:32 2025
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

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

(RbnAlarmId,) = mibBuilder.importSymbols(
    "RBN-ALARM-TC",
    "RbnAlarmId")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnKBytes,
 RbnPercentage,
 RbnSlot) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnKBytes",
    "RbnPercentage",
    "RbnSlot")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnSysResourcesMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24)
)
if mibBuilder.loadTexts:
    rbnSysResourcesMib.setRevisions(
        ("2011-04-29 18:00",
         "2011-01-19 18:00",
         "2009-07-16 00:00",
         "2007-05-29 00:00",
         "2005-04-18 00:00",
         "2003-09-02 18:00",
         "2002-10-10 00:00",
         "2002-06-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnSRMIBNotifications_ObjectIdentity = ObjectIdentity
rbnSRMIBNotifications = _RbnSRMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0)
)
_RbnSRMIBObjects_ObjectIdentity = ObjectIdentity
rbnSRMIBObjects = _RbnSRMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1)
)
_RbnSRProcess_ObjectIdentity = ObjectIdentity
rbnSRProcess = _RbnSRProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 1)
)
_RbnSRProcessNotifyLastUpdate_Type = TimeTicks
_RbnSRProcessNotifyLastUpdate_Object = MibScalar
rbnSRProcessNotifyLastUpdate = _RbnSRProcessNotifyLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 1, 1),
    _RbnSRProcessNotifyLastUpdate_Type()
)
rbnSRProcessNotifyLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRProcessNotifyLastUpdate.setStatus("current")


class _RbnSRProcessEventNotifyEnable_Type(Integer32):
    """Custom type rbnSRProcessEventNotifyEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_RbnSRProcessEventNotifyEnable_Type.__name__ = "Integer32"
_RbnSRProcessEventNotifyEnable_Object = MibScalar
rbnSRProcessEventNotifyEnable = _RbnSRProcessEventNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 1, 2),
    _RbnSRProcessEventNotifyEnable_Type()
)
rbnSRProcessEventNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSRProcessEventNotifyEnable.setStatus("current")
_RbnSRProcessNotifyTable_Object = MibTable
rbnSRProcessNotifyTable = _RbnSRProcessNotifyTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rbnSRProcessNotifyTable.setStatus("current")
_RbnSRProcessNotifyEntry_Object = MibTableRow
rbnSRProcessNotifyEntry = _RbnSRProcessNotifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 1, 3, 1)
)
rbnSRProcessNotifyEntry.setIndexNames(
    (0, "RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyProcName"),
)
if mibBuilder.loadTexts:
    rbnSRProcessNotifyEntry.setStatus("current")


class _RbnSRProcessNotifyProcName_Type(SnmpAdminString):
    """Custom type rbnSRProcessNotifyProcName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RbnSRProcessNotifyProcName_Type.__name__ = "SnmpAdminString"
_RbnSRProcessNotifyProcName_Object = MibTableColumn
rbnSRProcessNotifyProcName = _RbnSRProcessNotifyProcName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 1, 3, 1, 1),
    _RbnSRProcessNotifyProcName_Type()
)
rbnSRProcessNotifyProcName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSRProcessNotifyProcName.setStatus("current")


class _RbnSRProcessNotifyPID_Type(Unsigned32):
    """Custom type rbnSRProcessNotifyPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RbnSRProcessNotifyPID_Type.__name__ = "Unsigned32"
_RbnSRProcessNotifyPID_Object = MibTableColumn
rbnSRProcessNotifyPID = _RbnSRProcessNotifyPID_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 1, 3, 1, 2),
    _RbnSRProcessNotifyPID_Type()
)
rbnSRProcessNotifyPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRProcessNotifyPID.setStatus("current")


class _RbnSRProcessNotifyEventCause_Type(Integer32):
    """Custom type rbnSRProcessNotifyEventCause based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34)
        )
    )
    namedValues = NamedValues(
        *(("firstStart", 1),
          ("hangup", 2),
          ("interrupt", 3),
          ("quit", 4),
          ("illegalInstruction", 5),
          ("traceTrap", 6),
          ("abort", 7),
          ("emt", 8),
          ("floatingPointException", 9),
          ("kill", 10),
          ("busError", 11),
          ("segmentFault", 12),
          ("systemCallError", 13),
          ("pipeError", 14),
          ("alarmClock", 15),
          ("softwareTermination", 16),
          ("urgentConditionOnIOChannel", 17),
          ("stopNotFromTty", 18),
          ("stopFromTty", 19),
          ("continueStopped", 20),
          ("childExit", 21),
          ("ttyInput", 22),
          ("ttyOutput", 23),
          ("inputOutput", 24),
          ("exceededCpuTime", 25),
          ("exceededFileSize", 26),
          ("virtualAlarm", 27),
          ("profilingAlarm", 28),
          ("windowResize", 29),
          ("infoRequest", 30),
          ("userDefined1", 31),
          ("userDefined2", 32),
          ("powerFailRestart", 33),
          ("unknown", 34))
    )


_RbnSRProcessNotifyEventCause_Type.__name__ = "Integer32"
_RbnSRProcessNotifyEventCause_Object = MibTableColumn
rbnSRProcessNotifyEventCause = _RbnSRProcessNotifyEventCause_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 1, 3, 1, 3),
    _RbnSRProcessNotifyEventCause_Type()
)
rbnSRProcessNotifyEventCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRProcessNotifyEventCause.setStatus("current")


class _RbnSRProcessNotifyEventType_Type(Integer32):
    """Custom type rbnSRProcessNotifyEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("death", 1),
          ("birth", 2))
    )


_RbnSRProcessNotifyEventType_Type.__name__ = "Integer32"
_RbnSRProcessNotifyEventType_Object = MibTableColumn
rbnSRProcessNotifyEventType = _RbnSRProcessNotifyEventType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 1, 3, 1, 4),
    _RbnSRProcessNotifyEventType_Type()
)
rbnSRProcessNotifyEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRProcessNotifyEventType.setStatus("current")


class _RbnSRProcessNumOfSpawn_Type(Unsigned32):
    """Custom type rbnSRProcessNumOfSpawn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RbnSRProcessNumOfSpawn_Type.__name__ = "Unsigned32"
_RbnSRProcessNumOfSpawn_Object = MibTableColumn
rbnSRProcessNumOfSpawn = _RbnSRProcessNumOfSpawn_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 1, 3, 1, 5),
    _RbnSRProcessNumOfSpawn_Type()
)
rbnSRProcessNumOfSpawn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRProcessNumOfSpawn.setStatus("current")
_RbnSRProcessNotifyLastTimeSent_Type = TimeTicks
_RbnSRProcessNotifyLastTimeSent_Object = MibTableColumn
rbnSRProcessNotifyLastTimeSent = _RbnSRProcessNotifyLastTimeSent_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 1, 3, 1, 6),
    _RbnSRProcessNotifyLastTimeSent_Type()
)
rbnSRProcessNotifyLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRProcessNotifyLastTimeSent.setStatus("current")
_RbnSRStorage_ObjectIdentity = ObjectIdentity
rbnSRStorage = _RbnSRStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2)
)
_RbnSRStorageTable_Object = MibTable
rbnSRStorageTable = _RbnSRStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rbnSRStorageTable.setStatus("current")
_RbnSRStorageEntry_Object = MibTableRow
rbnSRStorageEntry = _RbnSRStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1, 1)
)
rbnSRStorageEntry.setIndexNames(
    (0, "RBN-SYS-RESOURCES-MIB", "rbnSRStorageIndex"),
)
if mibBuilder.loadTexts:
    rbnSRStorageEntry.setStatus("current")


class _RbnSRStorageIndex_Type(Integer32):
    """Custom type rbnSRStorageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RbnSRStorageIndex_Type.__name__ = "Integer32"
_RbnSRStorageIndex_Object = MibTableColumn
rbnSRStorageIndex = _RbnSRStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1, 1, 1),
    _RbnSRStorageIndex_Type()
)
rbnSRStorageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSRStorageIndex.setStatus("current")


class _RbnSRStorageDescr_Type(SnmpAdminString):
    """Custom type rbnSRStorageDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RbnSRStorageDescr_Type.__name__ = "SnmpAdminString"
_RbnSRStorageDescr_Object = MibTableColumn
rbnSRStorageDescr = _RbnSRStorageDescr_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1, 1, 2),
    _RbnSRStorageDescr_Type()
)
rbnSRStorageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRStorageDescr.setStatus("current")


class _RbnSRStorageMedia_Type(Integer32):
    """Custom type rbnSRStorageMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("hardDisk", 2),
          ("flashMemory", 3))
    )


_RbnSRStorageMedia_Type.__name__ = "Integer32"
_RbnSRStorageMedia_Object = MibTableColumn
rbnSRStorageMedia = _RbnSRStorageMedia_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1, 1, 3),
    _RbnSRStorageMedia_Type()
)
rbnSRStorageMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRStorageMedia.setStatus("current")
_RbnSRStorageRemovable_Type = TruthValue
_RbnSRStorageRemovable_Object = MibTableColumn
rbnSRStorageRemovable = _RbnSRStorageRemovable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1, 1, 4),
    _RbnSRStorageRemovable_Type()
)
rbnSRStorageRemovable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRStorageRemovable.setStatus("current")
_RbnSRStorageSize_Type = RbnKBytes
_RbnSRStorageSize_Object = MibTableColumn
rbnSRStorageSize = _RbnSRStorageSize_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1, 1, 5),
    _RbnSRStorageSize_Type()
)
rbnSRStorageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRStorageSize.setStatus("current")
if mibBuilder.loadTexts:
    rbnSRStorageSize.setUnits("KBytes")
_RbnSRStorageUtilization_Type = RbnPercentage
_RbnSRStorageUtilization_Object = MibTableColumn
rbnSRStorageUtilization = _RbnSRStorageUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1, 1, 6),
    _RbnSRStorageUtilization_Type()
)
rbnSRStorageUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRStorageUtilization.setStatus("current")
_RbnSRStorageSlot_Type = RbnSlot
_RbnSRStorageSlot_Object = MibTableColumn
rbnSRStorageSlot = _RbnSRStorageSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1, 1, 7),
    _RbnSRStorageSlot_Type()
)
rbnSRStorageSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRStorageSlot.setStatus("current")
_RbnSRStorageMountTime_Type = TimeTicks
_RbnSRStorageMountTime_Object = MibTableColumn
rbnSRStorageMountTime = _RbnSRStorageMountTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1, 1, 8),
    _RbnSRStorageMountTime_Type()
)
rbnSRStorageMountTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRStorageMountTime.setStatus("current")


class _RbnSRStorageStatus_Type(Integer32):
    """Custom type rbnSRStorageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("degrading", 2),
          ("failed", 3))
    )


_RbnSRStorageStatus_Type.__name__ = "Integer32"
_RbnSRStorageStatus_Object = MibTableColumn
rbnSRStorageStatus = _RbnSRStorageStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1, 1, 9),
    _RbnSRStorageStatus_Type()
)
rbnSRStorageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRStorageStatus.setStatus("current")
_RbnSRStorageErrors_Type = Counter32
_RbnSRStorageErrors_Object = MibTableColumn
rbnSRStorageErrors = _RbnSRStorageErrors_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 1, 1, 10),
    _RbnSRStorageErrors_Type()
)
rbnSRStorageErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRStorageErrors.setStatus("current")
_RbnSseDiskStorageTable_Object = MibTable
rbnSseDiskStorageTable = _RbnSseDiskStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rbnSseDiskStorageTable.setStatus("current")
_RbnSseDiskStorageEntry_Object = MibTableRow
rbnSseDiskStorageEntry = _RbnSseDiskStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 2, 1)
)
rbnSseDiskStorageEntry.setIndexNames(
    (0, "RBN-SYS-RESOURCES-MIB", "rbnSseDiskSlot"),
    (0, "RBN-SYS-RESOURCES-MIB", "rbnSseDiskNum"),
)
if mibBuilder.loadTexts:
    rbnSseDiskStorageEntry.setStatus("current")
_RbnSseDiskSlot_Type = RbnSlot
_RbnSseDiskSlot_Object = MibTableColumn
rbnSseDiskSlot = _RbnSseDiskSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 2, 1, 1),
    _RbnSseDiskSlot_Type()
)
rbnSseDiskSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSseDiskSlot.setStatus("current")


class _RbnSseDiskNum_Type(Unsigned32):
    """Custom type rbnSseDiskNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RbnSseDiskNum_Type.__name__ = "Unsigned32"
_RbnSseDiskNum_Object = MibTableColumn
rbnSseDiskNum = _RbnSseDiskNum_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 2, 1, 2),
    _RbnSseDiskNum_Type()
)
rbnSseDiskNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSseDiskNum.setStatus("current")


class _RbnSseDiskState_Type(Integer32):
    """Custom type rbnSseDiskState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RbnSseDiskState_Type.__name__ = "Integer32"
_RbnSseDiskState_Object = MibTableColumn
rbnSseDiskState = _RbnSseDiskState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 2, 1, 3),
    _RbnSseDiskState_Type()
)
rbnSseDiskState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSseDiskState.setStatus("current")
_RbnSseDiskSize_Type = Unsigned32
_RbnSseDiskSize_Object = MibTableColumn
rbnSseDiskSize = _RbnSseDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 2, 1, 4),
    _RbnSseDiskSize_Type()
)
rbnSseDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSseDiskSize.setStatus("current")
if mibBuilder.loadTexts:
    rbnSseDiskSize.setUnits("GBytes")
_RbnSseDiskUsed_Type = Unsigned32
_RbnSseDiskUsed_Object = MibTableColumn
rbnSseDiskUsed = _RbnSseDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 2, 2, 1, 5),
    _RbnSseDiskUsed_Type()
)
rbnSseDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSseDiskUsed.setStatus("current")
if mibBuilder.loadTexts:
    rbnSseDiskUsed.setUnits("GBytes")
_RbnSRSystem_ObjectIdentity = ObjectIdentity
rbnSRSystem = _RbnSRSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 3)
)
_RbnSRSystemUptime_Type = TimeTicks
_RbnSRSystemUptime_Object = MibScalar
rbnSRSystemUptime = _RbnSRSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 3, 1),
    _RbnSRSystemUptime_Type()
)
rbnSRSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSRSystemUptime.setStatus("current")
_RbnSRSystemDate_Type = DateAndTime
_RbnSRSystemDate_Object = MibScalar
rbnSRSystemDate = _RbnSRSystemDate_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 3, 2),
    _RbnSRSystemDate_Type()
)
rbnSRSystemDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbnSRSystemDate.setStatus("current")
_RbnPowerExceeded_ObjectIdentity = ObjectIdentity
rbnPowerExceeded = _RbnPowerExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 4)
)


class _RbnSRPowerExceededStatus_Type(Integer32):
    """Custom type rbnSRPowerExceededStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("failed", 2))
    )


_RbnSRPowerExceededStatus_Type.__name__ = "Integer32"
_RbnSRPowerExceededStatus_Object = MibScalar
rbnSRPowerExceededStatus = _RbnSRPowerExceededStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 4, 1),
    _RbnSRPowerExceededStatus_Type()
)
rbnSRPowerExceededStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSRPowerExceededStatus.setStatus("current")
_RbnSseDiskAlarmDateAndTime_Type = DateAndTime
_RbnSseDiskAlarmDateAndTime_Object = MibScalar
rbnSseDiskAlarmDateAndTime = _RbnSseDiskAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 5),
    _RbnSseDiskAlarmDateAndTime_Type()
)
rbnSseDiskAlarmDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSseDiskAlarmDateAndTime.setStatus("current")
_RbnSseDiskAlarmSeverity_Type = ItuPerceivedSeverity
_RbnSseDiskAlarmSeverity_Object = MibScalar
rbnSseDiskAlarmSeverity = _RbnSseDiskAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 6),
    _RbnSseDiskAlarmSeverity_Type()
)
rbnSseDiskAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSseDiskAlarmSeverity.setStatus("current")
_RbnSseDiskAlarmProbableCause_Type = IANAItuProbableCause
_RbnSseDiskAlarmProbableCause_Object = MibScalar
rbnSseDiskAlarmProbableCause = _RbnSseDiskAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 7),
    _RbnSseDiskAlarmProbableCause_Type()
)
rbnSseDiskAlarmProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSseDiskAlarmProbableCause.setStatus("current")
_RbnSseDiskEventType_Type = IANAItuEventType
_RbnSseDiskEventType_Object = MibScalar
rbnSseDiskEventType = _RbnSseDiskEventType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 8),
    _RbnSseDiskEventType_Type()
)
rbnSseDiskEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSseDiskEventType.setStatus("current")


class _RbnSseDiskAlarmDescription_Type(SnmpAdminString):
    """Custom type rbnSseDiskAlarmDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RbnSseDiskAlarmDescription_Type.__name__ = "SnmpAdminString"
_RbnSseDiskAlarmDescription_Object = MibScalar
rbnSseDiskAlarmDescription = _RbnSseDiskAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 9),
    _RbnSseDiskAlarmDescription_Type()
)
rbnSseDiskAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnSseDiskAlarmDescription.setStatus("current")
_RbnIssuObjects_ObjectIdentity = ObjectIdentity
rbnIssuObjects = _RbnIssuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 10)
)


class _RbnIssuState_Type(Integer32):
    """Custom type rbnIssuState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("start", 1),
          ("complete", 2),
          ("aborted", 3))
    )


_RbnIssuState_Type.__name__ = "Integer32"
_RbnIssuState_Object = MibScalar
rbnIssuState = _RbnIssuState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 10, 1),
    _RbnIssuState_Type()
)
rbnIssuState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnIssuState.setStatus("current")
_RbnChassisGroup_ObjectIdentity = ObjectIdentity
rbnChassisGroup = _RbnChassisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 11)
)
_RbnChassisAlarmId_Type = RbnAlarmId
_RbnChassisAlarmId_Object = MibScalar
rbnChassisAlarmId = _RbnChassisAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 11, 1),
    _RbnChassisAlarmId_Type()
)
rbnChassisAlarmId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnChassisAlarmId.setStatus("current")
_RbnChassisAlarmType_Type = IANAItuEventType
_RbnChassisAlarmType_Object = MibScalar
rbnChassisAlarmType = _RbnChassisAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 11, 2),
    _RbnChassisAlarmType_Type()
)
rbnChassisAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnChassisAlarmType.setStatus("current")
_RbnChassisAlarmDateAndTime_Type = DateAndTime
_RbnChassisAlarmDateAndTime_Object = MibScalar
rbnChassisAlarmDateAndTime = _RbnChassisAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 11, 3),
    _RbnChassisAlarmDateAndTime_Type()
)
rbnChassisAlarmDateAndTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnChassisAlarmDateAndTime.setStatus("current")


class _RbnChassisAlarmDescription_Type(SnmpAdminString):
    """Custom type rbnChassisAlarmDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RbnChassisAlarmDescription_Type.__name__ = "SnmpAdminString"
_RbnChassisAlarmDescription_Object = MibScalar
rbnChassisAlarmDescription = _RbnChassisAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 11, 4),
    _RbnChassisAlarmDescription_Type()
)
rbnChassisAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnChassisAlarmDescription.setStatus("current")
_RbnChassisAlarmProbableCause_Type = IANAItuProbableCause
_RbnChassisAlarmProbableCause_Object = MibScalar
rbnChassisAlarmProbableCause = _RbnChassisAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 11, 5),
    _RbnChassisAlarmProbableCause_Type()
)
rbnChassisAlarmProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnChassisAlarmProbableCause.setStatus("current")
_RbnChassisAlarmSeverity_Type = ItuPerceivedSeverity
_RbnChassisAlarmSeverity_Object = MibScalar
rbnChassisAlarmSeverity = _RbnChassisAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 1, 11, 6),
    _RbnChassisAlarmSeverity_Type()
)
rbnChassisAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnChassisAlarmSeverity.setStatus("current")
_RbnSRMIBConformance_ObjectIdentity = ObjectIdentity
rbnSRMIBConformance = _RbnSRMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2)
)
_RbnSRMIBCompliances_ObjectIdentity = ObjectIdentity
rbnSRMIBCompliances = _RbnSRMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 1)
)
_RbnSRMIBGroups_ObjectIdentity = ObjectIdentity
rbnSRMIBGroups = _RbnSRMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2)
)

# Managed Objects groups

rbnSRProcessNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 1)
)
rbnSRProcessNotifyGroup.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyLastUpdate"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRProcessEventNotifyEnable"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyPID"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyEventCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyEventType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNumOfSpawn"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyLastTimeSent"))
)
if mibBuilder.loadTexts:
    rbnSRProcessNotifyGroup.setStatus("current")

rbnSRStorageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 2)
)
rbnSRStorageGroup.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRStorageDescr"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageMedia"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageRemovable"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageSize"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageUtilization"))
)
if mibBuilder.loadTexts:
    rbnSRStorageGroup.setStatus("deprecated")

rbnSRStorageGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 5)
)
rbnSRStorageGroup2.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRStorageDescr"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageMedia"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageRemovable"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageSize"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageUtilization"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageSlot"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageMountTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageStatus"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageErrors"))
)
if mibBuilder.loadTexts:
    rbnSRStorageGroup2.setStatus("current")

rbnSRSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 7)
)
rbnSRSystemGroup.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRSystemUptime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRSystemDate"))
)
if mibBuilder.loadTexts:
    rbnSRSystemGroup.setStatus("current")

rbnSRPowerExceededGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 9)
)
rbnSRPowerExceededGroup.setObjects(
    ("RBN-SYS-RESOURCES-MIB", "rbnSRPowerExceededStatus")
)
if mibBuilder.loadTexts:
    rbnSRPowerExceededGroup.setStatus("current")

rbnSseDiskGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 10)
)
rbnSseDiskGroup.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSseDiskState"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskSize"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskUsed"))
)
if mibBuilder.loadTexts:
    rbnSseDiskGroup.setStatus("current")

rbnSseDiskEventObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 11)
)
rbnSseDiskEventObjectGroup.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSseDiskEventType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDateAndTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDescription"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmProbableCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmSeverity"))
)
if mibBuilder.loadTexts:
    rbnSseDiskEventObjectGroup.setStatus("current")

rbnIssuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 13)
)
rbnIssuGroup.setObjects(
    ("RBN-SYS-RESOURCES-MIB", "rbnIssuState")
)
if mibBuilder.loadTexts:
    rbnIssuGroup.setStatus("current")

rbnChassisEventObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 15)
)
rbnChassisEventObjectGroup.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmId"),
        ("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmDateAndTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmDescription"),
        ("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmProbableCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmSeverity"))
)
if mibBuilder.loadTexts:
    rbnChassisEventObjectGroup.setStatus("current")


# Notification objects

rbnSRProcessEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 1)
)
rbnSRProcessEvent.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyPID"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyEventCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyEventType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNumOfSpawn"))
)
if mibBuilder.loadTexts:
    rbnSRProcessEvent.setStatus(
        "current"
    )

rbnSRSwitchoverEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 2)
)
if mibBuilder.loadTexts:
    rbnSRSwitchoverEvent.setStatus(
        "current"
    )

rbnSRStorageFailedEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 3)
)
rbnSRStorageFailedEvent.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRStorageDescr"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageMedia"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageSlot"))
)
if mibBuilder.loadTexts:
    rbnSRStorageFailedEvent.setStatus(
        "current"
    )

rbnSRPowerExceededEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 4)
)
rbnSRPowerExceededEvent.setObjects(
    ("RBN-SYS-RESOURCES-MIB", "rbnSRPowerExceededStatus")
)
if mibBuilder.loadTexts:
    rbnSRPowerExceededEvent.setStatus(
        "current"
    )

rbnSseDiskHealthDegradedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 5)
)
rbnSseDiskHealthDegradedAlarm.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDateAndTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmSeverity"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmProbableCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskEventType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDescription"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskState"))
)
if mibBuilder.loadTexts:
    rbnSseDiskHealthDegradedAlarm.setStatus(
        "current"
    )

rbnSseDiskFailedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 6)
)
rbnSseDiskFailedAlarm.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDateAndTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmSeverity"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmProbableCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskEventType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDescription"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskState"))
)
if mibBuilder.loadTexts:
    rbnSseDiskFailedAlarm.setStatus(
        "current"
    )

rbnSseDiskMissingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 7)
)
rbnSseDiskMissingAlarm.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDateAndTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmSeverity"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmProbableCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskEventType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDescription"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskState"))
)
if mibBuilder.loadTexts:
    rbnSseDiskMissingAlarm.setStatus(
        "current"
    )

rbnSseDiskUnsupportedAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 8)
)
rbnSseDiskUnsupportedAlarm.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDateAndTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmSeverity"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmProbableCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskEventType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDescription"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskState"))
)
if mibBuilder.loadTexts:
    rbnSseDiskUnsupportedAlarm.setStatus(
        "current"
    )

rbnSseDiskOOSAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 9)
)
rbnSseDiskOOSAlarm.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDateAndTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmSeverity"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmProbableCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskEventType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDescription"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskState"))
)
if mibBuilder.loadTexts:
    rbnSseDiskOOSAlarm.setStatus(
        "current"
    )

rbnSseDiskVoltageFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 10)
)
rbnSseDiskVoltageFailureAlarm.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDateAndTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmSeverity"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmProbableCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskEventType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDescription"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskState"))
)
if mibBuilder.loadTexts:
    rbnSseDiskVoltageFailureAlarm.setStatus(
        "current"
    )

rbnSseDiskOverHeatAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 11)
)
rbnSseDiskOverHeatAlarm.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDateAndTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmSeverity"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmProbableCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskEventType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDescription"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskState"))
)
if mibBuilder.loadTexts:
    rbnSseDiskOverHeatAlarm.setStatus(
        "current"
    )

rbnSseDiskReadFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 12)
)
rbnSseDiskReadFailureAlarm.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDateAndTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmSeverity"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmProbableCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskEventType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskAlarmDescription"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskState"))
)
if mibBuilder.loadTexts:
    rbnSseDiskReadFailureAlarm.setStatus(
        "current"
    )

rbnIssuStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 13)
)
rbnIssuStateChange.setObjects(
    ("RBN-SYS-RESOURCES-MIB", "rbnIssuState")
)
if mibBuilder.loadTexts:
    rbnIssuStateChange.setStatus(
        "current"
    )

rbnChassisAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 0, 14)
)
rbnChassisAlarm.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmId"),
        ("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmType"),
        ("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmDateAndTime"),
        ("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmDescription"),
        ("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmProbableCause"),
        ("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarmSeverity"))
)
if mibBuilder.loadTexts:
    rbnChassisAlarm.setStatus(
        "current"
    )


# Notifications groups

rbnSRProcessEventNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 3)
)
rbnSRProcessEventNotificationGroup.setObjects(
    ("RBN-SYS-RESOURCES-MIB", "rbnSRProcessEvent")
)
if mibBuilder.loadTexts:
    rbnSRProcessEventNotificationGroup.setStatus(
        "obsolete"
    )

rbnSRNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 4)
)
rbnSRNotificationGroup.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRProcessEvent"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRSwitchoverEvent"))
)
if mibBuilder.loadTexts:
    rbnSRNotificationGroup.setStatus(
        "deprecated"
    )

rbnSRNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 6)
)
rbnSRNotificationGroup2.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRProcessEvent"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRSwitchoverEvent"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRStorageFailedEvent"))
)
if mibBuilder.loadTexts:
    rbnSRNotificationGroup2.setStatus(
        "current"
    )

rbnSRPowerNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 8)
)
rbnSRPowerNotifyGroup.setObjects(
    ("RBN-SYS-RESOURCES-MIB", "rbnSRPowerExceededEvent")
)
if mibBuilder.loadTexts:
    rbnSRPowerNotifyGroup.setStatus(
        "current"
    )

rbnSseDiskNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 12)
)
rbnSseDiskNotifyGroup.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSseDiskHealthDegradedAlarm"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskFailedAlarm"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskMissingAlarm"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskUnsupportedAlarm"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskOOSAlarm"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskVoltageFailureAlarm"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskOverHeatAlarm"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSseDiskReadFailureAlarm"))
)
if mibBuilder.loadTexts:
    rbnSseDiskNotifyGroup.setStatus(
        "current"
    )

rbnIssuNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 14)
)
rbnIssuNotifyGroup.setObjects(
    ("RBN-SYS-RESOURCES-MIB", "rbnIssuStateChange")
)
if mibBuilder.loadTexts:
    rbnIssuNotifyGroup.setStatus(
        "current"
    )

rbnChassisNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 2, 16)
)
rbnChassisNotifyGroup.setObjects(
    ("RBN-SYS-RESOURCES-MIB", "rbnChassisAlarm")
)
if mibBuilder.loadTexts:
    rbnChassisNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnSRMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnSRMIBCompliance1.setStatus(
        "obsolete"
    )

rbnSRMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 1, 2)
)
rbnSRMIBCompliance2.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyGroup"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRNotificationGroup"))
)
if mibBuilder.loadTexts:
    rbnSRMIBCompliance2.setStatus(
        "deprecated"
    )

rbnSRMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 1, 3)
)
rbnSRMIBCompliance3.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyGroup"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRNotificationGroup2"))
)
if mibBuilder.loadTexts:
    rbnSRMIBCompliance3.setStatus(
        "deprecated"
    )

rbnSRMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 1, 4)
)
rbnSRMIBCompliance4.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyGroup"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRNotificationGroup2"))
)
if mibBuilder.loadTexts:
    rbnSRMIBCompliance4.setStatus(
        "deprecated"
    )

rbnSRMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 1, 5)
)
rbnSRMIBCompliance.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyGroup"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRNotificationGroup2"))
)
if mibBuilder.loadTexts:
    rbnSRMIBCompliance.setStatus(
        "deprecated"
    )

rbnSRMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 24, 2, 1, 6)
)
rbnSRMIBCompliance6.setObjects(
      *(("RBN-SYS-RESOURCES-MIB", "rbnSRProcessNotifyGroup"),
        ("RBN-SYS-RESOURCES-MIB", "rbnSRNotificationGroup2"),
        ("RBN-SYS-RESOURCES-MIB", "rbnIssuGroup"),
        ("RBN-SYS-RESOURCES-MIB", "rbnIssuNotifyGroup"))
)
if mibBuilder.loadTexts:
    rbnSRMIBCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-SYS-RESOURCES-MIB",
    **{"rbnSysResourcesMib": rbnSysResourcesMib,
       "rbnSRMIBNotifications": rbnSRMIBNotifications,
       "rbnSRProcessEvent": rbnSRProcessEvent,
       "rbnSRSwitchoverEvent": rbnSRSwitchoverEvent,
       "rbnSRStorageFailedEvent": rbnSRStorageFailedEvent,
       "rbnSRPowerExceededEvent": rbnSRPowerExceededEvent,
       "rbnSseDiskHealthDegradedAlarm": rbnSseDiskHealthDegradedAlarm,
       "rbnSseDiskFailedAlarm": rbnSseDiskFailedAlarm,
       "rbnSseDiskMissingAlarm": rbnSseDiskMissingAlarm,
       "rbnSseDiskUnsupportedAlarm": rbnSseDiskUnsupportedAlarm,
       "rbnSseDiskOOSAlarm": rbnSseDiskOOSAlarm,
       "rbnSseDiskVoltageFailureAlarm": rbnSseDiskVoltageFailureAlarm,
       "rbnSseDiskOverHeatAlarm": rbnSseDiskOverHeatAlarm,
       "rbnSseDiskReadFailureAlarm": rbnSseDiskReadFailureAlarm,
       "rbnIssuStateChange": rbnIssuStateChange,
       "rbnChassisAlarm": rbnChassisAlarm,
       "rbnSRMIBObjects": rbnSRMIBObjects,
       "rbnSRProcess": rbnSRProcess,
       "rbnSRProcessNotifyLastUpdate": rbnSRProcessNotifyLastUpdate,
       "rbnSRProcessEventNotifyEnable": rbnSRProcessEventNotifyEnable,
       "rbnSRProcessNotifyTable": rbnSRProcessNotifyTable,
       "rbnSRProcessNotifyEntry": rbnSRProcessNotifyEntry,
       "rbnSRProcessNotifyProcName": rbnSRProcessNotifyProcName,
       "rbnSRProcessNotifyPID": rbnSRProcessNotifyPID,
       "rbnSRProcessNotifyEventCause": rbnSRProcessNotifyEventCause,
       "rbnSRProcessNotifyEventType": rbnSRProcessNotifyEventType,
       "rbnSRProcessNumOfSpawn": rbnSRProcessNumOfSpawn,
       "rbnSRProcessNotifyLastTimeSent": rbnSRProcessNotifyLastTimeSent,
       "rbnSRStorage": rbnSRStorage,
       "rbnSRStorageTable": rbnSRStorageTable,
       "rbnSRStorageEntry": rbnSRStorageEntry,
       "rbnSRStorageIndex": rbnSRStorageIndex,
       "rbnSRStorageDescr": rbnSRStorageDescr,
       "rbnSRStorageMedia": rbnSRStorageMedia,
       "rbnSRStorageRemovable": rbnSRStorageRemovable,
       "rbnSRStorageSize": rbnSRStorageSize,
       "rbnSRStorageUtilization": rbnSRStorageUtilization,
       "rbnSRStorageSlot": rbnSRStorageSlot,
       "rbnSRStorageMountTime": rbnSRStorageMountTime,
       "rbnSRStorageStatus": rbnSRStorageStatus,
       "rbnSRStorageErrors": rbnSRStorageErrors,
       "rbnSseDiskStorageTable": rbnSseDiskStorageTable,
       "rbnSseDiskStorageEntry": rbnSseDiskStorageEntry,
       "rbnSseDiskSlot": rbnSseDiskSlot,
       "rbnSseDiskNum": rbnSseDiskNum,
       "rbnSseDiskState": rbnSseDiskState,
       "rbnSseDiskSize": rbnSseDiskSize,
       "rbnSseDiskUsed": rbnSseDiskUsed,
       "rbnSRSystem": rbnSRSystem,
       "rbnSRSystemUptime": rbnSRSystemUptime,
       "rbnSRSystemDate": rbnSRSystemDate,
       "rbnPowerExceeded": rbnPowerExceeded,
       "rbnSRPowerExceededStatus": rbnSRPowerExceededStatus,
       "rbnSseDiskAlarmDateAndTime": rbnSseDiskAlarmDateAndTime,
       "rbnSseDiskAlarmSeverity": rbnSseDiskAlarmSeverity,
       "rbnSseDiskAlarmProbableCause": rbnSseDiskAlarmProbableCause,
       "rbnSseDiskEventType": rbnSseDiskEventType,
       "rbnSseDiskAlarmDescription": rbnSseDiskAlarmDescription,
       "rbnIssuObjects": rbnIssuObjects,
       "rbnIssuState": rbnIssuState,
       "rbnChassisGroup": rbnChassisGroup,
       "rbnChassisAlarmId": rbnChassisAlarmId,
       "rbnChassisAlarmType": rbnChassisAlarmType,
       "rbnChassisAlarmDateAndTime": rbnChassisAlarmDateAndTime,
       "rbnChassisAlarmDescription": rbnChassisAlarmDescription,
       "rbnChassisAlarmProbableCause": rbnChassisAlarmProbableCause,
       "rbnChassisAlarmSeverity": rbnChassisAlarmSeverity,
       "rbnSRMIBConformance": rbnSRMIBConformance,
       "rbnSRMIBCompliances": rbnSRMIBCompliances,
       "rbnSRMIBCompliance1": rbnSRMIBCompliance1,
       "rbnSRMIBCompliance2": rbnSRMIBCompliance2,
       "rbnSRMIBCompliance3": rbnSRMIBCompliance3,
       "rbnSRMIBCompliance4": rbnSRMIBCompliance4,
       "rbnSRMIBCompliance": rbnSRMIBCompliance,
       "rbnSRMIBCompliance6": rbnSRMIBCompliance6,
       "rbnSRMIBGroups": rbnSRMIBGroups,
       "rbnSRProcessNotifyGroup": rbnSRProcessNotifyGroup,
       "rbnSRStorageGroup": rbnSRStorageGroup,
       "rbnSRProcessEventNotificationGroup": rbnSRProcessEventNotificationGroup,
       "rbnSRNotificationGroup": rbnSRNotificationGroup,
       "rbnSRStorageGroup2": rbnSRStorageGroup2,
       "rbnSRNotificationGroup2": rbnSRNotificationGroup2,
       "rbnSRSystemGroup": rbnSRSystemGroup,
       "rbnSRPowerNotifyGroup": rbnSRPowerNotifyGroup,
       "rbnSRPowerExceededGroup": rbnSRPowerExceededGroup,
       "rbnSseDiskGroup": rbnSseDiskGroup,
       "rbnSseDiskEventObjectGroup": rbnSseDiskEventObjectGroup,
       "rbnSseDiskNotifyGroup": rbnSseDiskNotifyGroup,
       "rbnIssuGroup": rbnIssuGroup,
       "rbnIssuNotifyGroup": rbnIssuNotifyGroup,
       "rbnChassisEventObjectGroup": rbnChassisEventObjectGroup,
       "rbnChassisNotifyGroup": rbnChassisNotifyGroup}
)
