# SNMP MIB module (CISCO-RF-SUPPLEMENTAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-RF-SUPPLEMENTAL-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:18:37 2025
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

(ConfigCopyState,) = mibBuilder.importSymbols(
    "CISCO-CONFIG-COPY-MIB",
    "ConfigCopyState")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(ifAdminStatus,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifIndex",
    "ifOperStatus")

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

ciscoRfSupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198)
)
if mibBuilder.loadTexts:
    ciscoRfSupMIB.setRevisions(
        ("2019-02-22 00:00",
         "2004-05-27 00:00",
         "2004-03-04 00:00",
         "2001-03-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RfSupSyncAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableAutoSync", 1),
          ("disableAutoSync", 2))
    )



class RfSupSyncOperState(TextualConvention, Integer32):
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
        *(("inSync", 1),
          ("lastUpdateFailed", 2),
          ("commDown", 3),
          ("syncDisabled", 4),
          ("noStandbyPresent", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoRfSupMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoRfSupMIBNotifs = _CiscoRfSupMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 0)
)
_CiscoRfSupMIBObjects_ObjectIdentity = ObjectIdentity
ciscoRfSupMIBObjects = _CiscoRfSupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1)
)
_CRfSupSystem_ObjectIdentity = ObjectIdentity
cRfSupSystem = _CRfSupSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1)
)
_CRfSupSysAvailableStartTime_Type = DateAndTime
_CRfSupSysAvailableStartTime_Object = MibScalar
cRfSupSysAvailableStartTime = _CRfSupSysAvailableStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 1),
    _CRfSupSysAvailableStartTime_Type()
)
cRfSupSysAvailableStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysAvailableStartTime.setStatus("current")
_CRfSupSysSwitchoverTime_Type = DateAndTime
_CRfSupSysSwitchoverTime_Object = MibScalar
cRfSupSysSwitchoverTime = _CRfSupSysSwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 2),
    _CRfSupSysSwitchoverTime_Type()
)
cRfSupSysSwitchoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysSwitchoverTime.setStatus("current")
_CRfSupSysSwitchovers_Type = Counter32
_CRfSupSysSwitchovers_Object = MibScalar
cRfSupSysSwitchovers = _CRfSupSysSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 3),
    _CRfSupSysSwitchovers_Type()
)
cRfSupSysSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysSwitchovers.setStatus("current")
_CRfSupSysRunningConfigSyncTime_Type = DateAndTime
_CRfSupSysRunningConfigSyncTime_Object = MibScalar
cRfSupSysRunningConfigSyncTime = _CRfSupSysRunningConfigSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 4),
    _CRfSupSysRunningConfigSyncTime_Type()
)
cRfSupSysRunningConfigSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysRunningConfigSyncTime.setStatus("current")
_CRfSupSysRunningConfigAdmin_Type = RfSupSyncAdminState
_CRfSupSysRunningConfigAdmin_Object = MibScalar
cRfSupSysRunningConfigAdmin = _CRfSupSysRunningConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 5),
    _CRfSupSysRunningConfigAdmin_Type()
)
cRfSupSysRunningConfigAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRfSupSysRunningConfigAdmin.setStatus("current")
_CRfSupSysRunningConfigOper_Type = RfSupSyncOperState
_CRfSupSysRunningConfigOper_Object = MibScalar
cRfSupSysRunningConfigOper = _CRfSupSysRunningConfigOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 6),
    _CRfSupSysRunningConfigOper_Type()
)
cRfSupSysRunningConfigOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysRunningConfigOper.setStatus("current")
_CRfSupSysStartupConfigSyncTime_Type = DateAndTime
_CRfSupSysStartupConfigSyncTime_Object = MibScalar
cRfSupSysStartupConfigSyncTime = _CRfSupSysStartupConfigSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 7),
    _CRfSupSysStartupConfigSyncTime_Type()
)
cRfSupSysStartupConfigSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysStartupConfigSyncTime.setStatus("current")
_CRfSupSysStartupConfigAdmin_Type = RfSupSyncAdminState
_CRfSupSysStartupConfigAdmin_Object = MibScalar
cRfSupSysStartupConfigAdmin = _CRfSupSysStartupConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 8),
    _CRfSupSysStartupConfigAdmin_Type()
)
cRfSupSysStartupConfigAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRfSupSysStartupConfigAdmin.setStatus("current")
_CRfSupSysStartupConfigOper_Type = RfSupSyncOperState
_CRfSupSysStartupConfigOper_Object = MibScalar
cRfSupSysStartupConfigOper = _CRfSupSysStartupConfigOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 9),
    _CRfSupSysStartupConfigOper_Type()
)
cRfSupSysStartupConfigOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysStartupConfigOper.setStatus("current")
_CRfSupSysBootImageSyncTime_Type = DateAndTime
_CRfSupSysBootImageSyncTime_Object = MibScalar
cRfSupSysBootImageSyncTime = _CRfSupSysBootImageSyncTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 10),
    _CRfSupSysBootImageSyncTime_Type()
)
cRfSupSysBootImageSyncTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysBootImageSyncTime.setStatus("current")
_CRfSupSysBootImageAdmin_Type = RfSupSyncAdminState
_CRfSupSysBootImageAdmin_Object = MibScalar
cRfSupSysBootImageAdmin = _CRfSupSysBootImageAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 11),
    _CRfSupSysBootImageAdmin_Type()
)
cRfSupSysBootImageAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRfSupSysBootImageAdmin.setStatus("current")
_CRfSupSysBootImageOper_Type = RfSupSyncOperState
_CRfSupSysBootImageOper_Object = MibScalar
cRfSupSysBootImageOper = _CRfSupSysBootImageOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 12),
    _CRfSupSysBootImageOper_Type()
)
cRfSupSysBootImageOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysBootImageOper.setStatus("current")


class _CRfSupSysStandbyBootFile_Type(SnmpAdminString):
    """Custom type cRfSupSysStandbyBootFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CRfSupSysStandbyBootFile_Type.__name__ = "SnmpAdminString"
_CRfSupSysStandbyBootFile_Object = MibScalar
cRfSupSysStandbyBootFile = _CRfSupSysStandbyBootFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 13),
    _CRfSupSysStandbyBootFile_Type()
)
cRfSupSysStandbyBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRfSupSysStandbyBootFile.setStatus("current")


class _CRfSupNotificationsEnabled_Type(TruthValue):
    """Custom type cRfSupNotificationsEnabled based on TruthValue"""
    defaultValue = 2


_CRfSupNotificationsEnabled_Type.__name__ = "TruthValue"
_CRfSupNotificationsEnabled_Object = MibScalar
cRfSupNotificationsEnabled = _CRfSupNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 14),
    _CRfSupNotificationsEnabled_Type()
)
cRfSupNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRfSupNotificationsEnabled.setStatus("current")
_CRfSupSysIfCounterSync_Type = TruthValue
_CRfSupSysIfCounterSync_Object = MibScalar
cRfSupSysIfCounterSync = _CRfSupSysIfCounterSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 15),
    _CRfSupSysIfCounterSync_Type()
)
cRfSupSysIfCounterSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRfSupSysIfCounterSync.setStatus("current")
_CRfSupSysFailureReason_Type = OctetString
_CRfSupSysFailureReason_Object = MibScalar
cRfSupSysFailureReason = _CRfSupSysFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 16),
    _CRfSupSysFailureReason_Type()
)
cRfSupSysFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysFailureReason.setStatus("current")


class _CRfSupSysSeverity_Type(Integer32):
    """Custom type cRfSupSysSeverity based on Integer32"""
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("informational", 4),
          ("clear", 5))
    )


_CRfSupSysSeverity_Type.__name__ = "Integer32"
_CRfSupSysSeverity_Object = MibScalar
cRfSupSysSeverity = _CRfSupSysSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 17),
    _CRfSupSysSeverity_Type()
)
cRfSupSysSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysSeverity.setStatus("current")


class _CRfSupSysErrorType_Type(Integer32):
    """Custom type cRfSupSysErrorType based on Integer32"""
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
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("download-config", 1),
          ("download-code", 2),
          ("download-icon", 3),
          ("download-image", 4),
          ("download-signature", 5),
          ("download-webadmincert", 6),
          ("download-webauthcert", 7),
          ("download-webauthbundle", 8),
          ("download-eapdevcert", 9),
          ("download-eapcacert", 10),
          ("download-login-banner", 11),
          ("upload-config", 12),
          ("upload-debug-file", 13),
          ("upload-crashfile", 14),
          ("upload-watchdog-crash-file", 15),
          ("upload-panic-crash-file", 16),
          ("upload-coredump", 17),
          ("upload-errorlog", 18),
          ("upload-invalid-config", 19),
          ("upload-pac", 20),
          ("upload-radio-core-dump", 21),
          ("upload-ap-crash-data", 22),
          ("upload-signature", 23),
          ("upload-systemtrace", 24),
          ("upload-packet-capture", 25),
          ("upload-traplog", 26),
          ("route-add", 27),
          ("route-del", 28),
          ("interface-service-port", 29),
          ("reset", 30),
          ("other", 31),
          ("config-sync-fail", 32),
          ("peer-maintenance", 33),
          ("peer-loss", 34),
          ("rfTrapClearTemplist", 35))
    )


_CRfSupSysErrorType_Type.__name__ = "Integer32"
_CRfSupSysErrorType_Object = MibScalar
cRfSupSysErrorType = _CRfSupSysErrorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 1, 18),
    _CRfSupSysErrorType_Type()
)
cRfSupSysErrorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupSysErrorType.setStatus("current")
_CRfSupCpu_ObjectIdentity = ObjectIdentity
cRfSupCpu = _CRfSupCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2)
)
_CRfSupCpuTable_Object = MibTable
cRfSupCpuTable = _CRfSupCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cRfSupCpuTable.setStatus("current")
_CRfSupCpuEntry_Object = MibTableRow
cRfSupCpuEntry = _CRfSupCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1)
)
cRfSupCpuEntry.setIndexNames(
    (0, "CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupCpuUniqueIndex"),
)
if mibBuilder.loadTexts:
    cRfSupCpuEntry.setStatus("current")
_CRfSupCpuUniqueIndex_Type = PhysicalIndex
_CRfSupCpuUniqueIndex_Object = MibTableColumn
cRfSupCpuUniqueIndex = _CRfSupCpuUniqueIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1, 1),
    _CRfSupCpuUniqueIndex_Type()
)
cRfSupCpuUniqueIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cRfSupCpuUniqueIndex.setStatus("current")


class _CRfSupCpuActiveSeverity_Type(Integer32):
    """Custom type cRfSupCpuActiveSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nonFaulty", 0),
          ("nonTrafficAffectingFault", 1),
          ("partialTrafficAffectingFault", 2),
          ("fullyTrafficAffectingFault", 3),
          ("unknown", 4))
    )


_CRfSupCpuActiveSeverity_Type.__name__ = "Integer32"
_CRfSupCpuActiveSeverity_Object = MibTableColumn
cRfSupCpuActiveSeverity = _CRfSupCpuActiveSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1, 2),
    _CRfSupCpuActiveSeverity_Type()
)
cRfSupCpuActiveSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupCpuActiveSeverity.setStatus("current")
_CRfSupCpuInitTime_Type = DateAndTime
_CRfSupCpuInitTime_Object = MibTableColumn
cRfSupCpuInitTime = _CRfSupCpuInitTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 2, 1, 1, 3),
    _CRfSupCpuInitTime_Type()
)
cRfSupCpuInitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupCpuInitTime.setStatus("current")
_CRfSupAction_ObjectIdentity = ObjectIdentity
cRfSupAction = _CRfSupAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 3)
)


class _CRfSupActionManualSync_Type(Integer32):
    """Custom type cRfSupActionManualSync based on Integer32"""
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
        *(("noAction", 1),
          ("runningConfig", 2),
          ("startupConfig", 3),
          ("bootImage", 4))
    )


_CRfSupActionManualSync_Type.__name__ = "Integer32"
_CRfSupActionManualSync_Object = MibScalar
cRfSupActionManualSync = _CRfSupActionManualSync_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 3, 1),
    _CRfSupActionManualSync_Type()
)
cRfSupActionManualSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cRfSupActionManualSync.setStatus("current")
_CRfSupActionLastSyncResult_Type = ConfigCopyState
_CRfSupActionLastSyncResult_Object = MibScalar
cRfSupActionLastSyncResult = _CRfSupActionLastSyncResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 1, 3, 2),
    _CRfSupActionLastSyncResult_Type()
)
cRfSupActionLastSyncResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRfSupActionLastSyncResult.setStatus("current")
_CiscoRfSupMibConformance_ObjectIdentity = ObjectIdentity
ciscoRfSupMibConformance = _CiscoRfSupMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2)
)
_CiscoRfSupMibCompliances_ObjectIdentity = ObjectIdentity
ciscoRfSupMibCompliances = _CiscoRfSupMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1)
)
_CiscoRfSupMibGroups_ObjectIdentity = ObjectIdentity
ciscoRfSupMibGroups = _CiscoRfSupMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2)
)

# Managed Objects groups

ciscoRfSupSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 1)
)
ciscoRfSupSysGroup.setObjects(
      *(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysAvailableStartTime"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchoverTime"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchovers"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysRunningConfigSyncTime"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysRunningConfigAdmin"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysRunningConfigOper"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStartupConfigSyncTime"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStartupConfigAdmin"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStartupConfigOper"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysBootImageSyncTime"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysBootImageAdmin"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysBootImageOper"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStandbyBootFile"))
)
if mibBuilder.loadTexts:
    ciscoRfSupSysGroup.setStatus("current")

ciscoRfSupCpuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 2)
)
ciscoRfSupCpuGroup.setObjects(
      *(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupCpuActiveSeverity"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupCpuInitTime"))
)
if mibBuilder.loadTexts:
    ciscoRfSupCpuGroup.setStatus("current")

ciscoRfSupActionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 3)
)
ciscoRfSupActionGroup.setObjects(
      *(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupActionManualSync"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupActionLastSyncResult"))
)
if mibBuilder.loadTexts:
    ciscoRfSupActionGroup.setStatus("current")

ciscoRfSupSysOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 4)
)
ciscoRfSupSysOptionalGroup.setObjects(
    ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupNotificationsEnabled")
)
if mibBuilder.loadTexts:
    ciscoRfSupSysOptionalGroup.setStatus("current")

ciscoRfSupSysOptionalSyncGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 6)
)
ciscoRfSupSysOptionalSyncGroup.setObjects(
    ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysIfCounterSync")
)
if mibBuilder.loadTexts:
    ciscoRfSupSysOptionalSyncGroup.setStatus("current")


# Notification objects

ciscoRfSupTimeChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 0, 1)
)
ciscoRfSupTimeChangeEvent.setObjects(
      *(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysAvailableStartTime"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchoverTime"))
)
if mibBuilder.loadTexts:
    ciscoRfSupTimeChangeEvent.setStatus(
        "current"
    )

ciscoRfSupTimeZoneChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 0, 2)
)
ciscoRfSupTimeZoneChangeEvent.setObjects(
      *(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysAvailableStartTime"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSwitchoverTime"))
)
if mibBuilder.loadTexts:
    ciscoRfSupTimeZoneChangeEvent.setStatus(
        "current"
    )

ciscoRfSupHAFailureEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 0, 3)
)
ciscoRfSupHAFailureEvent.setObjects(
      *(("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysStartupConfigSyncTime"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysRunningConfigSyncTime"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupActionManualSync"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupActionLastSyncResult"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysFailureReason"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysSeverity"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "cRfSupSysErrorType"))
)
if mibBuilder.loadTexts:
    ciscoRfSupHAFailureEvent.setStatus(
        "current"
    )

ciscoRfSupPeerLinkStateChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 0, 4)
)
ciscoRfSupPeerLinkStateChangeEvent.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"))
)
if mibBuilder.loadTexts:
    ciscoRfSupPeerLinkStateChangeEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoRfSupNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 5)
)
ciscoRfSupNotifGroup.setObjects(
    ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupTimeChangeEvent")
)
if mibBuilder.loadTexts:
    ciscoRfSupNotifGroup.setStatus(
        "deprecated"
    )

ciscoRfSupNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 2, 7)
)
ciscoRfSupNotifGroupRev1.setObjects(
      *(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupTimeChangeEvent"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupTimeZoneChangeEvent"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupHAFailureEvent"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupPeerLinkStateChangeEvent"))
)
if mibBuilder.loadTexts:
    ciscoRfSupNotifGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoRfSupMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1, 1)
)
ciscoRfSupMibCompliance.setObjects(
      *(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupActionGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupCpuGroup"))
)
if mibBuilder.loadTexts:
    ciscoRfSupMibCompliance.setStatus(
        "deprecated"
    )

ciscoRfSupMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1, 2)
)
ciscoRfSupMibComplianceRev1.setObjects(
      *(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupActionGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupCpuGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalGroup"))
)
if mibBuilder.loadTexts:
    ciscoRfSupMibComplianceRev1.setStatus(
        "deprecated"
    )

ciscoRfSupMibComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1, 3)
)
ciscoRfSupMibComplianceRev2.setObjects(
      *(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupActionGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupCpuGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupNotifGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalSyncGroup"))
)
if mibBuilder.loadTexts:
    ciscoRfSupMibComplianceRev2.setStatus(
        "deprecated"
    )

ciscoRfSupMibComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 198, 2, 1, 4)
)
ciscoRfSupMibComplianceRev3.setObjects(
      *(("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupActionGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupCpuGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalGroup"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupNotifGroupRev1"),
        ("CISCO-RF-SUPPLEMENTAL-MIB", "ciscoRfSupSysOptionalSyncGroup"))
)
if mibBuilder.loadTexts:
    ciscoRfSupMibComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RF-SUPPLEMENTAL-MIB",
    **{"RfSupSyncAdminState": RfSupSyncAdminState,
       "RfSupSyncOperState": RfSupSyncOperState,
       "ciscoRfSupMIB": ciscoRfSupMIB,
       "ciscoRfSupMIBNotifs": ciscoRfSupMIBNotifs,
       "ciscoRfSupTimeChangeEvent": ciscoRfSupTimeChangeEvent,
       "ciscoRfSupTimeZoneChangeEvent": ciscoRfSupTimeZoneChangeEvent,
       "ciscoRfSupHAFailureEvent": ciscoRfSupHAFailureEvent,
       "ciscoRfSupPeerLinkStateChangeEvent": ciscoRfSupPeerLinkStateChangeEvent,
       "ciscoRfSupMIBObjects": ciscoRfSupMIBObjects,
       "cRfSupSystem": cRfSupSystem,
       "cRfSupSysAvailableStartTime": cRfSupSysAvailableStartTime,
       "cRfSupSysSwitchoverTime": cRfSupSysSwitchoverTime,
       "cRfSupSysSwitchovers": cRfSupSysSwitchovers,
       "cRfSupSysRunningConfigSyncTime": cRfSupSysRunningConfigSyncTime,
       "cRfSupSysRunningConfigAdmin": cRfSupSysRunningConfigAdmin,
       "cRfSupSysRunningConfigOper": cRfSupSysRunningConfigOper,
       "cRfSupSysStartupConfigSyncTime": cRfSupSysStartupConfigSyncTime,
       "cRfSupSysStartupConfigAdmin": cRfSupSysStartupConfigAdmin,
       "cRfSupSysStartupConfigOper": cRfSupSysStartupConfigOper,
       "cRfSupSysBootImageSyncTime": cRfSupSysBootImageSyncTime,
       "cRfSupSysBootImageAdmin": cRfSupSysBootImageAdmin,
       "cRfSupSysBootImageOper": cRfSupSysBootImageOper,
       "cRfSupSysStandbyBootFile": cRfSupSysStandbyBootFile,
       "cRfSupNotificationsEnabled": cRfSupNotificationsEnabled,
       "cRfSupSysIfCounterSync": cRfSupSysIfCounterSync,
       "cRfSupSysFailureReason": cRfSupSysFailureReason,
       "cRfSupSysSeverity": cRfSupSysSeverity,
       "cRfSupSysErrorType": cRfSupSysErrorType,
       "cRfSupCpu": cRfSupCpu,
       "cRfSupCpuTable": cRfSupCpuTable,
       "cRfSupCpuEntry": cRfSupCpuEntry,
       "cRfSupCpuUniqueIndex": cRfSupCpuUniqueIndex,
       "cRfSupCpuActiveSeverity": cRfSupCpuActiveSeverity,
       "cRfSupCpuInitTime": cRfSupCpuInitTime,
       "cRfSupAction": cRfSupAction,
       "cRfSupActionManualSync": cRfSupActionManualSync,
       "cRfSupActionLastSyncResult": cRfSupActionLastSyncResult,
       "ciscoRfSupMibConformance": ciscoRfSupMibConformance,
       "ciscoRfSupMibCompliances": ciscoRfSupMibCompliances,
       "ciscoRfSupMibCompliance": ciscoRfSupMibCompliance,
       "ciscoRfSupMibComplianceRev1": ciscoRfSupMibComplianceRev1,
       "ciscoRfSupMibComplianceRev2": ciscoRfSupMibComplianceRev2,
       "ciscoRfSupMibComplianceRev3": ciscoRfSupMibComplianceRev3,
       "ciscoRfSupMibGroups": ciscoRfSupMibGroups,
       "ciscoRfSupSysGroup": ciscoRfSupSysGroup,
       "ciscoRfSupCpuGroup": ciscoRfSupCpuGroup,
       "ciscoRfSupActionGroup": ciscoRfSupActionGroup,
       "ciscoRfSupSysOptionalGroup": ciscoRfSupSysOptionalGroup,
       "ciscoRfSupNotifGroup": ciscoRfSupNotifGroup,
       "ciscoRfSupSysOptionalSyncGroup": ciscoRfSupSysOptionalSyncGroup,
       "ciscoRfSupNotifGroupRev1": ciscoRfSupNotifGroupRev1}
)
