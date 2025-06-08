# SNMP MIB module (CIENA-CES-FILE-TRANSFER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_1271/CIENA-CES-FILE-TRANSFER-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:39:46 2025
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

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

cienaCesFileTransferMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 15)
)
if mibBuilder.loadTexts:
    cienaCesFileTransferMIB.setRevisions(
        ("2017-06-07 00:00",
         "2011-02-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesFileTransferMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesFileTransferMIBObjects = _CienaCesFileTransferMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1)
)
_CienaCesFileTransfer_ObjectIdentity = ObjectIdentity
cienaCesFileTransfer = _CienaCesFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1, 1)
)
_CienaCesFTransferRemoteFilename_Type = DisplayString
_CienaCesFTransferRemoteFilename_Object = MibScalar
cienaCesFTransferRemoteFilename = _CienaCesFTransferRemoteFilename_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1, 1, 1),
    _CienaCesFTransferRemoteFilename_Type()
)
cienaCesFTransferRemoteFilename.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesFTransferRemoteFilename.setStatus("current")
_CienaCesFTransferLocalFilename_Type = DisplayString
_CienaCesFTransferLocalFilename_Object = MibScalar
cienaCesFTransferLocalFilename = _CienaCesFTransferLocalFilename_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1, 1, 2),
    _CienaCesFTransferLocalFilename_Type()
)
cienaCesFTransferLocalFilename.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesFTransferLocalFilename.setStatus("current")


class _CienaCesFTransferNotificationStatus_Type(Integer32):
    """Custom type cienaCesFTransferNotificationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("noStatus", 0),
          ("fileAlreadyExist", 1),
          ("tftpServerNotFound", 2),
          ("fileGetError", 3),
          ("filePutError", 4),
          ("fileSystemError", 5),
          ("fileContentsInvalid", 6),
          ("flashOffline", 7),
          ("badFileCrc", 8),
          ("allFilesSkipped", 9),
          ("serverIpAddrInvalid", 10),
          ("filePathInvalid", 11),
          ("fileNameInvalid", 12),
          ("sourceNotFound", 13),
          ("fileNameNeeded", 14),
          ("notEnoughSpace", 15),
          ("putSuccessful", 16),
          ("downloadSuccess", 17),
          ("internalError", 18))
    )


_CienaCesFTransferNotificationStatus_Type.__name__ = "Integer32"
_CienaCesFTransferNotificationStatus_Object = MibScalar
cienaCesFTransferNotificationStatus = _CienaCesFTransferNotificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1, 1, 3),
    _CienaCesFTransferNotificationStatus_Type()
)
cienaCesFTransferNotificationStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesFTransferNotificationStatus.setStatus("current")
_CienaCesFTransferNotificationInfo_Type = DisplayString
_CienaCesFTransferNotificationInfo_Object = MibScalar
cienaCesFTransferNotificationInfo = _CienaCesFTransferNotificationInfo_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 15, 1, 1, 4),
    _CienaCesFTransferNotificationInfo_Type()
)
cienaCesFTransferNotificationInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cienaCesFTransferNotificationInfo.setStatus("current")
_CienaCesFileTransferMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesFileTransferMIBNotificationPrefix = _CienaCesFileTransferMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 16)
)
_CienaCesFileTransferMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesFileTransferMIBNotifications = _CienaCesFileTransferMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 16, 0)
)

# Managed Objects groups


# Notification objects

cienaCesFTransferCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 16, 0, 1)
)
cienaCesFTransferCompletion.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-FILE-TRANSFER-MIB", "cienaCesFTransferRemoteFilename"),
        ("CIENA-CES-FILE-TRANSFER-MIB", "cienaCesFTransferLocalFilename"),
        ("CIENA-CES-FILE-TRANSFER-MIB", "cienaCesFTransferNotificationStatus"),
        ("CIENA-CES-FILE-TRANSFER-MIB", "cienaCesFTransferNotificationInfo"))
)
if mibBuilder.loadTexts:
    cienaCesFTransferCompletion.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-FILE-TRANSFER-MIB",
    **{"cienaCesFileTransferMIB": cienaCesFileTransferMIB,
       "cienaCesFileTransferMIBObjects": cienaCesFileTransferMIBObjects,
       "cienaCesFileTransfer": cienaCesFileTransfer,
       "cienaCesFTransferRemoteFilename": cienaCesFTransferRemoteFilename,
       "cienaCesFTransferLocalFilename": cienaCesFTransferLocalFilename,
       "cienaCesFTransferNotificationStatus": cienaCesFTransferNotificationStatus,
       "cienaCesFTransferNotificationInfo": cienaCesFTransferNotificationInfo,
       "cienaCesFileTransferMIBNotificationPrefix": cienaCesFileTransferMIBNotificationPrefix,
       "cienaCesFileTransferMIBNotifications": cienaCesFileTransferMIBNotifications,
       "cienaCesFTransferCompletion": cienaCesFTransferCompletion}
)
