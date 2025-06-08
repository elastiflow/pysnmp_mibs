# SNMP MIB module (RBN-CONFIG-FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/RBN-CONFIG-FILE-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:52 2025
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

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rbnConfigFileMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13)
)
if mibBuilder.loadTexts:
    rbnConfigFileMib.setRevisions(
        ("2011-01-19 18:00",
         "2002-05-29 00:00",
         "2001-10-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnConfigFileMIBNotifications_ObjectIdentity = ObjectIdentity
rbnConfigFileMIBNotifications = _RbnConfigFileMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 0)
)
_RbnConfigFileMIBObjects_ObjectIdentity = ObjectIdentity
rbnConfigFileMIBObjects = _RbnConfigFileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1)
)
_RcfJobs_ObjectIdentity = ObjectIdentity
rcfJobs = _RcfJobs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1)
)
_RcfJobSpinLock_Type = TestAndIncr
_RcfJobSpinLock_Object = MibScalar
rcfJobSpinLock = _RcfJobSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 1),
    _RcfJobSpinLock_Type()
)
rcfJobSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcfJobSpinLock.setStatus("current")
_RcfJobNextIndex_Type = Unsigned32
_RcfJobNextIndex_Object = MibScalar
rcfJobNextIndex = _RcfJobNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 2),
    _RcfJobNextIndex_Type()
)
rcfJobNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcfJobNextIndex.setStatus("current")
_RcfJobTable_Object = MibTable
rcfJobTable = _RcfJobTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rcfJobTable.setStatus("current")
_RcfJobEntry_Object = MibTableRow
rcfJobEntry = _RcfJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1)
)
rcfJobEntry.setIndexNames(
    (0, "RBN-CONFIG-FILE-MIB", "rcfJobIndex"),
)
if mibBuilder.loadTexts:
    rcfJobEntry.setStatus("current")


class _RcfJobIndex_Type(Unsigned32):
    """Custom type rcfJobIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RcfJobIndex_Type.__name__ = "Unsigned32"
_RcfJobIndex_Object = MibTableColumn
rcfJobIndex = _RcfJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 1),
    _RcfJobIndex_Type()
)
rcfJobIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcfJobIndex.setStatus("current")


class _RcfJobOp_Type(Integer32):
    """Custom type rcfJobOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("load", 0),
          ("save", 1))
    )


_RcfJobOp_Type.__name__ = "Integer32"
_RcfJobOp_Object = MibTableColumn
rcfJobOp = _RcfJobOp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 2),
    _RcfJobOp_Type()
)
rcfJobOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobOp.setStatus("current")


class _RcfJobProtocol_Type(Integer32):
    """Custom type rcfJobProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("tftp", 1),
          ("ftp", 2))
    )


_RcfJobProtocol_Type.__name__ = "Integer32"
_RcfJobProtocol_Object = MibTableColumn
rcfJobProtocol = _RcfJobProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 3),
    _RcfJobProtocol_Type()
)
rcfJobProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobProtocol.setStatus("current")


class _RcfJobFilename_Type(SnmpAdminString):
    """Custom type rcfJobFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RcfJobFilename_Type.__name__ = "SnmpAdminString"
_RcfJobFilename_Object = MibTableColumn
rcfJobFilename = _RcfJobFilename_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 4),
    _RcfJobFilename_Type()
)
rcfJobFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobFilename.setStatus("current")
_RcfJobIpAddressType_Type = InetAddressType
_RcfJobIpAddressType_Object = MibTableColumn
rcfJobIpAddressType = _RcfJobIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 5),
    _RcfJobIpAddressType_Type()
)
rcfJobIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobIpAddressType.setStatus("current")
_RcfJobIpAddress_Type = InetAddress
_RcfJobIpAddress_Object = MibTableColumn
rcfJobIpAddress = _RcfJobIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 6),
    _RcfJobIpAddress_Type()
)
rcfJobIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobIpAddress.setStatus("current")


class _RcfJobUsername_Type(SnmpAdminString):
    """Custom type rcfJobUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RcfJobUsername_Type.__name__ = "SnmpAdminString"
_RcfJobUsername_Object = MibTableColumn
rcfJobUsername = _RcfJobUsername_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 7),
    _RcfJobUsername_Type()
)
rcfJobUsername.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobUsername.setStatus("current")


class _RcfJobPassword_Type(SnmpAdminString):
    """Custom type rcfJobPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RcfJobPassword_Type.__name__ = "SnmpAdminString"
_RcfJobPassword_Object = MibTableColumn
rcfJobPassword = _RcfJobPassword_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 8),
    _RcfJobPassword_Type()
)
rcfJobPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobPassword.setStatus("current")


class _RcfJobPassiveMode_Type(TruthValue):
    """Custom type rcfJobPassiveMode based on TruthValue"""
    defaultValue = 2


_RcfJobPassiveMode_Type.__name__ = "TruthValue"
_RcfJobPassiveMode_Object = MibTableColumn
rcfJobPassiveMode = _RcfJobPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 9),
    _RcfJobPassiveMode_Type()
)
rcfJobPassiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobPassiveMode.setStatus("current")


class _RcfJobStopAtLine_Type(Unsigned32):
    """Custom type rcfJobStopAtLine based on Unsigned32"""
    defaultValue = 0


_RcfJobStopAtLine_Type.__name__ = "Unsigned32"
_RcfJobStopAtLine_Object = MibTableColumn
rcfJobStopAtLine = _RcfJobStopAtLine_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 10),
    _RcfJobStopAtLine_Type()
)
rcfJobStopAtLine.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobStopAtLine.setStatus("current")


class _RcfJobSaveDefaults_Type(TruthValue):
    """Custom type rcfJobSaveDefaults based on TruthValue"""
    defaultValue = 2


_RcfJobSaveDefaults_Type.__name__ = "TruthValue"
_RcfJobSaveDefaults_Object = MibTableColumn
rcfJobSaveDefaults = _RcfJobSaveDefaults_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 11),
    _RcfJobSaveDefaults_Type()
)
rcfJobSaveDefaults.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobSaveDefaults.setStatus("current")


class _RcfJobState_Type(Integer32):
    """Custom type rcfJobState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pending", 0),
          ("inProgress", 1),
          ("completed", 2))
    )


_RcfJobState_Type.__name__ = "Integer32"
_RcfJobState_Object = MibTableColumn
rcfJobState = _RcfJobState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 12),
    _RcfJobState_Type()
)
rcfJobState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcfJobState.setStatus("current")


class _RcfJobResult_Type(Integer32):
    """Custom type rcfJobResult based on Integer32"""
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
        *(("success", 0),
          ("other", 1),
          ("noMemory", 2),
          ("parse", 3),
          ("io", 4),
          ("access", 5))
    )


_RcfJobResult_Type.__name__ = "Integer32"
_RcfJobResult_Object = MibTableColumn
rcfJobResult = _RcfJobResult_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 13),
    _RcfJobResult_Type()
)
rcfJobResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcfJobResult.setStatus("current")
_RcfJobErrorMsgs_Type = SnmpAdminString
_RcfJobErrorMsgs_Object = MibTableColumn
rcfJobErrorMsgs = _RcfJobErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 14),
    _RcfJobErrorMsgs_Type()
)
rcfJobErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcfJobErrorMsgs.setStatus("current")
_RcfJobCreateTime_Type = TimeStamp
_RcfJobCreateTime_Object = MibTableColumn
rcfJobCreateTime = _RcfJobCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 15),
    _RcfJobCreateTime_Type()
)
rcfJobCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcfJobCreateTime.setStatus("current")
_RcfJobStartTime_Type = TimeStamp
_RcfJobStartTime_Object = MibTableColumn
rcfJobStartTime = _RcfJobStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 16),
    _RcfJobStartTime_Type()
)
rcfJobStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcfJobStartTime.setStatus("current")
_RcfJobStopTime_Type = TimeStamp
_RcfJobStopTime_Object = MibTableColumn
rcfJobStopTime = _RcfJobStopTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 17),
    _RcfJobStopTime_Type()
)
rcfJobStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcfJobStopTime.setStatus("current")


class _RcfJobNotifyOnCompletion_Type(TruthValue):
    """Custom type rcfJobNotifyOnCompletion based on TruthValue"""
    defaultValue = 2


_RcfJobNotifyOnCompletion_Type.__name__ = "TruthValue"
_RcfJobNotifyOnCompletion_Object = MibTableColumn
rcfJobNotifyOnCompletion = _RcfJobNotifyOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 18),
    _RcfJobNotifyOnCompletion_Type()
)
rcfJobNotifyOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobNotifyOnCompletion.setStatus("current")


class _RcfJobOwner_Type(OwnerString):
    """Custom type rcfJobOwner based on OwnerString"""
    defaultValue = OctetString("")


_RcfJobOwner_Type.__name__ = "OwnerString"
_RcfJobOwner_Object = MibTableColumn
rcfJobOwner = _RcfJobOwner_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 19),
    _RcfJobOwner_Type()
)
rcfJobOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobOwner.setStatus("current")
_RcfJobRowStatus_Type = RowStatus
_RcfJobRowStatus_Object = MibTableColumn
rcfJobRowStatus = _RcfJobRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 1, 1, 3, 1, 20),
    _RcfJobRowStatus_Type()
)
rcfJobRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcfJobRowStatus.setStatus("current")
_RbnConfigFileMIBConformance_ObjectIdentity = ObjectIdentity
rbnConfigFileMIBConformance = _RbnConfigFileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 2)
)
_RbnConfigFileCompliances_ObjectIdentity = ObjectIdentity
rbnConfigFileCompliances = _RbnConfigFileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 2, 1)
)
_RbnConfigFileGroups_ObjectIdentity = ObjectIdentity
rbnConfigFileGroups = _RbnConfigFileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 2, 2)
)

# Managed Objects groups

rcfJobGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 2, 2, 1)
)
rcfJobGroup.setObjects(
      *(("RBN-CONFIG-FILE-MIB", "rcfJobSpinLock"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobNextIndex"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobOp"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobProtocol"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobFilename"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobIpAddressType"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobIpAddress"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobUsername"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobPassword"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobPassiveMode"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobStopAtLine"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobSaveDefaults"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobState"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobResult"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobCreateTime"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobStartTime"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobStopTime"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobErrorMsgs"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobNotifyOnCompletion"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobOwner"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobRowStatus"))
)
if mibBuilder.loadTexts:
    rcfJobGroup.setStatus("current")


# Notification objects

rcfJobCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 0, 1)
)
rcfJobCompleted.setObjects(
      *(("RBN-CONFIG-FILE-MIB", "rcfJobResult"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobErrorMsgs"))
)
if mibBuilder.loadTexts:
    rcfJobCompleted.setStatus(
        "current"
    )


# Notifications groups

rcfJobNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 2, 2, 2)
)
rcfJobNotifyGroup.setObjects(
    ("RBN-CONFIG-FILE-MIB", "rcfJobCompleted")
)
if mibBuilder.loadTexts:
    rcfJobNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnConfigFileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 13, 2, 1, 1)
)
rbnConfigFileCompliance.setObjects(
      *(("RBN-CONFIG-FILE-MIB", "rcfJobGroup"),
        ("RBN-CONFIG-FILE-MIB", "rcfJobNotifyGroup"))
)
if mibBuilder.loadTexts:
    rbnConfigFileCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-CONFIG-FILE-MIB",
    **{"rbnConfigFileMib": rbnConfigFileMib,
       "rbnConfigFileMIBNotifications": rbnConfigFileMIBNotifications,
       "rcfJobCompleted": rcfJobCompleted,
       "rbnConfigFileMIBObjects": rbnConfigFileMIBObjects,
       "rcfJobs": rcfJobs,
       "rcfJobSpinLock": rcfJobSpinLock,
       "rcfJobNextIndex": rcfJobNextIndex,
       "rcfJobTable": rcfJobTable,
       "rcfJobEntry": rcfJobEntry,
       "rcfJobIndex": rcfJobIndex,
       "rcfJobOp": rcfJobOp,
       "rcfJobProtocol": rcfJobProtocol,
       "rcfJobFilename": rcfJobFilename,
       "rcfJobIpAddressType": rcfJobIpAddressType,
       "rcfJobIpAddress": rcfJobIpAddress,
       "rcfJobUsername": rcfJobUsername,
       "rcfJobPassword": rcfJobPassword,
       "rcfJobPassiveMode": rcfJobPassiveMode,
       "rcfJobStopAtLine": rcfJobStopAtLine,
       "rcfJobSaveDefaults": rcfJobSaveDefaults,
       "rcfJobState": rcfJobState,
       "rcfJobResult": rcfJobResult,
       "rcfJobErrorMsgs": rcfJobErrorMsgs,
       "rcfJobCreateTime": rcfJobCreateTime,
       "rcfJobStartTime": rcfJobStartTime,
       "rcfJobStopTime": rcfJobStopTime,
       "rcfJobNotifyOnCompletion": rcfJobNotifyOnCompletion,
       "rcfJobOwner": rcfJobOwner,
       "rcfJobRowStatus": rcfJobRowStatus,
       "rbnConfigFileMIBConformance": rbnConfigFileMIBConformance,
       "rbnConfigFileCompliances": rbnConfigFileCompliances,
       "rbnConfigFileCompliance": rbnConfigFileCompliance,
       "rbnConfigFileGroups": rbnConfigFileGroups,
       "rcfJobGroup": rcfJobGroup,
       "rcfJobNotifyGroup": rcfJobNotifyGroup}
)
