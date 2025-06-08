# SNMP MIB module (MF-List-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/broadforward_39216/MF-List-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:58:58 2025
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

(AdminStatus,
 mfModules,
 moduleName,
 severity) = mibBuilder.importSymbols(
    "MF-MIB",
    "AdminStatus",
    "mfModules",
    "moduleName",
    "severity")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mfList = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7)
)
if mibBuilder.loadTexts:
    mfList.setRevisions(
        ("2016-08-12 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ListOperationalStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("inactive", 0),
          ("active", 1),
          ("loading", 2),
          ("stopping", 3),
          ("loadingFailed", 4),
          ("reloadingFailed", 5))
    )



# MIB Managed Objects in the order of their OIDs

_ListFilesTable_Object = MibTable
listFilesTable = _ListFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2)
)
if mibBuilder.loadTexts:
    listFilesTable.setStatus("current")
_ListFilesEntry_Object = MibTableRow
listFilesEntry = _ListFilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1)
)
listFilesEntry.setIndexNames(
    (0, "MF-List-MIB", "listFileIndex"),
)
if mibBuilder.loadTexts:
    listFilesEntry.setStatus("current")


class _ListProfIndex_Type(Integer32):
    """Custom type listProfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_ListProfIndex_Type.__name__ = "Integer32"
_ListProfIndex_Object = MibTableColumn
listProfIndex = _ListProfIndex_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 1),
    _ListProfIndex_Type()
)
listProfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    listProfIndex.setStatus("current")


class _ListFileIndex_Type(Integer32):
    """Custom type listFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000),
    )


_ListFileIndex_Type.__name__ = "Integer32"
_ListFileIndex_Object = MibTableColumn
listFileIndex = _ListFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 2),
    _ListFileIndex_Type()
)
listFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    listFileIndex.setStatus("current")
_ListFileName_Type = DisplayString
_ListFileName_Object = MibTableColumn
listFileName = _ListFileName_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 3),
    _ListFileName_Type()
)
listFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listFileName.setStatus("current")


class _ListFileReload_Type(Integer32):
    """Custom type listFileReload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ListFileReload_Type.__name__ = "Integer32"
_ListFileReload_Object = MibTableColumn
listFileReload = _ListFileReload_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 4),
    _ListFileReload_Type()
)
listFileReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listFileReload.setStatus("current")
_ListFileStatus_Type = DisplayString
_ListFileStatus_Object = MibTableColumn
listFileStatus = _ListFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 5),
    _ListFileStatus_Type()
)
listFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listFileStatus.setStatus("current")
_ListFileNumberOfRecords_Type = Gauge32
_ListFileNumberOfRecords_Object = MibTableColumn
listFileNumberOfRecords = _ListFileNumberOfRecords_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 6),
    _ListFileNumberOfRecords_Type()
)
listFileNumberOfRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listFileNumberOfRecords.setStatus("current")
_ListFileDuplicateRecords_Type = Gauge32
_ListFileDuplicateRecords_Object = MibTableColumn
listFileDuplicateRecords = _ListFileDuplicateRecords_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 7),
    _ListFileDuplicateRecords_Type()
)
listFileDuplicateRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listFileDuplicateRecords.setStatus("current")
_ListFileLastLoadedOn_Type = Unsigned32
_ListFileLastLoadedOn_Object = MibTableColumn
listFileLastLoadedOn = _ListFileLastLoadedOn_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 8),
    _ListFileLastLoadedOn_Type()
)
listFileLastLoadedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listFileLastLoadedOn.setStatus("current")
_ListFileTotalReloads_Type = Counter64
_ListFileTotalReloads_Object = MibTableColumn
listFileTotalReloads = _ListFileTotalReloads_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 101),
    _ListFileTotalReloads_Type()
)
listFileTotalReloads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listFileTotalReloads.setStatus("current")
_ListFileSuccessfulReload_Type = Counter64
_ListFileSuccessfulReload_Object = MibTableColumn
listFileSuccessfulReload = _ListFileSuccessfulReload_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 102),
    _ListFileSuccessfulReload_Type()
)
listFileSuccessfulReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listFileSuccessfulReload.setStatus("current")
_ListFileFailedReload_Type = Counter64
_ListFileFailedReload_Object = MibTableColumn
listFileFailedReload = _ListFileFailedReload_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 103),
    _ListFileFailedReload_Type()
)
listFileFailedReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listFileFailedReload.setStatus("current")
_ListFileTotalQueries_Type = Counter64
_ListFileTotalQueries_Object = MibTableColumn
listFileTotalQueries = _ListFileTotalQueries_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 2, 1, 104),
    _ListFileTotalQueries_Type()
)
listFileTotalQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listFileTotalQueries.setStatus("current")
_ListProfilesTable_Object = MibTable
listProfilesTable = _ListProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3)
)
if mibBuilder.loadTexts:
    listProfilesTable.setStatus("current")
_ListProfilesEntry_Object = MibTableRow
listProfilesEntry = _ListProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1)
)
listProfilesEntry.setIndexNames(
    (0, "MF-List-MIB", "listProfileIndex"),
)
if mibBuilder.loadTexts:
    listProfilesEntry.setStatus("current")


class _ListProfileIndex_Type(Integer32):
    """Custom type listProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ListProfileIndex_Type.__name__ = "Integer32"
_ListProfileIndex_Object = MibTableColumn
listProfileIndex = _ListProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 1),
    _ListProfileIndex_Type()
)
listProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    listProfileIndex.setStatus("current")
_ListProfileAdminStatus_Type = AdminStatus
_ListProfileAdminStatus_Object = MibTableColumn
listProfileAdminStatus = _ListProfileAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 2),
    _ListProfileAdminStatus_Type()
)
listProfileAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listProfileAdminStatus.setStatus("current")
_ListProfileName_Type = DisplayString
_ListProfileName_Object = MibTableColumn
listProfileName = _ListProfileName_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 3),
    _ListProfileName_Type()
)
listProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listProfileName.setStatus("current")
_ListProfileDescription_Type = DisplayString
_ListProfileDescription_Object = MibTableColumn
listProfileDescription = _ListProfileDescription_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 4),
    _ListProfileDescription_Type()
)
listProfileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listProfileDescription.setStatus("current")
_ListProfileLastActivatedOn_Type = Unsigned32
_ListProfileLastActivatedOn_Object = MibTableColumn
listProfileLastActivatedOn = _ListProfileLastActivatedOn_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 5),
    _ListProfileLastActivatedOn_Type()
)
listProfileLastActivatedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listProfileLastActivatedOn.setStatus("current")
_ListProfileOperationalStatus_Type = ListOperationalStatus
_ListProfileOperationalStatus_Object = MibTableColumn
listProfileOperationalStatus = _ListProfileOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 6),
    _ListProfileOperationalStatus_Type()
)
listProfileOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listProfileOperationalStatus.setStatus("current")
_ListProfileNumberOfRecords_Type = Gauge32
_ListProfileNumberOfRecords_Object = MibTableColumn
listProfileNumberOfRecords = _ListProfileNumberOfRecords_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 7),
    _ListProfileNumberOfRecords_Type()
)
listProfileNumberOfRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listProfileNumberOfRecords.setStatus("current")
_ListProfileNumberOfUsers_Type = Gauge32
_ListProfileNumberOfUsers_Object = MibTableColumn
listProfileNumberOfUsers = _ListProfileNumberOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 8),
    _ListProfileNumberOfUsers_Type()
)
listProfileNumberOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    listProfileNumberOfUsers.setStatus("current")
_ListProfileTotalReloads_Type = Counter64
_ListProfileTotalReloads_Object = MibTableColumn
listProfileTotalReloads = _ListProfileTotalReloads_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 101),
    _ListProfileTotalReloads_Type()
)
listProfileTotalReloads.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listProfileTotalReloads.setStatus("current")
_ListProfileSuccessfulReload_Type = Counter64
_ListProfileSuccessfulReload_Object = MibTableColumn
listProfileSuccessfulReload = _ListProfileSuccessfulReload_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 102),
    _ListProfileSuccessfulReload_Type()
)
listProfileSuccessfulReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listProfileSuccessfulReload.setStatus("current")
_ListProfileFailedReload_Type = Counter64
_ListProfileFailedReload_Object = MibTableColumn
listProfileFailedReload = _ListProfileFailedReload_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 103),
    _ListProfileFailedReload_Type()
)
listProfileFailedReload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listProfileFailedReload.setStatus("current")
_ListProfileTotalQueries_Type = Counter64
_ListProfileTotalQueries_Object = MibTableColumn
listProfileTotalQueries = _ListProfileTotalQueries_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 104),
    _ListProfileTotalQueries_Type()
)
listProfileTotalQueries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listProfileTotalQueries.setStatus("current")
_ListProfileQueryResultFound_Type = Counter64
_ListProfileQueryResultFound_Object = MibTableColumn
listProfileQueryResultFound = _ListProfileQueryResultFound_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 105),
    _ListProfileQueryResultFound_Type()
)
listProfileQueryResultFound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listProfileQueryResultFound.setStatus("current")
_ListProfileQueryResultFailed_Type = Counter64
_ListProfileQueryResultFailed_Object = MibTableColumn
listProfileQueryResultFailed = _ListProfileQueryResultFailed_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 106),
    _ListProfileQueryResultFailed_Type()
)
listProfileQueryResultFailed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listProfileQueryResultFailed.setStatus("current")
_ListProfileQueryResultNotFound_Type = Counter64
_ListProfileQueryResultNotFound_Object = MibTableColumn
listProfileQueryResultNotFound = _ListProfileQueryResultNotFound_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 3, 1, 107),
    _ListProfileQueryResultNotFound_Type()
)
listProfileQueryResultNotFound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listProfileQueryResultNotFound.setStatus("current")
_ActivateProfile_Type = DisplayString
_ActivateProfile_Object = MibScalar
activateProfile = _ActivateProfile_Object(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 4),
    _ActivateProfile_Type()
)
activateProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activateProfile.setStatus("current")
_MfListNotifications_ObjectIdentity = ObjectIdentity
mfListNotifications = _MfListNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 11, 0)
)

# Managed Objects groups

mfListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 1)
)
mfListGroup.setObjects(
      *(("MF-List-MIB", "listProfileName"),
        ("MF-List-MIB", "listProfileAdminStatus"),
        ("MF-List-MIB", "listProfileOperationalStatus"),
        ("MF-List-MIB", "listProfileDescription"),
        ("MF-List-MIB", "listProfileLastActivatedOn"),
        ("MF-List-MIB", "listProfileNumberOfRecords"),
        ("MF-List-MIB", "listProfileNumberOfUsers"),
        ("MF-List-MIB", "listProfileTotalReloads"),
        ("MF-List-MIB", "listProfileSuccessfulReload"),
        ("MF-List-MIB", "listProfileFailedReload"),
        ("MF-List-MIB", "listProfileTotalQueries"),
        ("MF-List-MIB", "listProfileQueryResultFound"),
        ("MF-List-MIB", "listProfileQueryResultFailed"),
        ("MF-List-MIB", "listProfileQueryResultNotFound"),
        ("MF-List-MIB", "listFileName"),
        ("MF-List-MIB", "listFileReload"),
        ("MF-List-MIB", "listFileStatus"),
        ("MF-List-MIB", "listFileNumberOfRecords"),
        ("MF-List-MIB", "listFileDuplicateRecords"),
        ("MF-List-MIB", "listFileLastLoadedOn"),
        ("MF-List-MIB", "listFileTotalReloads"),
        ("MF-List-MIB", "listFileSuccessfulReload"),
        ("MF-List-MIB", "listFileFailedReload"),
        ("MF-List-MIB", "listFileTotalQueries"),
        ("MF-List-MIB", "activateProfile"))
)
if mibBuilder.loadTexts:
    mfListGroup.setStatus("current")


# Notification objects

profileReloadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 11, 0, 1)
)
profileReloadSuccess.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"),
        ("MF-List-MIB", "listProfileName"))
)
if mibBuilder.loadTexts:
    profileReloadSuccess.setStatus(
        "current"
    )

profileReloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 11, 0, 2)
)
profileReloadFailed.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"),
        ("MF-List-MIB", "listProfileName"))
)
if mibBuilder.loadTexts:
    profileReloadFailed.setStatus(
        "current"
    )

fileReloadSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 11, 0, 3)
)
fileReloadSuccess.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"),
        ("MF-List-MIB", "listFileName"))
)
if mibBuilder.loadTexts:
    fileReloadSuccess.setStatus(
        "current"
    )

fileReloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 11, 0, 4)
)
fileReloadFailed.setObjects(
      *(("MF-MIB", "severity"),
        ("MF-MIB", "moduleName"),
        ("MF-List-MIB", "listFileName"))
)
if mibBuilder.loadTexts:
    fileReloadFailed.setStatus(
        "current"
    )


# Notifications groups

mfListNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 39216, 1, 50, 7, 10)
)
mfListNotifGroup.setObjects(
      *(("MF-List-MIB", "profileReloadSuccess"),
        ("MF-List-MIB", "profileReloadFailed"),
        ("MF-List-MIB", "fileReloadSuccess"),
        ("MF-List-MIB", "fileReloadFailed"))
)
if mibBuilder.loadTexts:
    mfListNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MF-List-MIB",
    **{"ListOperationalStatus": ListOperationalStatus,
       "mfList": mfList,
       "mfListGroup": mfListGroup,
       "listFilesTable": listFilesTable,
       "listFilesEntry": listFilesEntry,
       "listProfIndex": listProfIndex,
       "listFileIndex": listFileIndex,
       "listFileName": listFileName,
       "listFileReload": listFileReload,
       "listFileStatus": listFileStatus,
       "listFileNumberOfRecords": listFileNumberOfRecords,
       "listFileDuplicateRecords": listFileDuplicateRecords,
       "listFileLastLoadedOn": listFileLastLoadedOn,
       "listFileTotalReloads": listFileTotalReloads,
       "listFileSuccessfulReload": listFileSuccessfulReload,
       "listFileFailedReload": listFileFailedReload,
       "listFileTotalQueries": listFileTotalQueries,
       "listProfilesTable": listProfilesTable,
       "listProfilesEntry": listProfilesEntry,
       "listProfileIndex": listProfileIndex,
       "listProfileAdminStatus": listProfileAdminStatus,
       "listProfileName": listProfileName,
       "listProfileDescription": listProfileDescription,
       "listProfileLastActivatedOn": listProfileLastActivatedOn,
       "listProfileOperationalStatus": listProfileOperationalStatus,
       "listProfileNumberOfRecords": listProfileNumberOfRecords,
       "listProfileNumberOfUsers": listProfileNumberOfUsers,
       "listProfileTotalReloads": listProfileTotalReloads,
       "listProfileSuccessfulReload": listProfileSuccessfulReload,
       "listProfileFailedReload": listProfileFailedReload,
       "listProfileTotalQueries": listProfileTotalQueries,
       "listProfileQueryResultFound": listProfileQueryResultFound,
       "listProfileQueryResultFailed": listProfileQueryResultFailed,
       "listProfileQueryResultNotFound": listProfileQueryResultNotFound,
       "activateProfile": activateProfile,
       "mfListNotifGroup": mfListNotifGroup,
       "mfListNotifications": mfListNotifications,
       "profileReloadSuccess": profileReloadSuccess,
       "profileReloadFailed": profileReloadFailed,
       "fileReloadSuccess": fileReloadSuccess,
       "fileReloadFailed": fileReloadFailed}
)
