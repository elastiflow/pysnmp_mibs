# SNMP MIB module (CISCO-LICENSE-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LICENSE-MGR-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:47:33 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

ciscoLicenseMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369)
)
if mibBuilder.loadTexts:
    ciscoLicenseMgrMIB.setRevisions(
        ("2008-11-04 00:00",
         "2008-04-22 00:00",
         "2007-08-02 00:00",
         "2006-12-17 00:00",
         "2005-09-30 00:00",
         "2004-12-01 00:00",
         "2004-07-20 00:00",
         "2003-11-27 00:00",
         "2003-10-30 00:00",
         "2003-09-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ClmLicenseType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portActivation", 1),
          ("portActivation10G", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLicenseMgrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrMIBObjects = _CiscoLicenseMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1)
)
_CiscoLicenseMgrConfig_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrConfig = _CiscoLicenseMgrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 1)
)


class _ClmHostId_Type(SnmpAdminString):
    """Custom type clmHostId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(40, 40),
    )
    fixedLength = 40


_ClmHostId_Type.__name__ = "SnmpAdminString"
_ClmHostId_Object = MibScalar
clmHostId = _ClmHostId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 1, 1),
    _ClmHostId_Type()
)
clmHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmHostId.setStatus("current")


class _ClmNotificationsEnable_Type(TruthValue):
    """Custom type clmNotificationsEnable based on TruthValue"""
    defaultValue = 1


_ClmNotificationsEnable_Type.__name__ = "TruthValue"
_ClmNotificationsEnable_Object = MibScalar
clmNotificationsEnable = _ClmNotificationsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 1, 2),
    _ClmNotificationsEnable_Type()
)
clmNotificationsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmNotificationsEnable.setStatus("current")
_ClmLicenseConfiguration_ObjectIdentity = ObjectIdentity
clmLicenseConfiguration = _ClmLicenseConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2)
)
_ClmLicenseConfigSpinLock_Type = TestAndIncr
_ClmLicenseConfigSpinLock_Object = MibScalar
clmLicenseConfigSpinLock = _ClmLicenseConfigSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 1),
    _ClmLicenseConfigSpinLock_Type()
)
clmLicenseConfigSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseConfigSpinLock.setStatus("current")


class _ClmLicenseFileURI_Type(SnmpAdminString):
    """Custom type clmLicenseFileURI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClmLicenseFileURI_Type.__name__ = "SnmpAdminString"
_ClmLicenseFileURI_Object = MibScalar
clmLicenseFileURI = _ClmLicenseFileURI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 2),
    _ClmLicenseFileURI_Type()
)
clmLicenseFileURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseFileURI.setStatus("current")


class _ClmLicenseFileTargetName_Type(SnmpAdminString):
    """Custom type clmLicenseFileTargetName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ClmLicenseFileTargetName_Type.__name__ = "SnmpAdminString"
_ClmLicenseFileTargetName_Object = MibScalar
clmLicenseFileTargetName = _ClmLicenseFileTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 3),
    _ClmLicenseFileTargetName_Type()
)
clmLicenseFileTargetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseFileTargetName.setStatus("current")


class _ClmLicenseConfigCommand_Type(Integer32):
    """Custom type clmLicenseConfigCommand based on Integer32"""
    defaultValue = 3

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
        *(("install", 1),
          ("uninstall", 2),
          ("noOp", 3),
          ("update", 4))
    )


_ClmLicenseConfigCommand_Type.__name__ = "Integer32"
_ClmLicenseConfigCommand_Object = MibScalar
clmLicenseConfigCommand = _ClmLicenseConfigCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 4),
    _ClmLicenseConfigCommand_Type()
)
clmLicenseConfigCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseConfigCommand.setStatus("current")


class _ClmLicenseConfigCommandStatus_Type(Integer32):
    """Custom type clmLicenseConfigCommandStatus based on Integer32"""
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("inProgress", 2),
          ("corruptedLicenseFile", 3),
          ("targetLicenseFileAlreadyExist", 4),
          ("invalidLicenseFileName", 5),
          ("duplicateLicense", 6),
          ("licenseInUse", 7),
          ("generalLicensingFailure", 8),
          ("none", 9),
          ("licenseExpiryConflict", 10),
          ("invalidLicenseCount", 11),
          ("notThisHost", 12),
          ("licenseInGraceExceeded", 13),
          ("licenseFileNotFound", 14),
          ("licenseFileMissing", 15),
          ("invalidLicenseFileExtension", 16),
          ("invalidURI", 17),
          ("noDemoLicenseSupport", 18),
          ("invalidPlatform", 19),
          ("licenseServerBusy", 20),
          ("invalidLicenseFeature", 21),
          ("noFeatureSupport", 22),
          ("emptyLicenseFile", 23),
          ("invalidServerLine", 24),
          ("invalidVendorLine", 25),
          ("invalidLicFilenameSize", 26),
          ("permanentLicenseExpiryConflict", 27))
    )


_ClmLicenseConfigCommandStatus_Type.__name__ = "Integer32"
_ClmLicenseConfigCommandStatus_Object = MibScalar
clmLicenseConfigCommandStatus = _ClmLicenseConfigCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 5),
    _ClmLicenseConfigCommandStatus_Type()
)
clmLicenseConfigCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseConfigCommandStatus.setStatus("current")
_ClmLicenseRequestSpinLock_Type = TestAndIncr
_ClmLicenseRequestSpinLock_Object = MibScalar
clmLicenseRequestSpinLock = _ClmLicenseRequestSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 6),
    _ClmLicenseRequestSpinLock_Type()
)
clmLicenseRequestSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseRequestSpinLock.setStatus("current")


class _ClmLicenseRequestFeatureName_Type(SnmpAdminString):
    """Custom type clmLicenseRequestFeatureName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ClmLicenseRequestFeatureName_Type.__name__ = "SnmpAdminString"
_ClmLicenseRequestFeatureName_Object = MibScalar
clmLicenseRequestFeatureName = _ClmLicenseRequestFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 7),
    _ClmLicenseRequestFeatureName_Type()
)
clmLicenseRequestFeatureName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseRequestFeatureName.setStatus("current")


class _ClmLicenseRequestAppName_Type(SnmpAdminString):
    """Custom type clmLicenseRequestAppName based on SnmpAdminString"""
    defaultValue = OctetString("")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ClmLicenseRequestAppName_Type.__name__ = "SnmpAdminString"
_ClmLicenseRequestAppName_Object = MibScalar
clmLicenseRequestAppName = _ClmLicenseRequestAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 8),
    _ClmLicenseRequestAppName_Type()
)
clmLicenseRequestAppName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseRequestAppName.setStatus("current")


class _ClmLicenseRequestCommand_Type(Integer32):
    """Custom type clmLicenseRequestCommand based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("checkIn", 1),
          ("checkOut", 2),
          ("noOp", 3))
    )


_ClmLicenseRequestCommand_Type.__name__ = "Integer32"
_ClmLicenseRequestCommand_Object = MibScalar
clmLicenseRequestCommand = _ClmLicenseRequestCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 9),
    _ClmLicenseRequestCommand_Type()
)
clmLicenseRequestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmLicenseRequestCommand.setStatus("current")


class _ClmLicenseRequestCommandStatus_Type(Integer32):
    """Custom type clmLicenseRequestCommandStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("none", 2),
          ("licenseDenied", 3),
          ("licenseTooMany", 4),
          ("generalLicensingFailure", 5),
          ("invalidFeature", 6),
          ("licenseExpired", 7),
          ("licenseServerDown", 8))
    )


_ClmLicenseRequestCommandStatus_Type.__name__ = "Integer32"
_ClmLicenseRequestCommandStatus_Object = MibScalar
clmLicenseRequestCommandStatus = _ClmLicenseRequestCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 2, 10),
    _ClmLicenseRequestCommandStatus_Type()
)
clmLicenseRequestCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseRequestCommandStatus.setStatus("current")
_ClmLicenseInformation_ObjectIdentity = ObjectIdentity
clmLicenseInformation = _ClmLicenseInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3)
)


class _ClmNoOfLicenseFilesInstalled_Type(Integer32):
    """Custom type clmNoOfLicenseFilesInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ClmNoOfLicenseFilesInstalled_Type.__name__ = "Integer32"
_ClmNoOfLicenseFilesInstalled_Object = MibScalar
clmNoOfLicenseFilesInstalled = _ClmNoOfLicenseFilesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 1),
    _ClmNoOfLicenseFilesInstalled_Type()
)
clmNoOfLicenseFilesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmNoOfLicenseFilesInstalled.setStatus("current")
_ClmLicenseFileContentsTable_Object = MibTable
clmLicenseFileContentsTable = _ClmLicenseFileContentsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2)
)
if mibBuilder.loadTexts:
    clmLicenseFileContentsTable.setStatus("current")
_ClmLicenseFileContentsEntry_Object = MibTableRow
clmLicenseFileContentsEntry = _ClmLicenseFileContentsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1)
)
clmLicenseFileContentsEntry.setIndexNames(
    (0, "CISCO-LICENSE-MGR-MIB", "clmLicenseFileName"),
    (0, "CISCO-LICENSE-MGR-MIB", "clmLicenseFileRowNumber"),
)
if mibBuilder.loadTexts:
    clmLicenseFileContentsEntry.setStatus("current")


class _ClmLicenseFileName_Type(SnmpAdminString):
    """Custom type clmLicenseFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ClmLicenseFileName_Type.__name__ = "SnmpAdminString"
_ClmLicenseFileName_Object = MibTableColumn
clmLicenseFileName = _ClmLicenseFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1, 1),
    _ClmLicenseFileName_Type()
)
clmLicenseFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmLicenseFileName.setStatus("current")
_ClmLicenseFileRowNumber_Type = Unsigned32
_ClmLicenseFileRowNumber_Object = MibTableColumn
clmLicenseFileRowNumber = _ClmLicenseFileRowNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1, 2),
    _ClmLicenseFileRowNumber_Type()
)
clmLicenseFileRowNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmLicenseFileRowNumber.setStatus("current")
_ClmLicenseFileTimeStamp_Type = DateAndTime
_ClmLicenseFileTimeStamp_Object = MibTableColumn
clmLicenseFileTimeStamp = _ClmLicenseFileTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1, 3),
    _ClmLicenseFileTimeStamp_Type()
)
clmLicenseFileTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseFileTimeStamp.setStatus("current")
_ClmLicenseFileNoOfRows_Type = Unsigned32
_ClmLicenseFileNoOfRows_Object = MibTableColumn
clmLicenseFileNoOfRows = _ClmLicenseFileNoOfRows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1, 4),
    _ClmLicenseFileNoOfRows_Type()
)
clmLicenseFileNoOfRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseFileNoOfRows.setStatus("current")


class _ClmLicenseFileRowContents_Type(SnmpAdminString):
    """Custom type clmLicenseFileRowContents based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClmLicenseFileRowContents_Type.__name__ = "SnmpAdminString"
_ClmLicenseFileRowContents_Object = MibTableColumn
clmLicenseFileRowContents = _ClmLicenseFileRowContents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 2, 1, 5),
    _ClmLicenseFileRowContents_Type()
)
clmLicenseFileRowContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseFileRowContents.setStatus("current")


class _ClmNoOfLicensedFeatures_Type(Integer32):
    """Custom type clmNoOfLicensedFeatures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_ClmNoOfLicensedFeatures_Type.__name__ = "Integer32"
_ClmNoOfLicensedFeatures_Object = MibScalar
clmNoOfLicensedFeatures = _ClmNoOfLicensedFeatures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 3),
    _ClmNoOfLicensedFeatures_Type()
)
clmNoOfLicensedFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmNoOfLicensedFeatures.setStatus("current")
_ClmLicenseFeatureUsageTable_Object = MibTable
clmLicenseFeatureUsageTable = _ClmLicenseFeatureUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4)
)
if mibBuilder.loadTexts:
    clmLicenseFeatureUsageTable.setStatus("current")
_ClmLicenseFeatureUsageEntry_Object = MibTableRow
clmLicenseFeatureUsageEntry = _ClmLicenseFeatureUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1)
)
clmLicenseFeatureUsageEntry.setIndexNames(
    (0, "CISCO-LICENSE-MGR-MIB", "clmLicenseFeatureName"),
)
if mibBuilder.loadTexts:
    clmLicenseFeatureUsageEntry.setStatus("current")


class _ClmLicenseFeatureName_Type(SnmpAdminString):
    """Custom type clmLicenseFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_ClmLicenseFeatureName_Type.__name__ = "SnmpAdminString"
_ClmLicenseFeatureName_Object = MibTableColumn
clmLicenseFeatureName = _ClmLicenseFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 1),
    _ClmLicenseFeatureName_Type()
)
clmLicenseFeatureName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmLicenseFeatureName.setStatus("current")


class _ClmLicenseFlag_Type(Bits):
    """Custom type clmLicenseFlag based on Bits"""
    namedValues = NamedValues(
        *(("demo", 0),
          ("permanent", 1),
          ("counted", 2),
          ("unlicensed", 3),
          ("inGracePeriod", 4),
          ("inHonorPeriod", 5))
    )

_ClmLicenseFlag_Type.__name__ = "Bits"
_ClmLicenseFlag_Object = MibTableColumn
clmLicenseFlag = _ClmLicenseFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 2),
    _ClmLicenseFlag_Type()
)
clmLicenseFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseFlag.setStatus("current")


class _ClmNoOfLicenseMaxUsages_Type(Integer32):
    """Custom type clmNoOfLicenseMaxUsages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClmNoOfLicenseMaxUsages_Type.__name__ = "Integer32"
_ClmNoOfLicenseMaxUsages_Object = MibTableColumn
clmNoOfLicenseMaxUsages = _ClmNoOfLicenseMaxUsages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 3),
    _ClmNoOfLicenseMaxUsages_Type()
)
clmNoOfLicenseMaxUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmNoOfLicenseMaxUsages.setStatus("current")


class _ClmNoOfMissingUsageLicenses_Type(Integer32):
    """Custom type clmNoOfMissingUsageLicenses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClmNoOfMissingUsageLicenses_Type.__name__ = "Integer32"
_ClmNoOfMissingUsageLicenses_Object = MibTableColumn
clmNoOfMissingUsageLicenses = _ClmNoOfMissingUsageLicenses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 4),
    _ClmNoOfMissingUsageLicenses_Type()
)
clmNoOfMissingUsageLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmNoOfMissingUsageLicenses.setStatus("current")


class _ClmNoOfLicenseCurrentUsages_Type(Integer32):
    """Custom type clmNoOfLicenseCurrentUsages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ClmNoOfLicenseCurrentUsages_Type.__name__ = "Integer32"
_ClmNoOfLicenseCurrentUsages_Object = MibTableColumn
clmNoOfLicenseCurrentUsages = _ClmNoOfLicenseCurrentUsages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 5),
    _ClmNoOfLicenseCurrentUsages_Type()
)
clmNoOfLicenseCurrentUsages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmNoOfLicenseCurrentUsages.setStatus("current")
_ClmLicenseExpiryDate_Type = DateAndTime
_ClmLicenseExpiryDate_Object = MibTableColumn
clmLicenseExpiryDate = _ClmLicenseExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 6),
    _ClmLicenseExpiryDate_Type()
)
clmLicenseExpiryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseExpiryDate.setStatus("current")


class _ClmLicenseGracePeriod_Type(Integer32):
    """Custom type clmLicenseGracePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5184000),
    )


_ClmLicenseGracePeriod_Type.__name__ = "Integer32"
_ClmLicenseGracePeriod_Object = MibTableColumn
clmLicenseGracePeriod = _ClmLicenseGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 7),
    _ClmLicenseGracePeriod_Type()
)
clmLicenseGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseGracePeriod.setStatus("deprecated")
if mibBuilder.loadTexts:
    clmLicenseGracePeriod.setUnits("seconds")
_ClmLicenseEnabled_Type = TruthValue
_ClmLicenseEnabled_Object = MibTableColumn
clmLicenseEnabled = _ClmLicenseEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 8),
    _ClmLicenseEnabled_Type()
)
clmLicenseEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseEnabled.setStatus("current")


class _ClmLicenseGracePeriodLeft_Type(Unsigned32):
    """Custom type clmLicenseGracePeriodLeft based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ClmLicenseGracePeriodLeft_Type.__name__ = "Unsigned32"
_ClmLicenseGracePeriodLeft_Object = MibTableColumn
clmLicenseGracePeriodLeft = _ClmLicenseGracePeriodLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 9),
    _ClmLicenseGracePeriodLeft_Type()
)
clmLicenseGracePeriodLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseGracePeriodLeft.setStatus("current")
if mibBuilder.loadTexts:
    clmLicenseGracePeriodLeft.setUnits("seconds")


class _ClmLicenseDefaultLicenses_Type(Unsigned32):
    """Custom type clmLicenseDefaultLicenses based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ClmLicenseDefaultLicenses_Type.__name__ = "Unsigned32"
_ClmLicenseDefaultLicenses_Object = MibTableColumn
clmLicenseDefaultLicenses = _ClmLicenseDefaultLicenses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 4, 1, 10),
    _ClmLicenseDefaultLicenses_Type()
)
clmLicenseDefaultLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseDefaultLicenses.setStatus("current")
_ClmFeatureUsageDetailsTable_Object = MibTable
clmFeatureUsageDetailsTable = _ClmFeatureUsageDetailsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 5)
)
if mibBuilder.loadTexts:
    clmFeatureUsageDetailsTable.setStatus("current")
_ClmFeatureUsageDetailsEntry_Object = MibTableRow
clmFeatureUsageDetailsEntry = _ClmFeatureUsageDetailsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 5, 1)
)
clmFeatureUsageDetailsEntry.setIndexNames(
    (0, "CISCO-LICENSE-MGR-MIB", "clmLicenseFeatureName"),
    (0, "CISCO-LICENSE-MGR-MIB", "clmLicensedAppIndex"),
)
if mibBuilder.loadTexts:
    clmFeatureUsageDetailsEntry.setStatus("current")
_ClmLicensedAppIndex_Type = Unsigned32
_ClmLicensedAppIndex_Object = MibTableColumn
clmLicensedAppIndex = _ClmLicensedAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 5, 1, 1),
    _ClmLicensedAppIndex_Type()
)
clmLicensedAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmLicensedAppIndex.setStatus("current")


class _ClmLicensedAppName_Type(SnmpAdminString):
    """Custom type clmLicensedAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_ClmLicensedAppName_Type.__name__ = "SnmpAdminString"
_ClmLicensedAppName_Object = MibTableColumn
clmLicensedAppName = _ClmLicensedAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 5, 1, 2),
    _ClmLicensedAppName_Type()
)
clmLicensedAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicensedAppName.setStatus("current")
_ClmLicenseViolationWarnFlag_Type = TruthValue
_ClmLicenseViolationWarnFlag_Object = MibScalar
clmLicenseViolationWarnFlag = _ClmLicenseViolationWarnFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 6),
    _ClmLicenseViolationWarnFlag_Type()
)
clmLicenseViolationWarnFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmLicenseViolationWarnFlag.setStatus("current")
_ClmPortLicensingTable_Object = MibTable
clmPortLicensingTable = _ClmPortLicensingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 7)
)
if mibBuilder.loadTexts:
    clmPortLicensingTable.setStatus("current")
_ClmPortLicensingEntry_Object = MibTableRow
clmPortLicensingEntry = _ClmPortLicensingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 7, 1)
)
clmPortLicensingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-LICENSE-MGR-MIB", "clmPortLicensingType"),
)
if mibBuilder.loadTexts:
    clmPortLicensingEntry.setStatus("current")
_ClmPortLicensingType_Type = ClmLicenseType
_ClmPortLicensingType_Object = MibTableColumn
clmPortLicensingType = _ClmPortLicensingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 7, 1, 1),
    _ClmPortLicensingType_Type()
)
clmPortLicensingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clmPortLicensingType.setStatus("current")


class _ClmPortLicensingConfig_Type(Integer32):
    """Custom type clmPortLicensingConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eligible", 1),
          ("inEligible", 2),
          ("acquire", 3))
    )


_ClmPortLicensingConfig_Type.__name__ = "Integer32"
_ClmPortLicensingConfig_Object = MibTableColumn
clmPortLicensingConfig = _ClmPortLicensingConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 7, 1, 2),
    _ClmPortLicensingConfig_Type()
)
clmPortLicensingConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clmPortLicensingConfig.setStatus("current")


class _ClmPortLicensingOper_Type(Integer32):
    """Custom type clmPortLicensingOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAcquired", 1),
          ("acquired", 2))
    )


_ClmPortLicensingOper_Type.__name__ = "Integer32"
_ClmPortLicensingOper_Object = MibTableColumn
clmPortLicensingOper = _ClmPortLicensingOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 7, 1, 3),
    _ClmPortLicensingOper_Type()
)
clmPortLicensingOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmPortLicensingOper.setStatus("current")
_ClmPortLicCountTable_Object = MibTable
clmPortLicCountTable = _ClmPortLicCountTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 8)
)
if mibBuilder.loadTexts:
    clmPortLicCountTable.setStatus("current")
_ClmPortLicCountEntry_Object = MibTableRow
clmPortLicCountEntry = _ClmPortLicCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 8, 1)
)
clmPortLicCountEntry.setIndexNames(
    (0, "CISCO-LICENSE-MGR-MIB", "clmPortLicensingType"),
)
if mibBuilder.loadTexts:
    clmPortLicCountEntry.setStatus("current")
_ClmPortLicCountMax_Type = Unsigned32
_ClmPortLicCountMax_Object = MibTableColumn
clmPortLicCountMax = _ClmPortLicCountMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 8, 1, 1),
    _ClmPortLicCountMax_Type()
)
clmPortLicCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmPortLicCountMax.setStatus("current")
_ClmPortLicCountUsed_Type = Gauge32
_ClmPortLicCountUsed_Object = MibTableColumn
clmPortLicCountUsed = _ClmPortLicCountUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 8, 1, 2),
    _ClmPortLicCountUsed_Type()
)
clmPortLicCountUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmPortLicCountUsed.setStatus("current")
if mibBuilder.loadTexts:
    clmPortLicCountUsed.setUnits("licenses")
_ClmPortLicCountMaxInternal_Type = Unsigned32
_ClmPortLicCountMaxInternal_Object = MibTableColumn
clmPortLicCountMaxInternal = _ClmPortLicCountMaxInternal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 8, 1, 3),
    _ClmPortLicCountMaxInternal_Type()
)
clmPortLicCountMaxInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmPortLicCountMaxInternal.setStatus("current")
_ClmPortLicCountUsedInternal_Type = Gauge32
_ClmPortLicCountUsedInternal_Object = MibTableColumn
clmPortLicCountUsedInternal = _ClmPortLicCountUsedInternal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 8, 1, 4),
    _ClmPortLicCountUsedInternal_Type()
)
clmPortLicCountUsedInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmPortLicCountUsedInternal.setStatus("current")
if mibBuilder.loadTexts:
    clmPortLicCountUsedInternal.setUnits("licenses")
_ClmLicenseFeatureStatus_ObjectIdentity = ObjectIdentity
clmLicenseFeatureStatus = _ClmLicenseFeatureStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 9)
)
_ClmMaxSslTransactions_Type = Integer32
_ClmMaxSslTransactions_Object = MibScalar
clmMaxSslTransactions = _ClmMaxSslTransactions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 9, 1),
    _ClmMaxSslTransactions_Type()
)
clmMaxSslTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmMaxSslTransactions.setStatus("current")
_ClmMaxVirtualizedContext_Type = Integer32
_ClmMaxVirtualizedContext_Object = MibScalar
clmMaxVirtualizedContext = _ClmMaxVirtualizedContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 9, 2),
    _ClmMaxVirtualizedContext_Type()
)
clmMaxVirtualizedContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmMaxVirtualizedContext.setStatus("current")
_ClmModuleBandwidth_Type = Integer32
_ClmModuleBandwidth_Object = MibScalar
clmModuleBandwidth = _ClmModuleBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 9, 3),
    _ClmModuleBandwidth_Type()
)
clmModuleBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmModuleBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    clmModuleBandwidth.setUnits("Gbps")
_ClmCompressionPerformance_Type = Integer32
_ClmCompressionPerformance_Object = MibScalar
clmCompressionPerformance = _ClmCompressionPerformance_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 9, 4),
    _ClmCompressionPerformance_Type()
)
clmCompressionPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmCompressionPerformance.setStatus("current")
if mibBuilder.loadTexts:
    clmCompressionPerformance.setUnits("Mbps")
_ClmWebOptimization_Type = Integer32
_ClmWebOptimization_Object = MibScalar
clmWebOptimization = _ClmWebOptimization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 1, 3, 9, 5),
    _ClmWebOptimization_Type()
)
clmWebOptimization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clmWebOptimization.setStatus("current")
if mibBuilder.loadTexts:
    clmWebOptimization.setUnits("Cps")
_CiscoLicenseMgrMIBConform_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrMIBConform = _CiscoLicenseMgrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2)
)
_CiscoLicenseMgrCompliances_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrCompliances = _CiscoLicenseMgrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 1)
)
_CiscoLicenseMgrGroups_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrGroups = _CiscoLicenseMgrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2)
)
_CiscoLicenseMgrMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrMIBNotifs = _CiscoLicenseMgrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3)
)
_CiscoLicenseMgrNotifications_ObjectIdentity = ObjectIdentity
ciscoLicenseMgrNotifications = _CiscoLicenseMgrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3, 0)
)

# Managed Objects groups

clmLicenseInstallGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 1)
)
clmLicenseInstallGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmHostId"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseConfigSpinLock"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileURI"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileTargetName"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseConfigCommand"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseConfigCommandStatus"))
)
if mibBuilder.loadTexts:
    clmLicenseInstallGroup.setStatus("current")

clmNoOfInstalledLicensesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 2)
)
clmNoOfInstalledLicensesGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseFilesInstalled"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicensedFeatures"))
)
if mibBuilder.loadTexts:
    clmNoOfInstalledLicensesGroup.setStatus("current")

clmLicenseInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 3)
)
clmLicenseInformationGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseFileTimeStamp"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileNoOfRows"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileRowContents"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFlag"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseMaxUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfMissingUsageLicenses"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseCurrentUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryDate"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseGracePeriod"))
)
if mibBuilder.loadTexts:
    clmLicenseInformationGroup.setStatus("deprecated")

clmNotificationsEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 4)
)
clmNotificationsEnableGroup.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmNotificationsEnable")
)
if mibBuilder.loadTexts:
    clmNotificationsEnableGroup.setStatus("current")

clmLicenseRequestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 6)
)
clmLicenseRequestGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestSpinLock"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestFeatureName"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestAppName"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestCommand"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestCommandStatus"))
)
if mibBuilder.loadTexts:
    clmLicenseRequestGroup.setStatus("current")

clmLicenseInformationGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 7)
)
clmLicenseInformationGroup1.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseFileTimeStamp"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileNoOfRows"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileRowContents"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFlag"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseMaxUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfMissingUsageLicenses"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseCurrentUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryDate"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseGracePeriod"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicensedAppName"))
)
if mibBuilder.loadTexts:
    clmLicenseInformationGroup1.setStatus("deprecated")

clmLicenseInformationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 8)
)
clmLicenseInformationGroup2.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseFileTimeStamp"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileNoOfRows"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileRowContents"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFlag"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseMaxUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfMissingUsageLicenses"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseCurrentUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryDate"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseGracePeriod"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicensedAppName"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseViolationWarnFlag"))
)
if mibBuilder.loadTexts:
    clmLicenseInformationGroup2.setStatus("deprecated")

clmLicenseInformationGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 9)
)
clmLicenseInformationGroupSup1.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmLicenseEnabled")
)
if mibBuilder.loadTexts:
    clmLicenseInformationGroupSup1.setStatus("current")

clmLicenseInformationGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 10)
)
clmLicenseInformationGroup3.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseFileTimeStamp"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileNoOfRows"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileRowContents"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFlag"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseMaxUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfMissingUsageLicenses"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfLicenseCurrentUsages"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryDate"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseGracePeriodLeft"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicensedAppName"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseViolationWarnFlag"))
)
if mibBuilder.loadTexts:
    clmLicenseInformationGroup3.setStatus("current")

clmLicenseInformationGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 11)
)
clmLicenseInformationGroupSup2.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmLicenseDefaultLicenses")
)
if mibBuilder.loadTexts:
    clmLicenseInformationGroupSup2.setStatus("current")

clmLicenseInformationPortLicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 12)
)
clmLicenseInformationPortLicGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmPortLicensingConfig"),
        ("CISCO-LICENSE-MGR-MIB", "clmPortLicensingOper"),
        ("CISCO-LICENSE-MGR-MIB", "clmPortLicCountMax"),
        ("CISCO-LICENSE-MGR-MIB", "clmPortLicCountUsed"),
        ("CISCO-LICENSE-MGR-MIB", "clmPortLicCountMaxInternal"),
        ("CISCO-LICENSE-MGR-MIB", "clmPortLicCountUsedInternal"))
)
if mibBuilder.loadTexts:
    clmLicenseInformationPortLicGroup.setStatus("current")

clmLicenseFeatureStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 13)
)
clmLicenseFeatureStatusGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmMaxSslTransactions"),
        ("CISCO-LICENSE-MGR-MIB", "clmMaxVirtualizedContext"),
        ("CISCO-LICENSE-MGR-MIB", "clmModuleBandwidth"),
        ("CISCO-LICENSE-MGR-MIB", "clmCompressionPerformance"),
        ("CISCO-LICENSE-MGR-MIB", "clmWebOptimization"))
)
if mibBuilder.loadTexts:
    clmLicenseFeatureStatusGroup.setStatus("current")


# Notification objects

clmLicenseExpiryNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3, 0, 1)
)
clmLicenseExpiryNotify.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryDate")
)
if mibBuilder.loadTexts:
    clmLicenseExpiryNotify.setStatus(
        "current"
    )

clmNoLicenseForFeatureNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3, 0, 2)
)
clmNoLicenseForFeatureNotify.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmLicenseGracePeriodLeft")
)
if mibBuilder.loadTexts:
    clmNoLicenseForFeatureNotify.setStatus(
        "current"
    )

clmLicenseFileMissingNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3, 0, 3)
)
clmLicenseFileMissingNotify.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmNoOfMissingUsageLicenses")
)
if mibBuilder.loadTexts:
    clmLicenseFileMissingNotify.setStatus(
        "current"
    )

clmLicenseExpiryWarningNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 3, 0, 4)
)
clmLicenseExpiryWarningNotify.setObjects(
    ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryDate")
)
if mibBuilder.loadTexts:
    clmLicenseExpiryWarningNotify.setStatus(
        "current"
    )


# Notifications groups

clmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 2, 5)
)
clmNotificationGroup.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryNotify"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoLicenseForFeatureNotify"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFileMissingNotify"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseExpiryWarningNotify"))
)
if mibBuilder.loadTexts:
    clmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLicenseMgrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 1, 1)
)
ciscoLicenseMgrCompliance.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseInstallGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfInstalledLicensesGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationsEnableGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoLicenseMgrCompliance.setStatus(
        "deprecated"
    )

ciscoLicenseMgrCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 1, 2)
)
ciscoLicenseMgrCompliance1.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseInstallGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfInstalledLicensesGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationGroup1"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationsEnableGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoLicenseMgrCompliance1.setStatus(
        "deprecated"
    )

ciscoLicenseMgrCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 1, 3)
)
ciscoLicenseMgrCompliance2.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseInstallGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfInstalledLicensesGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationGroup2"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationsEnableGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationGroup"))
)
if mibBuilder.loadTexts:
    ciscoLicenseMgrCompliance2.setStatus(
        "deprecated"
    )

ciscoLicenseMgrCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 1, 4)
)
ciscoLicenseMgrCompliance3.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseInstallGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfInstalledLicensesGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationGroup3"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationsEnableGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationGroupSup1"))
)
if mibBuilder.loadTexts:
    ciscoLicenseMgrCompliance3.setStatus(
        "deprecated"
    )

ciscoLicenseMgrCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 1, 5)
)
ciscoLicenseMgrCompliance4.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseInstallGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfInstalledLicensesGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationGroup3"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationsEnableGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationGroupSup2"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationPortLicGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationGroupSup1"))
)
if mibBuilder.loadTexts:
    ciscoLicenseMgrCompliance4.setStatus(
        "deprecated"
    )

ciscoLicenseMgrCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 369, 2, 1, 6)
)
ciscoLicenseMgrCompliance5.setObjects(
      *(("CISCO-LICENSE-MGR-MIB", "clmLicenseInstallGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseRequestGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNoOfInstalledLicensesGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationGroup3"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationsEnableGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmNotificationGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationGroupSup2"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationPortLicGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseFeatureStatusGroup"),
        ("CISCO-LICENSE-MGR-MIB", "clmLicenseInformationGroupSup1"))
)
if mibBuilder.loadTexts:
    ciscoLicenseMgrCompliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LICENSE-MGR-MIB",
    **{"ClmLicenseType": ClmLicenseType,
       "ciscoLicenseMgrMIB": ciscoLicenseMgrMIB,
       "ciscoLicenseMgrMIBObjects": ciscoLicenseMgrMIBObjects,
       "ciscoLicenseMgrConfig": ciscoLicenseMgrConfig,
       "clmHostId": clmHostId,
       "clmNotificationsEnable": clmNotificationsEnable,
       "clmLicenseConfiguration": clmLicenseConfiguration,
       "clmLicenseConfigSpinLock": clmLicenseConfigSpinLock,
       "clmLicenseFileURI": clmLicenseFileURI,
       "clmLicenseFileTargetName": clmLicenseFileTargetName,
       "clmLicenseConfigCommand": clmLicenseConfigCommand,
       "clmLicenseConfigCommandStatus": clmLicenseConfigCommandStatus,
       "clmLicenseRequestSpinLock": clmLicenseRequestSpinLock,
       "clmLicenseRequestFeatureName": clmLicenseRequestFeatureName,
       "clmLicenseRequestAppName": clmLicenseRequestAppName,
       "clmLicenseRequestCommand": clmLicenseRequestCommand,
       "clmLicenseRequestCommandStatus": clmLicenseRequestCommandStatus,
       "clmLicenseInformation": clmLicenseInformation,
       "clmNoOfLicenseFilesInstalled": clmNoOfLicenseFilesInstalled,
       "clmLicenseFileContentsTable": clmLicenseFileContentsTable,
       "clmLicenseFileContentsEntry": clmLicenseFileContentsEntry,
       "clmLicenseFileName": clmLicenseFileName,
       "clmLicenseFileRowNumber": clmLicenseFileRowNumber,
       "clmLicenseFileTimeStamp": clmLicenseFileTimeStamp,
       "clmLicenseFileNoOfRows": clmLicenseFileNoOfRows,
       "clmLicenseFileRowContents": clmLicenseFileRowContents,
       "clmNoOfLicensedFeatures": clmNoOfLicensedFeatures,
       "clmLicenseFeatureUsageTable": clmLicenseFeatureUsageTable,
       "clmLicenseFeatureUsageEntry": clmLicenseFeatureUsageEntry,
       "clmLicenseFeatureName": clmLicenseFeatureName,
       "clmLicenseFlag": clmLicenseFlag,
       "clmNoOfLicenseMaxUsages": clmNoOfLicenseMaxUsages,
       "clmNoOfMissingUsageLicenses": clmNoOfMissingUsageLicenses,
       "clmNoOfLicenseCurrentUsages": clmNoOfLicenseCurrentUsages,
       "clmLicenseExpiryDate": clmLicenseExpiryDate,
       "clmLicenseGracePeriod": clmLicenseGracePeriod,
       "clmLicenseEnabled": clmLicenseEnabled,
       "clmLicenseGracePeriodLeft": clmLicenseGracePeriodLeft,
       "clmLicenseDefaultLicenses": clmLicenseDefaultLicenses,
       "clmFeatureUsageDetailsTable": clmFeatureUsageDetailsTable,
       "clmFeatureUsageDetailsEntry": clmFeatureUsageDetailsEntry,
       "clmLicensedAppIndex": clmLicensedAppIndex,
       "clmLicensedAppName": clmLicensedAppName,
       "clmLicenseViolationWarnFlag": clmLicenseViolationWarnFlag,
       "clmPortLicensingTable": clmPortLicensingTable,
       "clmPortLicensingEntry": clmPortLicensingEntry,
       "clmPortLicensingType": clmPortLicensingType,
       "clmPortLicensingConfig": clmPortLicensingConfig,
       "clmPortLicensingOper": clmPortLicensingOper,
       "clmPortLicCountTable": clmPortLicCountTable,
       "clmPortLicCountEntry": clmPortLicCountEntry,
       "clmPortLicCountMax": clmPortLicCountMax,
       "clmPortLicCountUsed": clmPortLicCountUsed,
       "clmPortLicCountMaxInternal": clmPortLicCountMaxInternal,
       "clmPortLicCountUsedInternal": clmPortLicCountUsedInternal,
       "clmLicenseFeatureStatus": clmLicenseFeatureStatus,
       "clmMaxSslTransactions": clmMaxSslTransactions,
       "clmMaxVirtualizedContext": clmMaxVirtualizedContext,
       "clmModuleBandwidth": clmModuleBandwidth,
       "clmCompressionPerformance": clmCompressionPerformance,
       "clmWebOptimization": clmWebOptimization,
       "ciscoLicenseMgrMIBConform": ciscoLicenseMgrMIBConform,
       "ciscoLicenseMgrCompliances": ciscoLicenseMgrCompliances,
       "ciscoLicenseMgrCompliance": ciscoLicenseMgrCompliance,
       "ciscoLicenseMgrCompliance1": ciscoLicenseMgrCompliance1,
       "ciscoLicenseMgrCompliance2": ciscoLicenseMgrCompliance2,
       "ciscoLicenseMgrCompliance3": ciscoLicenseMgrCompliance3,
       "ciscoLicenseMgrCompliance4": ciscoLicenseMgrCompliance4,
       "ciscoLicenseMgrCompliance5": ciscoLicenseMgrCompliance5,
       "ciscoLicenseMgrGroups": ciscoLicenseMgrGroups,
       "clmLicenseInstallGroup": clmLicenseInstallGroup,
       "clmNoOfInstalledLicensesGroup": clmNoOfInstalledLicensesGroup,
       "clmLicenseInformationGroup": clmLicenseInformationGroup,
       "clmNotificationsEnableGroup": clmNotificationsEnableGroup,
       "clmNotificationGroup": clmNotificationGroup,
       "clmLicenseRequestGroup": clmLicenseRequestGroup,
       "clmLicenseInformationGroup1": clmLicenseInformationGroup1,
       "clmLicenseInformationGroup2": clmLicenseInformationGroup2,
       "clmLicenseInformationGroupSup1": clmLicenseInformationGroupSup1,
       "clmLicenseInformationGroup3": clmLicenseInformationGroup3,
       "clmLicenseInformationGroupSup2": clmLicenseInformationGroupSup2,
       "clmLicenseInformationPortLicGroup": clmLicenseInformationPortLicGroup,
       "clmLicenseFeatureStatusGroup": clmLicenseFeatureStatusGroup,
       "ciscoLicenseMgrMIBNotifs": ciscoLicenseMgrMIBNotifs,
       "ciscoLicenseMgrNotifications": ciscoLicenseMgrNotifications,
       "clmLicenseExpiryNotify": clmLicenseExpiryNotify,
       "clmNoLicenseForFeatureNotify": clmNoLicenseForFeatureNotify,
       "clmLicenseFileMissingNotify": clmLicenseFileMissingNotify,
       "clmLicenseExpiryWarningNotify": clmLicenseExpiryWarningNotify}
)
