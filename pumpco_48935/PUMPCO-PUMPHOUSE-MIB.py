# SNMP MIB module (PUMPCO-PUMPHOUSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/pumpco_48935/PUMPCO-PUMPHOUSE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:01:09 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

pumpCo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48935)
)
if mibBuilder.loadTexts:
    pumpCo.setRevisions(
        ("2016-12-01 10:22",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PumpHouse_ObjectIdentity = ObjectIdentity
pumpHouse = _PumpHouse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48935, 1)
)
_PumpHouseTables_ObjectIdentity = ObjectIdentity
pumpHouseTables = _PumpHouseTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48935, 1, 1)
)
_PumpHousePulseStatsTable_Object = MibTable
pumpHousePulseStatsTable = _PumpHousePulseStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 1, 11)
)
if mibBuilder.loadTexts:
    pumpHousePulseStatsTable.setStatus("current")
_PumpHousePulseStatsEntry_Object = MibTableRow
pumpHousePulseStatsEntry = _PumpHousePulseStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 1, 11, 1)
)
pumpHousePulseStatsEntry.setIndexNames(
    (0, "PUMPCO-PUMPHOUSE-MIB", "phPulseStatsClass"),
)
if mibBuilder.loadTexts:
    pumpHousePulseStatsEntry.setStatus("current")


class _PhPulseStatsClass_Type(OctetString):
    """Custom type phPulseStatsClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_PhPulseStatsClass_Type.__name__ = "OctetString"
_PhPulseStatsClass_Object = MibTableColumn
phPulseStatsClass = _PhPulseStatsClass_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 1, 11, 1, 1),
    _PhPulseStatsClass_Type()
)
phPulseStatsClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phPulseStatsClass.setStatus("current")
_PhPulseStatsCount_Type = Integer32
_PhPulseStatsCount_Object = MibTableColumn
phPulseStatsCount = _PhPulseStatsCount_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 1, 11, 1, 2),
    _PhPulseStatsCount_Type()
)
phPulseStatsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phPulseStatsCount.setStatus("current")
_PhPulseStatsFailures_Type = Integer32
_PhPulseStatsFailures_Object = MibTableColumn
phPulseStatsFailures = _PhPulseStatsFailures_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 1, 11, 1, 3),
    _PhPulseStatsFailures_Type()
)
phPulseStatsFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phPulseStatsFailures.setStatus("current")
_PhPulseStatsAvgTime_Type = Integer32
_PhPulseStatsAvgTime_Object = MibTableColumn
phPulseStatsAvgTime = _PhPulseStatsAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 1, 11, 1, 4),
    _PhPulseStatsAvgTime_Type()
)
phPulseStatsAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phPulseStatsAvgTime.setStatus("current")
_PumpHouseTraps_ObjectIdentity = ObjectIdentity
pumpHouseTraps = _PumpHouseTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2)
)
_PumpHouseAlertingTraps_ObjectIdentity = ObjectIdentity
pumpHouseAlertingTraps = _PumpHouseAlertingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2, 1)
)
_PumpHouseAlert_ObjectIdentity = ObjectIdentity
pumpHouseAlert = _PumpHouseAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2, 1, 1)
)
_PhAlertId_Type = OctetString
_PhAlertId_Object = MibScalar
phAlertId = _PhAlertId_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2, 1, 1, 1),
    _PhAlertId_Type()
)
phAlertId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phAlertId.setStatus("current")
_PhAlertDt_Type = OctetString
_PhAlertDt_Object = MibScalar
phAlertDt = _PhAlertDt_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2, 1, 1, 2),
    _PhAlertDt_Type()
)
phAlertDt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phAlertDt.setStatus("current")
_PhAlertUser_Type = OctetString
_PhAlertUser_Object = MibScalar
phAlertUser = _PhAlertUser_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2, 1, 1, 3),
    _PhAlertUser_Type()
)
phAlertUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phAlertUser.setStatus("current")
_PhAlertCategory_Type = OctetString
_PhAlertCategory_Object = MibScalar
phAlertCategory = _PhAlertCategory_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2, 1, 1, 4),
    _PhAlertCategory_Type()
)
phAlertCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phAlertCategory.setStatus("current")
_PhAlertLevel_Type = OctetString
_PhAlertLevel_Object = MibScalar
phAlertLevel = _PhAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2, 1, 1, 5),
    _PhAlertLevel_Type()
)
phAlertLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phAlertLevel.setStatus("current")
_PhAlertMessage_Type = OctetString
_PhAlertMessage_Object = MibScalar
phAlertMessage = _PhAlertMessage_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2, 1, 1, 6),
    _PhAlertMessage_Type()
)
phAlertMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phAlertMessage.setStatus("current")
_PhAlertDetail_Type = OctetString
_PhAlertDetail_Object = MibScalar
phAlertDetail = _PhAlertDetail_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2, 1, 1, 7),
    _PhAlertDetail_Type()
)
phAlertDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phAlertDetail.setStatus("current")
_PhAlertSource_Type = OctetString
_PhAlertSource_Object = MibScalar
phAlertSource = _PhAlertSource_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2, 1, 1, 8),
    _PhAlertSource_Type()
)
phAlertSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phAlertSource.setStatus("current")
_PhAlertTenant_Type = OctetString
_PhAlertTenant_Object = MibScalar
phAlertTenant = _PhAlertTenant_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 2, 1, 1, 9),
    _PhAlertTenant_Type()
)
phAlertTenant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phAlertTenant.setStatus("current")
_PumpHouseValues_ObjectIdentity = ObjectIdentity
pumpHouseValues = _PumpHouseValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3)
)
_PhVersion_ObjectIdentity = ObjectIdentity
phVersion = _PhVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 1)
)
_PhVersionParent_Type = OctetString
_PhVersionParent_Object = MibScalar
phVersionParent = _PhVersionParent_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 1, 1),
    _PhVersionParent_Type()
)
phVersionParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phVersionParent.setStatus("current")
_PhVersionBranch_Type = OctetString
_PhVersionBranch_Object = MibScalar
phVersionBranch = _PhVersionBranch_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 1, 2),
    _PhVersionBranch_Type()
)
phVersionBranch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phVersionBranch.setStatus("current")
_PhVersionCommit_Type = OctetString
_PhVersionCommit_Object = MibScalar
phVersionCommit = _PhVersionCommit_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 1, 3),
    _PhVersionCommit_Type()
)
phVersionCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phVersionCommit.setStatus("current")
_PhVersionSummary_Type = OctetString
_PhVersionSummary_Object = MibScalar
phVersionSummary = _PhVersionSummary_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 1, 4),
    _PhVersionSummary_Type()
)
phVersionSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phVersionSummary.setStatus("current")
_PhVersionTag_Type = OctetString
_PhVersionTag_Object = MibScalar
phVersionTag = _PhVersionTag_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 1, 5),
    _PhVersionTag_Type()
)
phVersionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phVersionTag.setStatus("current")
_PhVersionUpdate_Type = OctetString
_PhVersionUpdate_Object = MibScalar
phVersionUpdate = _PhVersionUpdate_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 1, 6),
    _PhVersionUpdate_Type()
)
phVersionUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phVersionUpdate.setStatus("current")
_PhVersionNumber_Type = OctetString
_PhVersionNumber_Object = MibScalar
phVersionNumber = _PhVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 1, 7),
    _PhVersionNumber_Type()
)
phVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phVersionNumber.setStatus("current")
_PhJvm_ObjectIdentity = ObjectIdentity
phJvm = _PhJvm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 2)
)
_PhJvmUptime_Type = OctetString
_PhJvmUptime_Object = MibScalar
phJvmUptime = _PhJvmUptime_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 2, 1),
    _PhJvmUptime_Type()
)
phJvmUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phJvmUptime.setStatus("current")
_PhJvmUsedMemory_Type = OctetString
_PhJvmUsedMemory_Object = MibScalar
phJvmUsedMemory = _PhJvmUsedMemory_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 2, 2),
    _PhJvmUsedMemory_Type()
)
phJvmUsedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phJvmUsedMemory.setStatus("current")
_PhJvmMaxMemory_Type = OctetString
_PhJvmMaxMemory_Object = MibScalar
phJvmMaxMemory = _PhJvmMaxMemory_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 2, 3),
    _PhJvmMaxMemory_Type()
)
phJvmMaxMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phJvmMaxMemory.setStatus("current")
_PhJvmUsedPermGen_Type = OctetString
_PhJvmUsedPermGen_Object = MibScalar
phJvmUsedPermGen = _PhJvmUsedPermGen_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 2, 4),
    _PhJvmUsedPermGen_Type()
)
phJvmUsedPermGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phJvmUsedPermGen.setStatus("current")
_PhJvmMaxPermGen_Type = OctetString
_PhJvmMaxPermGen_Object = MibScalar
phJvmMaxPermGen = _PhJvmMaxPermGen_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 2, 5),
    _PhJvmMaxPermGen_Type()
)
phJvmMaxPermGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phJvmMaxPermGen.setStatus("current")
_PhSystem_ObjectIdentity = ObjectIdentity
phSystem = _PhSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 3)
)
_PhSystemAvgLoad_Type = OctetString
_PhSystemAvgLoad_Object = MibScalar
phSystemAvgLoad = _PhSystemAvgLoad_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 3, 1),
    _PhSystemAvgLoad_Type()
)
phSystemAvgLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSystemAvgLoad.setStatus("current")
_PhSystemVersion_Type = OctetString
_PhSystemVersion_Object = MibScalar
phSystemVersion = _PhSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 3, 2),
    _PhSystemVersion_Type()
)
phSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phSystemVersion.setStatus("current")
_PhUsers_ObjectIdentity = ObjectIdentity
phUsers = _PhUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 5)
)
_PhUsersTotal_Type = OctetString
_PhUsersTotal_Object = MibScalar
phUsersTotal = _PhUsersTotal_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 5, 1),
    _PhUsersTotal_Type()
)
phUsersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phUsersTotal.setStatus("current")
_PhUsersActive_Type = OctetString
_PhUsersActive_Object = MibScalar
phUsersActive = _PhUsersActive_Object(
    (1, 3, 6, 1, 4, 1, 48935, 1, 3, 5, 2),
    _PhUsersActive_Type()
)
phUsersActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phUsersActive.setStatus("current")
_PumpHouseGroups_ObjectIdentity = ObjectIdentity
pumpHouseGroups = _PumpHouseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48935, 1, 4)
)

# Managed Objects groups

pumpHouseAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48935, 1, 4, 1)
)
pumpHouseAlertGroup.setObjects(
      *(("PUMPCO-PUMPHOUSE-MIB", "phAlertId"),
        ("PUMPCO-PUMPHOUSE-MIB", "phAlertDt"),
        ("PUMPCO-PUMPHOUSE-MIB", "phAlertUser"),
        ("PUMPCO-PUMPHOUSE-MIB", "phAlertCategory"),
        ("PUMPCO-PUMPHOUSE-MIB", "phAlertLevel"),
        ("PUMPCO-PUMPHOUSE-MIB", "phAlertMessage"),
        ("PUMPCO-PUMPHOUSE-MIB", "phAlertDetail"),
        ("PUMPCO-PUMPHOUSE-MIB", "phAlertSource"),
        ("PUMPCO-PUMPHOUSE-MIB", "phAlertTenant"))
)
if mibBuilder.loadTexts:
    pumpHouseAlertGroup.setStatus("current")

phVersionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48935, 1, 4, 2)
)
phVersionGroup.setObjects(
      *(("PUMPCO-PUMPHOUSE-MIB", "phVersionParent"),
        ("PUMPCO-PUMPHOUSE-MIB", "phVersionBranch"),
        ("PUMPCO-PUMPHOUSE-MIB", "phVersionCommit"),
        ("PUMPCO-PUMPHOUSE-MIB", "phVersionSummary"),
        ("PUMPCO-PUMPHOUSE-MIB", "phVersionTag"),
        ("PUMPCO-PUMPHOUSE-MIB", "phVersionUpdate"),
        ("PUMPCO-PUMPHOUSE-MIB", "phVersionNumber"))
)
if mibBuilder.loadTexts:
    phVersionGroup.setStatus("current")

phJvmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48935, 1, 4, 3)
)
phJvmGroup.setObjects(
      *(("PUMPCO-PUMPHOUSE-MIB", "phJvmUptime"),
        ("PUMPCO-PUMPHOUSE-MIB", "phJvmUsedMemory"),
        ("PUMPCO-PUMPHOUSE-MIB", "phJvmMaxMemory"),
        ("PUMPCO-PUMPHOUSE-MIB", "phJvmUsedPermGen"),
        ("PUMPCO-PUMPHOUSE-MIB", "phJvmMaxPermGen"))
)
if mibBuilder.loadTexts:
    phJvmGroup.setStatus("current")

phSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48935, 1, 4, 4)
)
phSystemGroup.setObjects(
      *(("PUMPCO-PUMPHOUSE-MIB", "phSystemAvgLoad"),
        ("PUMPCO-PUMPHOUSE-MIB", "phSystemVersion"))
)
if mibBuilder.loadTexts:
    phSystemGroup.setStatus("current")

phUsersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48935, 1, 4, 5)
)
phUsersGroup.setObjects(
      *(("PUMPCO-PUMPHOUSE-MIB", "phUsersTotal"),
        ("PUMPCO-PUMPHOUSE-MIB", "phUsersActive"))
)
if mibBuilder.loadTexts:
    phUsersGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PUMPCO-PUMPHOUSE-MIB",
    **{"pumpCo": pumpCo,
       "pumpHouse": pumpHouse,
       "pumpHouseTables": pumpHouseTables,
       "pumpHousePulseStatsTable": pumpHousePulseStatsTable,
       "pumpHousePulseStatsEntry": pumpHousePulseStatsEntry,
       "phPulseStatsClass": phPulseStatsClass,
       "phPulseStatsCount": phPulseStatsCount,
       "phPulseStatsFailures": phPulseStatsFailures,
       "phPulseStatsAvgTime": phPulseStatsAvgTime,
       "pumpHouseTraps": pumpHouseTraps,
       "pumpHouseAlertingTraps": pumpHouseAlertingTraps,
       "pumpHouseAlert": pumpHouseAlert,
       "phAlertId": phAlertId,
       "phAlertDt": phAlertDt,
       "phAlertUser": phAlertUser,
       "phAlertCategory": phAlertCategory,
       "phAlertLevel": phAlertLevel,
       "phAlertMessage": phAlertMessage,
       "phAlertDetail": phAlertDetail,
       "phAlertSource": phAlertSource,
       "phAlertTenant": phAlertTenant,
       "pumpHouseValues": pumpHouseValues,
       "phVersion": phVersion,
       "phVersionParent": phVersionParent,
       "phVersionBranch": phVersionBranch,
       "phVersionCommit": phVersionCommit,
       "phVersionSummary": phVersionSummary,
       "phVersionTag": phVersionTag,
       "phVersionUpdate": phVersionUpdate,
       "phVersionNumber": phVersionNumber,
       "phJvm": phJvm,
       "phJvmUptime": phJvmUptime,
       "phJvmUsedMemory": phJvmUsedMemory,
       "phJvmMaxMemory": phJvmMaxMemory,
       "phJvmUsedPermGen": phJvmUsedPermGen,
       "phJvmMaxPermGen": phJvmMaxPermGen,
       "phSystem": phSystem,
       "phSystemAvgLoad": phSystemAvgLoad,
       "phSystemVersion": phSystemVersion,
       "phUsers": phUsers,
       "phUsersTotal": phUsersTotal,
       "phUsersActive": phUsersActive,
       "pumpHouseGroups": pumpHouseGroups,
       "pumpHouseAlertGroup": pumpHouseAlertGroup,
       "phVersionGroup": phVersionGroup,
       "phJvmGroup": phJvmGroup,
       "phSystemGroup": phSystemGroup,
       "phUsersGroup": phUsersGroup}
)
