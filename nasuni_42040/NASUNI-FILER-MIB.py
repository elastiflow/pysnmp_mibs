# SNMP MIB module (NASUNI-FILER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/nasuni_42040/NASUNI-FILER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:36:21 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nasuni = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42040)
)
if mibBuilder.loadTexts:
    nasuni.setRevisions(
        ("2013-07-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Filer_ObjectIdentity = ObjectIdentity
filer = _Filer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 1)
)


class _FilerIdentifier_Type(DisplayString):
    """Custom type filerIdentifier based on DisplayString"""
    defaultValue = OctetString("Nasuni Filer")


_FilerIdentifier_Type.__name__ = "DisplayString"
_FilerIdentifier_Object = MibScalar
filerIdentifier = _FilerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 1),
    _FilerIdentifier_Type()
)
filerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerIdentifier.setStatus("current")
_FilerVersion_Type = DisplayString
_FilerVersion_Object = MibScalar
filerVersion = _FilerVersion_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 2),
    _FilerVersion_Type()
)
filerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerVersion.setStatus("current")
_FilerSerialNumber_Type = DisplayString
_FilerSerialNumber_Object = MibScalar
filerSerialNumber = _FilerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 3),
    _FilerSerialNumber_Type()
)
filerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerSerialNumber.setStatus("current")
_FilerUptime_Type = TimeTicks
_FilerUptime_Object = MibScalar
filerUptime = _FilerUptime_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 4),
    _FilerUptime_Type()
)
filerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerUptime.setStatus("current")
_FilerUpdateAvailable_Type = DisplayString
_FilerUpdateAvailable_Object = MibScalar
filerUpdateAvailable = _FilerUpdateAvailable_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 5),
    _FilerUpdateAvailable_Type()
)
filerUpdateAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerUpdateAvailable.setStatus("current")
_FilerTotalUnprotectedData_Type = Counter64
_FilerTotalUnprotectedData_Object = MibScalar
filerTotalUnprotectedData = _FilerTotalUnprotectedData_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 6),
    _FilerTotalUnprotectedData_Type()
)
filerTotalUnprotectedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalUnprotectedData.setStatus("current")
if mibBuilder.loadTexts:
    filerTotalUnprotectedData.setUnits("bytes")
_FilerPushesCompleted_Type = Counter64
_FilerPushesCompleted_Object = MibScalar
filerPushesCompleted = _FilerPushesCompleted_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 7),
    _FilerPushesCompleted_Type()
)
filerPushesCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerPushesCompleted.setStatus("current")
_FilerTotalPushed_Type = Counter64
_FilerTotalPushed_Object = MibScalar
filerTotalPushed = _FilerTotalPushed_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 8),
    _FilerTotalPushed_Type()
)
filerTotalPushed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalPushed.setStatus("current")
if mibBuilder.loadTexts:
    filerTotalPushed.setUnits("bytes")
_FilerTotalRead_Type = Counter64
_FilerTotalRead_Object = MibScalar
filerTotalRead = _FilerTotalRead_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 9),
    _FilerTotalRead_Type()
)
filerTotalRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalRead.setStatus("current")
if mibBuilder.loadTexts:
    filerTotalRead.setUnits("bytes")
_FilerOpensForRead_Type = Counter64
_FilerOpensForRead_Object = MibScalar
filerOpensForRead = _FilerOpensForRead_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 10),
    _FilerOpensForRead_Type()
)
filerOpensForRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerOpensForRead.setStatus("current")
_FilerOpensForWrite_Type = Counter64
_FilerOpensForWrite_Object = MibScalar
filerOpensForWrite = _FilerOpensForWrite_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 11),
    _FilerOpensForWrite_Type()
)
filerOpensForWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerOpensForWrite.setStatus("current")
_FilerMergeConflicts_Type = Counter64
_FilerMergeConflicts_Object = MibScalar
filerMergeConflicts = _FilerMergeConflicts_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 12),
    _FilerMergeConflicts_Type()
)
filerMergeConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerMergeConflicts.setStatus("current")
_FilerReadHits_Type = Counter64
_FilerReadHits_Object = MibScalar
filerReadHits = _FilerReadHits_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 13),
    _FilerReadHits_Type()
)
filerReadHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerReadHits.setStatus("current")
_FilerReadMisses_Type = Counter64
_FilerReadMisses_Object = MibScalar
filerReadMisses = _FilerReadMisses_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 14),
    _FilerReadMisses_Type()
)
filerReadMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerReadMisses.setStatus("current")
_FilerNextFsckAfter_Type = DisplayString
_FilerNextFsckAfter_Object = MibScalar
filerNextFsckAfter = _FilerNextFsckAfter_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 15),
    _FilerNextFsckAfter_Type()
)
filerNextFsckAfter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerNextFsckAfter.setStatus("current")
_FilerCache_ObjectIdentity = ObjectIdentity
filerCache = _FilerCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 1, 100)
)
_FilerCacheTotal_Type = Counter64
_FilerCacheTotal_Object = MibScalar
filerCacheTotal = _FilerCacheTotal_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 100, 1),
    _FilerCacheTotal_Type()
)
filerCacheTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerCacheTotal.setStatus("current")
if mibBuilder.loadTexts:
    filerCacheTotal.setUnits("bytes")
_FilerCacheUsed_Type = Counter64
_FilerCacheUsed_Object = MibScalar
filerCacheUsed = _FilerCacheUsed_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 100, 2),
    _FilerCacheUsed_Type()
)
filerCacheUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerCacheUsed.setStatus("current")
if mibBuilder.loadTexts:
    filerCacheUsed.setUnits("bytes")
_FilerCacheFree_Type = Counter64
_FilerCacheFree_Object = MibScalar
filerCacheFree = _FilerCacheFree_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 100, 3),
    _FilerCacheFree_Type()
)
filerCacheFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerCacheFree.setStatus("current")
if mibBuilder.loadTexts:
    filerCacheFree.setUnits("bytes")
_FilerPlatform_ObjectIdentity = ObjectIdentity
filerPlatform = _FilerPlatform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101)
)
_FilerPlatformName_Type = DisplayString
_FilerPlatformName_Object = MibScalar
filerPlatformName = _FilerPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101, 1),
    _FilerPlatformName_Type()
)
filerPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerPlatformName.setStatus("current")
_FilerPlatformType_Type = DisplayString
_FilerPlatformType_Object = MibScalar
filerPlatformType = _FilerPlatformType_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101, 2),
    _FilerPlatformType_Type()
)
filerPlatformType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerPlatformType.setStatus("current")
_FilerPackageFormat_Type = DisplayString
_FilerPackageFormat_Object = MibScalar
filerPackageFormat = _FilerPackageFormat_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101, 3),
    _FilerPackageFormat_Type()
)
filerPackageFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerPackageFormat.setStatus("current")
_FilerBiosVersion_Type = DisplayString
_FilerBiosVersion_Object = MibScalar
filerBiosVersion = _FilerBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101, 4),
    _FilerBiosVersion_Type()
)
filerBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerBiosVersion.setStatus("current")
_FilerCpuModel_Type = DisplayString
_FilerCpuModel_Object = MibScalar
filerCpuModel = _FilerCpuModel_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101, 5),
    _FilerCpuModel_Type()
)
filerCpuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerCpuModel.setStatus("current")
_FilerPhysCpuCount_Type = Integer32
_FilerPhysCpuCount_Object = MibScalar
filerPhysCpuCount = _FilerPhysCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101, 6),
    _FilerPhysCpuCount_Type()
)
filerPhysCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerPhysCpuCount.setStatus("current")
_FilerCoreCount_Type = Integer32
_FilerCoreCount_Object = MibScalar
filerCoreCount = _FilerCoreCount_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101, 7),
    _FilerCoreCount_Type()
)
filerCoreCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerCoreCount.setStatus("current")
_FilerCpuArch_Type = DisplayString
_FilerCpuArch_Object = MibScalar
filerCpuArch = _FilerCpuArch_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101, 8),
    _FilerCpuArch_Type()
)
filerCpuArch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerCpuArch.setStatus("current")
_FilerCpuFreq_Type = Counter64
_FilerCpuFreq_Object = MibScalar
filerCpuFreq = _FilerCpuFreq_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101, 9),
    _FilerCpuFreq_Type()
)
filerCpuFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerCpuFreq.setStatus("current")
if mibBuilder.loadTexts:
    filerCpuFreq.setUnits("hertz")
_FilerDiskCount_Type = Integer32
_FilerDiskCount_Object = MibScalar
filerDiskCount = _FilerDiskCount_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101, 10),
    _FilerDiskCount_Type()
)
filerDiskCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerDiskCount.setStatus("current")
_FilerTotalMemory_Type = Counter64
_FilerTotalMemory_Object = MibScalar
filerTotalMemory = _FilerTotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 101, 11),
    _FilerTotalMemory_Type()
)
filerTotalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalMemory.setStatus("current")
if mibBuilder.loadTexts:
    filerTotalMemory.setUnits("bytes")
_FilerHealth_ObjectIdentity = ObjectIdentity
filerHealth = _FilerHealth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 1, 102)
)
_FilerAmbientTemp_Type = Integer32
_FilerAmbientTemp_Object = MibScalar
filerAmbientTemp = _FilerAmbientTemp_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 102, 1),
    _FilerAmbientTemp_Type()
)
filerAmbientTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerAmbientTemp.setStatus("current")
if mibBuilder.loadTexts:
    filerAmbientTemp.setUnits("degrees celsius")
_FilerInletTemp_Type = Integer32
_FilerInletTemp_Object = MibScalar
filerInletTemp = _FilerInletTemp_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 102, 2),
    _FilerInletTemp_Type()
)
filerInletTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerInletTemp.setStatus("current")
if mibBuilder.loadTexts:
    filerInletTemp.setUnits("degrees celsius")
_FilerExhaustTemp_Type = Integer32
_FilerExhaustTemp_Object = MibScalar
filerExhaustTemp = _FilerExhaustTemp_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 102, 3),
    _FilerExhaustTemp_Type()
)
filerExhaustTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerExhaustTemp.setStatus("current")
if mibBuilder.loadTexts:
    filerExhaustTemp.setUnits("degrees celsius")
_FilerNumPowerSupplies_Type = Integer32
_FilerNumPowerSupplies_Object = MibScalar
filerNumPowerSupplies = _FilerNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 102, 4),
    _FilerNumPowerSupplies_Type()
)
filerNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerNumPowerSupplies.setStatus("current")
_FilerPowerSupplyErrors_Type = Integer32
_FilerPowerSupplyErrors_Object = MibScalar
filerPowerSupplyErrors = _FilerPowerSupplyErrors_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 102, 5),
    _FilerPowerSupplyErrors_Type()
)
filerPowerSupplyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerPowerSupplyErrors.setStatus("current")
_FilerNumRaidArrays_Type = Integer32
_FilerNumRaidArrays_Object = MibScalar
filerNumRaidArrays = _FilerNumRaidArrays_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 102, 6),
    _FilerNumRaidArrays_Type()
)
filerNumRaidArrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerNumRaidArrays.setStatus("current")
_FilerRaidArrayErrors_Type = Integer32
_FilerRaidArrayErrors_Object = MibScalar
filerRaidArrayErrors = _FilerRaidArrayErrors_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 102, 7),
    _FilerRaidArrayErrors_Type()
)
filerRaidArrayErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerRaidArrayErrors.setStatus("current")
_FilerNumRaidDisks_Type = Integer32
_FilerNumRaidDisks_Object = MibScalar
filerNumRaidDisks = _FilerNumRaidDisks_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 102, 8),
    _FilerNumRaidDisks_Type()
)
filerNumRaidDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerNumRaidDisks.setStatus("current")
_FilerRaidDiskErrors_Type = Integer32
_FilerRaidDiskErrors_Object = MibScalar
filerRaidDiskErrors = _FilerRaidDiskErrors_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 102, 9),
    _FilerRaidDiskErrors_Type()
)
filerRaidDiskErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerRaidDiskErrors.setStatus("current")
_FilerCifs_ObjectIdentity = ObjectIdentity
filerCifs = _FilerCifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 1, 103)
)
_FilerTotalShares_Type = Integer32
_FilerTotalShares_Object = MibScalar
filerTotalShares = _FilerTotalShares_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 103, 1),
    _FilerTotalShares_Type()
)
filerTotalShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalShares.setStatus("current")
_FilerTotalShareLocks_Type = Integer32
_FilerTotalShareLocks_Object = MibScalar
filerTotalShareLocks = _FilerTotalShareLocks_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 103, 2),
    _FilerTotalShareLocks_Type()
)
filerTotalShareLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalShareLocks.setStatus("current")
_FilerTotalShareClients_Type = Integer32
_FilerTotalShareClients_Object = MibScalar
filerTotalShareClients = _FilerTotalShareClients_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 103, 3),
    _FilerTotalShareClients_Type()
)
filerTotalShareClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalShareClients.setStatus("current")
_FilerNfs_ObjectIdentity = ObjectIdentity
filerNfs = _FilerNfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 1, 104)
)
_FilerTotalExports_Type = Integer32
_FilerTotalExports_Object = MibScalar
filerTotalExports = _FilerTotalExports_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 104, 1),
    _FilerTotalExports_Type()
)
filerTotalExports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalExports.setStatus("current")
_FilerIscsi_ObjectIdentity = ObjectIdentity
filerIscsi = _FilerIscsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 1, 105)
)
_FilerTotalIscsiTargets_Type = Integer32
_FilerTotalIscsiTargets_Object = MibScalar
filerTotalIscsiTargets = _FilerTotalIscsiTargets_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 105, 1),
    _FilerTotalIscsiTargets_Type()
)
filerTotalIscsiTargets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalIscsiTargets.setStatus("current")
_FilerTotalIscsiClients_Type = Integer32
_FilerTotalIscsiClients_Object = MibScalar
filerTotalIscsiClients = _FilerTotalIscsiClients_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 105, 2),
    _FilerTotalIscsiClients_Type()
)
filerTotalIscsiClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalIscsiClients.setStatus("current")
_FilerMobile_ObjectIdentity = ObjectIdentity
filerMobile = _FilerMobile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 1, 106)
)
_FilerTotalMobileLicenses_Type = Integer32
_FilerTotalMobileLicenses_Object = MibScalar
filerTotalMobileLicenses = _FilerTotalMobileLicenses_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 106, 1),
    _FilerTotalMobileLicenses_Type()
)
filerTotalMobileLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalMobileLicenses.setStatus("current")
_FilerNumIOSLicenses_Type = Integer32
_FilerNumIOSLicenses_Object = MibScalar
filerNumIOSLicenses = _FilerNumIOSLicenses_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 106, 2),
    _FilerNumIOSLicenses_Type()
)
filerNumIOSLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerNumIOSLicenses.setStatus("current")
_FilerNumAndroidLicenses_Type = Integer32
_FilerNumAndroidLicenses_Object = MibScalar
filerNumAndroidLicenses = _FilerNumAndroidLicenses_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 106, 3),
    _FilerNumAndroidLicenses_Type()
)
filerNumAndroidLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerNumAndroidLicenses.setStatus("current")
_FilerServices_ObjectIdentity = ObjectIdentity
filerServices = _FilerServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 1, 107)
)
_FilerSupportServiceEnabled_Type = Integer32
_FilerSupportServiceEnabled_Object = MibScalar
filerSupportServiceEnabled = _FilerSupportServiceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 107, 1),
    _FilerSupportServiceEnabled_Type()
)
filerSupportServiceEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerSupportServiceEnabled.setStatus("current")
_FilerSupportServiceConnected_Type = Integer32
_FilerSupportServiceConnected_Object = MibScalar
filerSupportServiceConnected = _FilerSupportServiceConnected_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 107, 2),
    _FilerSupportServiceConnected_Type()
)
filerSupportServiceConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerSupportServiceConnected.setStatus("current")
_FilerSupportServiceRunning_Type = Integer32
_FilerSupportServiceRunning_Object = MibScalar
filerSupportServiceRunning = _FilerSupportServiceRunning_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 107, 3),
    _FilerSupportServiceRunning_Type()
)
filerSupportServiceRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerSupportServiceRunning.setStatus("current")
_FilerSupportServiceTimeout_Type = Integer32
_FilerSupportServiceTimeout_Object = MibScalar
filerSupportServiceTimeout = _FilerSupportServiceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 107, 4),
    _FilerSupportServiceTimeout_Type()
)
filerSupportServiceTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerSupportServiceTimeout.setStatus("current")
if mibBuilder.loadTexts:
    filerSupportServiceTimeout.setUnits("seconds")
_FilerNetwork_ObjectIdentity = ObjectIdentity
filerNetwork = _FilerNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 1, 108)
)
_FilerCloudOut_Type = Counter64
_FilerCloudOut_Object = MibScalar
filerCloudOut = _FilerCloudOut_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 108, 1),
    _FilerCloudOut_Type()
)
filerCloudOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerCloudOut.setStatus("current")
if mibBuilder.loadTexts:
    filerCloudOut.setUnits("bits/second")
_FilerCloudIn_Type = Counter64
_FilerCloudIn_Object = MibScalar
filerCloudIn = _FilerCloudIn_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 108, 2),
    _FilerCloudIn_Type()
)
filerCloudIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerCloudIn.setStatus("current")
if mibBuilder.loadTexts:
    filerCloudIn.setUnits("bits/second")
_FilerMobileOut_Type = Counter64
_FilerMobileOut_Object = MibScalar
filerMobileOut = _FilerMobileOut_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 108, 3),
    _FilerMobileOut_Type()
)
filerMobileOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerMobileOut.setStatus("current")
if mibBuilder.loadTexts:
    filerMobileOut.setUnits("bits/second")
_FilerMobileIn_Type = Counter64
_FilerMobileIn_Object = MibScalar
filerMobileIn = _FilerMobileIn_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 108, 4),
    _FilerMobileIn_Type()
)
filerMobileIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerMobileIn.setStatus("current")
if mibBuilder.loadTexts:
    filerMobileIn.setUnits("bits/second")
_FilerUIOut_Type = Counter64
_FilerUIOut_Object = MibScalar
filerUIOut = _FilerUIOut_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 108, 5),
    _FilerUIOut_Type()
)
filerUIOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerUIOut.setStatus("current")
if mibBuilder.loadTexts:
    filerUIOut.setUnits("bits/second")
_FilerUIIn_Type = Counter64
_FilerUIIn_Object = MibScalar
filerUIIn = _FilerUIIn_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 108, 6),
    _FilerUIIn_Type()
)
filerUIIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerUIIn.setStatus("current")
if mibBuilder.loadTexts:
    filerUIIn.setUnits("bits/second")
_FilerClientsOut_Type = Counter64
_FilerClientsOut_Object = MibScalar
filerClientsOut = _FilerClientsOut_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 108, 7),
    _FilerClientsOut_Type()
)
filerClientsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerClientsOut.setStatus("current")
if mibBuilder.loadTexts:
    filerClientsOut.setUnits("bits/second")
_FilerClientsIn_Type = Counter64
_FilerClientsIn_Object = MibScalar
filerClientsIn = _FilerClientsIn_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 108, 8),
    _FilerClientsIn_Type()
)
filerClientsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerClientsIn.setStatus("current")
if mibBuilder.loadTexts:
    filerClientsIn.setUnits("bits/second")
_FilerMigrationOut_Type = Counter64
_FilerMigrationOut_Object = MibScalar
filerMigrationOut = _FilerMigrationOut_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 108, 9),
    _FilerMigrationOut_Type()
)
filerMigrationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerMigrationOut.setStatus("current")
if mibBuilder.loadTexts:
    filerMigrationOut.setUnits("bits/second")
_FilerMigrationIn_Type = Counter64
_FilerMigrationIn_Object = MibScalar
filerMigrationIn = _FilerMigrationIn_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 108, 10),
    _FilerMigrationIn_Type()
)
filerMigrationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerMigrationIn.setStatus("current")
if mibBuilder.loadTexts:
    filerMigrationIn.setUnits("bits/second")
_FilerFtp_ObjectIdentity = ObjectIdentity
filerFtp = _FilerFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 1, 109)
)
_FilerTotalFtpdirs_Type = Integer32
_FilerTotalFtpdirs_Object = MibScalar
filerTotalFtpdirs = _FilerTotalFtpdirs_Object(
    (1, 3, 6, 1, 4, 1, 42040, 1, 109, 1),
    _FilerTotalFtpdirs_Type()
)
filerTotalFtpdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTotalFtpdirs.setStatus("current")
_Volumes_ObjectIdentity = ObjectIdentity
volumes = _Volumes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 2)
)
_VolumeCount_Type = Integer32
_VolumeCount_Object = MibScalar
volumeCount = _VolumeCount_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 1),
    _VolumeCount_Type()
)
volumeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeCount.setStatus("current")
_VolumeTable_Object = MibTable
volumeTable = _VolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2)
)
if mibBuilder.loadTexts:
    volumeTable.setStatus("current")
_VolumeTableEntry_Object = MibTableRow
volumeTableEntry = _VolumeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1)
)
volumeTableEntry.setIndexNames(
    (0, "NASUNI-FILER-MIB", "volumeTableIndex"),
)
if mibBuilder.loadTexts:
    volumeTableEntry.setStatus("current")


class _VolumeTableIndex_Type(Integer32):
    """Custom type volumeTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_VolumeTableIndex_Type.__name__ = "Integer32"
_VolumeTableIndex_Object = MibTableColumn
volumeTableIndex = _VolumeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 1),
    _VolumeTableIndex_Type()
)
volumeTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    volumeTableIndex.setStatus("current")
_VolumeTableDescription_Type = DisplayString
_VolumeTableDescription_Object = MibTableColumn
volumeTableDescription = _VolumeTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 2),
    _VolumeTableDescription_Type()
)
volumeTableDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableDescription.setStatus("current")
_VolumeTableProvider_Type = DisplayString
_VolumeTableProvider_Object = MibTableColumn
volumeTableProvider = _VolumeTableProvider_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 3),
    _VolumeTableProvider_Type()
)
volumeTableProvider.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableProvider.setStatus("current")
_VolumeTableProtocol_Type = DisplayString
_VolumeTableProtocol_Object = MibTableColumn
volumeTableProtocol = _VolumeTableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 4),
    _VolumeTableProtocol_Type()
)
volumeTableProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableProtocol.setStatus("current")
_VolumeTableStatus_Type = DisplayString
_VolumeTableStatus_Object = MibTableColumn
volumeTableStatus = _VolumeTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 5),
    _VolumeTableStatus_Type()
)
volumeTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableStatus.setStatus("current")
_VolumeTableAccessibleData_Type = Counter64
_VolumeTableAccessibleData_Object = MibTableColumn
volumeTableAccessibleData = _VolumeTableAccessibleData_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 6),
    _VolumeTableAccessibleData_Type()
)
volumeTableAccessibleData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableAccessibleData.setStatus("current")
if mibBuilder.loadTexts:
    volumeTableAccessibleData.setUnits("bytes")
_VolumeTableUnprotectedData_Type = Counter64
_VolumeTableUnprotectedData_Object = MibTableColumn
volumeTableUnprotectedData = _VolumeTableUnprotectedData_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 7),
    _VolumeTableUnprotectedData_Type()
)
volumeTableUnprotectedData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableUnprotectedData.setStatus("current")
if mibBuilder.loadTexts:
    volumeTableUnprotectedData.setUnits("bytes")
_VolumeTableLastSnapshotStart_Type = DisplayString
_VolumeTableLastSnapshotStart_Object = MibTableColumn
volumeTableLastSnapshotStart = _VolumeTableLastSnapshotStart_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 8),
    _VolumeTableLastSnapshotStart_Type()
)
volumeTableLastSnapshotStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableLastSnapshotStart.setStatus("current")
_VolumeTableLastSnapshotEnd_Type = DisplayString
_VolumeTableLastSnapshotEnd_Object = MibTableColumn
volumeTableLastSnapshotEnd = _VolumeTableLastSnapshotEnd_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 9),
    _VolumeTableLastSnapshotEnd_Type()
)
volumeTableLastSnapshotEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableLastSnapshotEnd.setStatus("current")
_VolumeTableLastSnapshotDuration_Type = Integer32
_VolumeTableLastSnapshotDuration_Object = MibTableColumn
volumeTableLastSnapshotDuration = _VolumeTableLastSnapshotDuration_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 10),
    _VolumeTableLastSnapshotDuration_Type()
)
volumeTableLastSnapshotDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableLastSnapshotDuration.setStatus("current")
if mibBuilder.loadTexts:
    volumeTableLastSnapshotDuration.setUnits("seconds")
_VolumeTableLastSnapshotVersion_Type = Counter64
_VolumeTableLastSnapshotVersion_Object = MibTableColumn
volumeTableLastSnapshotVersion = _VolumeTableLastSnapshotVersion_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 11),
    _VolumeTableLastSnapshotVersion_Type()
)
volumeTableLastSnapshotVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableLastSnapshotVersion.setStatus("current")
_VolumeTableIsActive_Type = Integer32
_VolumeTableIsActive_Object = MibTableColumn
volumeTableIsActive = _VolumeTableIsActive_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 12),
    _VolumeTableIsActive_Type()
)
volumeTableIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableIsActive.setStatus("current")
_VolumeTableIsShared_Type = Integer32
_VolumeTableIsShared_Object = MibTableColumn
volumeTableIsShared = _VolumeTableIsShared_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 13),
    _VolumeTableIsShared_Type()
)
volumeTableIsShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableIsShared.setStatus("current")
_VolumeTableIsReadOnly_Type = Integer32
_VolumeTableIsReadOnly_Object = MibTableColumn
volumeTableIsReadOnly = _VolumeTableIsReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 14),
    _VolumeTableIsReadOnly_Type()
)
volumeTableIsReadOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableIsReadOnly.setStatus("current")
_VolumeTableIsPinned_Type = Integer32
_VolumeTableIsPinned_Object = MibTableColumn
volumeTableIsPinned = _VolumeTableIsPinned_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 15),
    _VolumeTableIsPinned_Type()
)
volumeTableIsPinned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableIsPinned.setStatus("current")
_VolumeTableIsRemote_Type = Integer32
_VolumeTableIsRemote_Object = MibTableColumn
volumeTableIsRemote = _VolumeTableIsRemote_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 16),
    _VolumeTableIsRemote_Type()
)
volumeTableIsRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableIsRemote.setStatus("current")
_VolumeTableAvEnabled_Type = Integer32
_VolumeTableAvEnabled_Object = MibTableColumn
volumeTableAvEnabled = _VolumeTableAvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 17),
    _VolumeTableAvEnabled_Type()
)
volumeTableAvEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableAvEnabled.setStatus("current")
_VolumeTableRemoteAccessEnabled_Type = Integer32
_VolumeTableRemoteAccessEnabled_Object = MibTableColumn
volumeTableRemoteAccessEnabled = _VolumeTableRemoteAccessEnabled_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 18),
    _VolumeTableRemoteAccessEnabled_Type()
)
volumeTableRemoteAccessEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableRemoteAccessEnabled.setStatus("current")
_VolumeTableQuota_Type = Counter64
_VolumeTableQuota_Object = MibTableColumn
volumeTableQuota = _VolumeTableQuota_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 19),
    _VolumeTableQuota_Type()
)
volumeTableQuota.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableQuota.setStatus("current")
if mibBuilder.loadTexts:
    volumeTableQuota.setUnits("bytes")
_VolumeTableNumAVViolations_Type = Counter64
_VolumeTableNumAVViolations_Object = MibTableColumn
volumeTableNumAVViolations = _VolumeTableNumAVViolations_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 20),
    _VolumeTableNumAVViolations_Type()
)
volumeTableNumAVViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableNumAVViolations.setStatus("current")
_VolumeTableNumFileAlerts_Type = Counter64
_VolumeTableNumFileAlerts_Object = MibTableColumn
volumeTableNumFileAlerts = _VolumeTableNumFileAlerts_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 21),
    _VolumeTableNumFileAlerts_Type()
)
volumeTableNumFileAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableNumFileAlerts.setStatus("current")
_VolumeTableNumExports_Type = Integer32
_VolumeTableNumExports_Object = MibTableColumn
volumeTableNumExports = _VolumeTableNumExports_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 22),
    _VolumeTableNumExports_Type()
)
volumeTableNumExports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableNumExports.setStatus("current")
_VolumeTableNumShares_Type = Integer32
_VolumeTableNumShares_Object = MibTableColumn
volumeTableNumShares = _VolumeTableNumShares_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 23),
    _VolumeTableNumShares_Type()
)
volumeTableNumShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableNumShares.setStatus("current")
_VolumeTableNumFtpdirs_Type = Integer32
_VolumeTableNumFtpdirs_Object = MibTableColumn
volumeTableNumFtpdirs = _VolumeTableNumFtpdirs_Object(
    (1, 3, 6, 1, 4, 1, 42040, 2, 2, 1, 24),
    _VolumeTableNumFtpdirs_Type()
)
volumeTableNumFtpdirs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    volumeTableNumFtpdirs.setStatus("current")
_Account_ObjectIdentity = ObjectIdentity
account = _Account_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 3)
)
_AccountLicensedCapacity_Type = Counter64
_AccountLicensedCapacity_Object = MibScalar
accountLicensedCapacity = _AccountLicensedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 42040, 3, 1),
    _AccountLicensedCapacity_Type()
)
accountLicensedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountLicensedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    accountLicensedCapacity.setUnits("bytes")
_AccountUsedCapacity_Type = Counter64
_AccountUsedCapacity_Object = MibScalar
accountUsedCapacity = _AccountUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 42040, 3, 2),
    _AccountUsedCapacity_Type()
)
accountUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountUsedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    accountUsedCapacity.setUnits("bytes")
_AccountPercentUsedCapacity_Type = Integer32
_AccountPercentUsedCapacity_Object = MibScalar
accountPercentUsedCapacity = _AccountPercentUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 42040, 3, 3),
    _AccountPercentUsedCapacity_Type()
)
accountPercentUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accountPercentUsedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    accountPercentUsedCapacity.setUnits("percent")
_FilerTrapsWrap_ObjectIdentity = ObjectIdentity
filerTrapsWrap = _FilerTrapsWrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 100)
)
_FilerTraps_ObjectIdentity = ObjectIdentity
filerTraps = _FilerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42040, 100, 0)
)
_FilerTrapType_Type = DisplayString
_FilerTrapType_Object = MibScalar
filerTrapType = _FilerTrapType_Object(
    (1, 3, 6, 1, 4, 1, 42040, 100, 0, 1),
    _FilerTrapType_Type()
)
filerTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTrapType.setStatus("current")
_FilerTrapLevel_Type = DisplayString
_FilerTrapLevel_Object = MibScalar
filerTrapLevel = _FilerTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 42040, 100, 0, 2),
    _FilerTrapLevel_Type()
)
filerTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTrapLevel.setStatus("current")
_FilerTrapMessage_Type = DisplayString
_FilerTrapMessage_Object = MibScalar
filerTrapMessage = _FilerTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 42040, 100, 0, 3),
    _FilerTrapMessage_Type()
)
filerTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filerTrapMessage.setStatus("current")

# Managed Objects groups


# Notification objects

filerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42040, 100, 0, 4)
)
filerTrap.setObjects(
      *(("NASUNI-FILER-MIB", "filerTrapType"),
        ("NASUNI-FILER-MIB", "filerTrapLevel"),
        ("NASUNI-FILER-MIB", "filerTrapMessage"))
)
if mibBuilder.loadTexts:
    filerTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NASUNI-FILER-MIB",
    **{"nasuni": nasuni,
       "filer": filer,
       "filerIdentifier": filerIdentifier,
       "filerVersion": filerVersion,
       "filerSerialNumber": filerSerialNumber,
       "filerUptime": filerUptime,
       "filerUpdateAvailable": filerUpdateAvailable,
       "filerTotalUnprotectedData": filerTotalUnprotectedData,
       "filerPushesCompleted": filerPushesCompleted,
       "filerTotalPushed": filerTotalPushed,
       "filerTotalRead": filerTotalRead,
       "filerOpensForRead": filerOpensForRead,
       "filerOpensForWrite": filerOpensForWrite,
       "filerMergeConflicts": filerMergeConflicts,
       "filerReadHits": filerReadHits,
       "filerReadMisses": filerReadMisses,
       "filerNextFsckAfter": filerNextFsckAfter,
       "filerCache": filerCache,
       "filerCacheTotal": filerCacheTotal,
       "filerCacheUsed": filerCacheUsed,
       "filerCacheFree": filerCacheFree,
       "filerPlatform": filerPlatform,
       "filerPlatformName": filerPlatformName,
       "filerPlatformType": filerPlatformType,
       "filerPackageFormat": filerPackageFormat,
       "filerBiosVersion": filerBiosVersion,
       "filerCpuModel": filerCpuModel,
       "filerPhysCpuCount": filerPhysCpuCount,
       "filerCoreCount": filerCoreCount,
       "filerCpuArch": filerCpuArch,
       "filerCpuFreq": filerCpuFreq,
       "filerDiskCount": filerDiskCount,
       "filerTotalMemory": filerTotalMemory,
       "filerHealth": filerHealth,
       "filerAmbientTemp": filerAmbientTemp,
       "filerInletTemp": filerInletTemp,
       "filerExhaustTemp": filerExhaustTemp,
       "filerNumPowerSupplies": filerNumPowerSupplies,
       "filerPowerSupplyErrors": filerPowerSupplyErrors,
       "filerNumRaidArrays": filerNumRaidArrays,
       "filerRaidArrayErrors": filerRaidArrayErrors,
       "filerNumRaidDisks": filerNumRaidDisks,
       "filerRaidDiskErrors": filerRaidDiskErrors,
       "filerCifs": filerCifs,
       "filerTotalShares": filerTotalShares,
       "filerTotalShareLocks": filerTotalShareLocks,
       "filerTotalShareClients": filerTotalShareClients,
       "filerNfs": filerNfs,
       "filerTotalExports": filerTotalExports,
       "filerIscsi": filerIscsi,
       "filerTotalIscsiTargets": filerTotalIscsiTargets,
       "filerTotalIscsiClients": filerTotalIscsiClients,
       "filerMobile": filerMobile,
       "filerTotalMobileLicenses": filerTotalMobileLicenses,
       "filerNumIOSLicenses": filerNumIOSLicenses,
       "filerNumAndroidLicenses": filerNumAndroidLicenses,
       "filerServices": filerServices,
       "filerSupportServiceEnabled": filerSupportServiceEnabled,
       "filerSupportServiceConnected": filerSupportServiceConnected,
       "filerSupportServiceRunning": filerSupportServiceRunning,
       "filerSupportServiceTimeout": filerSupportServiceTimeout,
       "filerNetwork": filerNetwork,
       "filerCloudOut": filerCloudOut,
       "filerCloudIn": filerCloudIn,
       "filerMobileOut": filerMobileOut,
       "filerMobileIn": filerMobileIn,
       "filerUIOut": filerUIOut,
       "filerUIIn": filerUIIn,
       "filerClientsOut": filerClientsOut,
       "filerClientsIn": filerClientsIn,
       "filerMigrationOut": filerMigrationOut,
       "filerMigrationIn": filerMigrationIn,
       "filerFtp": filerFtp,
       "filerTotalFtpdirs": filerTotalFtpdirs,
       "volumes": volumes,
       "volumeCount": volumeCount,
       "volumeTable": volumeTable,
       "volumeTableEntry": volumeTableEntry,
       "volumeTableIndex": volumeTableIndex,
       "volumeTableDescription": volumeTableDescription,
       "volumeTableProvider": volumeTableProvider,
       "volumeTableProtocol": volumeTableProtocol,
       "volumeTableStatus": volumeTableStatus,
       "volumeTableAccessibleData": volumeTableAccessibleData,
       "volumeTableUnprotectedData": volumeTableUnprotectedData,
       "volumeTableLastSnapshotStart": volumeTableLastSnapshotStart,
       "volumeTableLastSnapshotEnd": volumeTableLastSnapshotEnd,
       "volumeTableLastSnapshotDuration": volumeTableLastSnapshotDuration,
       "volumeTableLastSnapshotVersion": volumeTableLastSnapshotVersion,
       "volumeTableIsActive": volumeTableIsActive,
       "volumeTableIsShared": volumeTableIsShared,
       "volumeTableIsReadOnly": volumeTableIsReadOnly,
       "volumeTableIsPinned": volumeTableIsPinned,
       "volumeTableIsRemote": volumeTableIsRemote,
       "volumeTableAvEnabled": volumeTableAvEnabled,
       "volumeTableRemoteAccessEnabled": volumeTableRemoteAccessEnabled,
       "volumeTableQuota": volumeTableQuota,
       "volumeTableNumAVViolations": volumeTableNumAVViolations,
       "volumeTableNumFileAlerts": volumeTableNumFileAlerts,
       "volumeTableNumExports": volumeTableNumExports,
       "volumeTableNumShares": volumeTableNumShares,
       "volumeTableNumFtpdirs": volumeTableNumFtpdirs,
       "account": account,
       "accountLicensedCapacity": accountLicensedCapacity,
       "accountUsedCapacity": accountUsedCapacity,
       "accountPercentUsedCapacity": accountPercentUsedCapacity,
       "filerTrapsWrap": filerTrapsWrap,
       "filerTraps": filerTraps,
       "filerTrapType": filerTrapType,
       "filerTrapLevel": filerTrapLevel,
       "filerTrapMessage": filerTrapMessage,
       "filerTrap": filerTrap}
)
