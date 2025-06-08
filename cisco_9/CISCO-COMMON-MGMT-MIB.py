# SNMP MIB module (CISCO-COMMON-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-COMMON-MGMT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:55:31 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(usmNoAuthProtocol,
 usmNoPrivProtocol) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "usmNoAuthProtocol",
    "usmNoPrivProtocol")

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
 dod,
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
    "dod",
    "iso")

(AutonomousType,
 DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCommonMgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 443)
)
if mibBuilder.loadTexts:
    ciscoCommonMgmtMIB.setRevisions(
        ("2008-06-13 00:00",
         "2005-06-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCommonMgmtNotifs_ObjectIdentity = ObjectIdentity
ciscoCommonMgmtNotifs = _CiscoCommonMgmtNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 0)
)
_CiscoCommonMgmtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCommonMgmtMIBObjects = _CiscoCommonMgmtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1)
)
_CcmUserConfig_ObjectIdentity = ObjectIdentity
ccmUserConfig = _CcmUserConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1)
)


class _CcmCommonMaxUsers_Type(Unsigned32):
    """Custom type ccmCommonMaxUsers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcmCommonMaxUsers_Type.__name__ = "Unsigned32"
_CcmCommonMaxUsers_Object = MibScalar
ccmCommonMaxUsers = _CcmCommonMaxUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 1),
    _CcmCommonMaxUsers_Type()
)
ccmCommonMaxUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCommonMaxUsers.setStatus("current")


class _CcmCommonUsers_Type(Unsigned32):
    """Custom type ccmCommonUsers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CcmCommonUsers_Type.__name__ = "Unsigned32"
_CcmCommonUsers_Object = MibScalar
ccmCommonUsers = _CcmCommonUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 2),
    _CcmCommonUsers_Type()
)
ccmCommonUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCommonUsers.setStatus("current")


class _CcmCommonUsersGlobalEnforcePriv_Type(TruthValue):
    """Custom type ccmCommonUsersGlobalEnforcePriv based on TruthValue"""
    defaultValue = 2


_CcmCommonUsersGlobalEnforcePriv_Type.__name__ = "TruthValue"
_CcmCommonUsersGlobalEnforcePriv_Object = MibScalar
ccmCommonUsersGlobalEnforcePriv = _CcmCommonUsersGlobalEnforcePriv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 3),
    _CcmCommonUsersGlobalEnforcePriv_Type()
)
ccmCommonUsersGlobalEnforcePriv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmCommonUsersGlobalEnforcePriv.setStatus("current")
_CcmCommonUserLastChange_Type = DateAndTime
_CcmCommonUserLastChange_Object = MibScalar
ccmCommonUserLastChange = _CcmCommonUserLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 4),
    _CcmCommonUserLastChange_Type()
)
ccmCommonUserLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCommonUserLastChange.setStatus("current")
_CcmCommonUserTable_Object = MibTable
ccmCommonUserTable = _CcmCommonUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ccmCommonUserTable.setStatus("current")
_CcmCommonUserEntry_Object = MibTableRow
ccmCommonUserEntry = _CcmCommonUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1)
)
ccmCommonUserEntry.setIndexNames(
    (0, "CISCO-COMMON-MGMT-MIB", "ccmCommonUserName"),
)
if mibBuilder.loadTexts:
    ccmCommonUserEntry.setStatus("current")


class _CcmCommonUserName_Type(SnmpAdminString):
    """Custom type ccmCommonUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcmCommonUserName_Type.__name__ = "SnmpAdminString"
_CcmCommonUserName_Object = MibTableColumn
ccmCommonUserName = _CcmCommonUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 1),
    _CcmCommonUserName_Type()
)
ccmCommonUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmCommonUserName.setStatus("current")


class _CcmCommonUserPassword_Type(DisplayString):
    """Custom type ccmCommonUserPassword based on DisplayString"""
    defaultHexValue = ""


_CcmCommonUserPassword_Type.__name__ = "DisplayString"
_CcmCommonUserPassword_Object = MibTableColumn
ccmCommonUserPassword = _CcmCommonUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 2),
    _CcmCommonUserPassword_Type()
)
ccmCommonUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmCommonUserPassword.setStatus("current")


class _CcmCommonUserExpiryDate_Type(DateAndTime):
    """Custom type ccmCommonUserExpiryDate based on DateAndTime"""
    defaultHexValue = "0000000000000000000000"


_CcmCommonUserExpiryDate_Type.__name__ = "DateAndTime"
_CcmCommonUserExpiryDate_Object = MibTableColumn
ccmCommonUserExpiryDate = _CcmCommonUserExpiryDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 3),
    _CcmCommonUserExpiryDate_Type()
)
ccmCommonUserExpiryDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmCommonUserExpiryDate.setStatus("current")


class _CcmCommonUserSshKeyFilename_Type(SnmpAdminString):
    """Custom type ccmCommonUserSshKeyFilename based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcmCommonUserSshKeyFilename_Type.__name__ = "SnmpAdminString"
_CcmCommonUserSshKeyFilename_Object = MibTableColumn
ccmCommonUserSshKeyFilename = _CcmCommonUserSshKeyFilename_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 4),
    _CcmCommonUserSshKeyFilename_Type()
)
ccmCommonUserSshKeyFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmCommonUserSshKeyFilename.setStatus("current")
_CcmCommonUserSshKeyConfigured_Type = TruthValue
_CcmCommonUserSshKeyConfigured_Object = MibTableColumn
ccmCommonUserSshKeyConfigured = _CcmCommonUserSshKeyConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 5),
    _CcmCommonUserSshKeyConfigured_Type()
)
ccmCommonUserSshKeyConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCommonUserSshKeyConfigured.setStatus("current")


class _CcmCommonUserSNMPAuthProtocol_Type(AutonomousType):
    """Custom type ccmCommonUserSNMPAuthProtocol based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 6, 3, 10, 1, 1, 1)


_CcmCommonUserSNMPAuthProtocol_Type.__name__ = "AutonomousType"
_CcmCommonUserSNMPAuthProtocol_Object = MibTableColumn
ccmCommonUserSNMPAuthProtocol = _CcmCommonUserSNMPAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 6),
    _CcmCommonUserSNMPAuthProtocol_Type()
)
ccmCommonUserSNMPAuthProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmCommonUserSNMPAuthProtocol.setStatus("current")


class _CcmCommonUserSNMPPrivProtocol_Type(AutonomousType):
    """Custom type ccmCommonUserSNMPPrivProtocol based on AutonomousType"""
    defaultValue = (1, 3, 6, 1, 6, 3, 10, 1, 2, 1)


_CcmCommonUserSNMPPrivProtocol_Type.__name__ = "AutonomousType"
_CcmCommonUserSNMPPrivProtocol_Object = MibTableColumn
ccmCommonUserSNMPPrivProtocol = _CcmCommonUserSNMPPrivProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 7),
    _CcmCommonUserSNMPPrivProtocol_Type()
)
ccmCommonUserSNMPPrivProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmCommonUserSNMPPrivProtocol.setStatus("current")


class _CcmCommonUserCredType_Type(Integer32):
    """Custom type ccmCommonUserCredType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("localCredentialStore", 2),
          ("remoteCredentialStore", 3))
    )


_CcmCommonUserCredType_Type.__name__ = "Integer32"
_CcmCommonUserCredType_Object = MibTableColumn
ccmCommonUserCredType = _CcmCommonUserCredType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 8),
    _CcmCommonUserCredType_Type()
)
ccmCommonUserCredType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccmCommonUserCredType.setStatus("current")


class _CcmCommonUserStorageType_Type(StorageType):
    """Custom type ccmCommonUserStorageType based on StorageType"""
    defaultValue = 3


_CcmCommonUserStorageType_Type.__name__ = "StorageType"
_CcmCommonUserStorageType_Object = MibTableColumn
ccmCommonUserStorageType = _CcmCommonUserStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 9),
    _CcmCommonUserStorageType_Type()
)
ccmCommonUserStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmCommonUserStorageType.setStatus("current")
_CcmCommonUserRowStatus_Type = RowStatus
_CcmCommonUserRowStatus_Object = MibTableColumn
ccmCommonUserRowStatus = _CcmCommonUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 5, 1, 10),
    _CcmCommonUserRowStatus_Type()
)
ccmCommonUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmCommonUserRowStatus.setStatus("current")
_CcmCommonUserRoleTable_Object = MibTable
ccmCommonUserRoleTable = _CcmCommonUserRoleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ccmCommonUserRoleTable.setStatus("current")
_CcmCommonUserRoleEntry_Object = MibTableRow
ccmCommonUserRoleEntry = _CcmCommonUserRoleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 6, 1)
)
ccmCommonUserRoleEntry.setIndexNames(
    (0, "CISCO-COMMON-MGMT-MIB", "ccmCommonUserName"),
    (0, "CISCO-COMMON-MGMT-MIB", "ccmCommonUserRoleName"),
)
if mibBuilder.loadTexts:
    ccmCommonUserRoleEntry.setStatus("current")


class _CcmCommonUserRoleName_Type(SnmpAdminString):
    """Custom type ccmCommonUserRoleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CcmCommonUserRoleName_Type.__name__ = "SnmpAdminString"
_CcmCommonUserRoleName_Object = MibTableColumn
ccmCommonUserRoleName = _CcmCommonUserRoleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 6, 1, 1),
    _CcmCommonUserRoleName_Type()
)
ccmCommonUserRoleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccmCommonUserRoleName.setStatus("current")


class _CcmCommonUserRoleStorageType_Type(StorageType):
    """Custom type ccmCommonUserRoleStorageType based on StorageType"""
    defaultValue = 3


_CcmCommonUserRoleStorageType_Type.__name__ = "StorageType"
_CcmCommonUserRoleStorageType_Object = MibTableColumn
ccmCommonUserRoleStorageType = _CcmCommonUserRoleStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 6, 1, 2),
    _CcmCommonUserRoleStorageType_Type()
)
ccmCommonUserRoleStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmCommonUserRoleStorageType.setStatus("current")
_CcmCommonUserRoleRowStatus_Type = RowStatus
_CcmCommonUserRoleRowStatus_Object = MibTableColumn
ccmCommonUserRoleRowStatus = _CcmCommonUserRoleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 6, 1, 3),
    _CcmCommonUserRoleRowStatus_Type()
)
ccmCommonUserRoleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccmCommonUserRoleRowStatus.setStatus("current")


class _CcmCommonUserCacheTimeout_Type(Unsigned32):
    """Custom type ccmCommonUserCacheTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CcmCommonUserCacheTimeout_Type.__name__ = "Unsigned32"
_CcmCommonUserCacheTimeout_Object = MibScalar
ccmCommonUserCacheTimeout = _CcmCommonUserCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 1, 1, 7),
    _CcmCommonUserCacheTimeout_Type()
)
ccmCommonUserCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccmCommonUserCacheTimeout.setStatus("current")
if mibBuilder.loadTexts:
    ccmCommonUserCacheTimeout.setUnits("seconds")
_CiscoCommonMgmtMIBConform_ObjectIdentity = ObjectIdentity
ciscoCommonMgmtMIBConform = _CiscoCommonMgmtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 2)
)
_CiscoCommonMgmtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCommonMgmtMIBCompliances = _CiscoCommonMgmtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 1)
)
_CiscoCommonMgmtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCommonMgmtMIBGroups = _CiscoCommonMgmtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 2)
)

# Managed Objects groups

ccmConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 2, 1)
)
ccmConfigurationGroup.setObjects(
      *(("CISCO-COMMON-MGMT-MIB", "ccmCommonMaxUsers"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUsers"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUsersGlobalEnforcePriv"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserLastChange"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserPassword"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserExpiryDate"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserSshKeyFilename"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserSshKeyConfigured"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserSNMPAuthProtocol"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserSNMPPrivProtocol"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserCredType"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserStorageType"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserRowStatus"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserRoleStorageType"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserRoleRowStatus"))
)
if mibBuilder.loadTexts:
    ccmConfigurationGroup.setStatus("current")

ccmCacheTimeoutConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 2, 2)
)
ccmCacheTimeoutConfigGroup.setObjects(
    ("CISCO-COMMON-MGMT-MIB", "ccmCommonUserCacheTimeout")
)
if mibBuilder.loadTexts:
    ccmCacheTimeoutConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCommonMgmtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 1, 1)
)
ciscoCommonMgmtMIBCompliance.setObjects(
    ("CISCO-COMMON-MGMT-MIB", "ccmConfigurationGroup")
)
if mibBuilder.loadTexts:
    ciscoCommonMgmtMIBCompliance.setStatus(
        "obsolete"
    )

ciscoCommonMgmtMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 443, 2, 1, 2)
)
ciscoCommonMgmtMIBCompliance1.setObjects(
      *(("CISCO-COMMON-MGMT-MIB", "ccmConfigurationGroup"),
        ("CISCO-COMMON-MGMT-MIB", "ccmCacheTimeoutConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoCommonMgmtMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-COMMON-MGMT-MIB",
    **{"ciscoCommonMgmtMIB": ciscoCommonMgmtMIB,
       "ciscoCommonMgmtNotifs": ciscoCommonMgmtNotifs,
       "ciscoCommonMgmtMIBObjects": ciscoCommonMgmtMIBObjects,
       "ccmUserConfig": ccmUserConfig,
       "ccmCommonMaxUsers": ccmCommonMaxUsers,
       "ccmCommonUsers": ccmCommonUsers,
       "ccmCommonUsersGlobalEnforcePriv": ccmCommonUsersGlobalEnforcePriv,
       "ccmCommonUserLastChange": ccmCommonUserLastChange,
       "ccmCommonUserTable": ccmCommonUserTable,
       "ccmCommonUserEntry": ccmCommonUserEntry,
       "ccmCommonUserName": ccmCommonUserName,
       "ccmCommonUserPassword": ccmCommonUserPassword,
       "ccmCommonUserExpiryDate": ccmCommonUserExpiryDate,
       "ccmCommonUserSshKeyFilename": ccmCommonUserSshKeyFilename,
       "ccmCommonUserSshKeyConfigured": ccmCommonUserSshKeyConfigured,
       "ccmCommonUserSNMPAuthProtocol": ccmCommonUserSNMPAuthProtocol,
       "ccmCommonUserSNMPPrivProtocol": ccmCommonUserSNMPPrivProtocol,
       "ccmCommonUserCredType": ccmCommonUserCredType,
       "ccmCommonUserStorageType": ccmCommonUserStorageType,
       "ccmCommonUserRowStatus": ccmCommonUserRowStatus,
       "ccmCommonUserRoleTable": ccmCommonUserRoleTable,
       "ccmCommonUserRoleEntry": ccmCommonUserRoleEntry,
       "ccmCommonUserRoleName": ccmCommonUserRoleName,
       "ccmCommonUserRoleStorageType": ccmCommonUserRoleStorageType,
       "ccmCommonUserRoleRowStatus": ccmCommonUserRoleRowStatus,
       "ccmCommonUserCacheTimeout": ccmCommonUserCacheTimeout,
       "ciscoCommonMgmtMIBConform": ciscoCommonMgmtMIBConform,
       "ciscoCommonMgmtMIBCompliances": ciscoCommonMgmtMIBCompliances,
       "ciscoCommonMgmtMIBCompliance": ciscoCommonMgmtMIBCompliance,
       "ciscoCommonMgmtMIBCompliance1": ciscoCommonMgmtMIBCompliance1,
       "ciscoCommonMgmtMIBGroups": ciscoCommonMgmtMIBGroups,
       "ccmConfigurationGroup": ccmConfigurationGroup,
       "ccmCacheTimeoutConfigGroup": ccmCacheTimeoutConfigGroup}
)
