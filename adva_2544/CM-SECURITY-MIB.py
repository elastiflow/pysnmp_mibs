# SNMP MIB module (CM-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/CM-SECURITY-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:57 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(IpVersion,
 UserInterfaceType) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "IpVersion",
    "UserInterfaceType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(usmUserEntry,) = mibBuilder.importSymbols(
    "SNMP-USER-BASED-SM-MIB",
    "usmUserEntry")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cmSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10)
)
if mibBuilder.loadTexts:
    cmSecurityMIB.setRevisions(
        ("2016-06-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CmRemoteAuthProtocol(TextualConvention, Integer32):
    status = "current"
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
          ("radius", 2),
          ("tacacs", 3))
    )



class CmSecurityAccessOrder(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )



class CmSecurityAuthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pap", 1),
          ("chap", 2))
    )



class CmSecurityPrivLevel(TextualConvention, Integer32):
    status = "current"
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("retrieve", 1),
          ("maintenance", 2),
          ("provisioning", 3),
          ("superuser", 4),
          ("testuser", 5),
          ("cryptouser", 6),
          ("netconf", 7))
    )



class CmRemoteAuthOrder(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("second", 2),
          ("third", 3))
    )



class CmSecurityPolicyStrength(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("medium", 2),
          ("high", 3))
    )



class UsmUserAccessType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 1),
          ("read-write", 2),
          ("trap-only", 3))
    )



class SecurityUserAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("remove-lockout", 1))
    )



class SnmpSecurityTrapType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("loginFailed", 2),
          ("disabled", 3))
    )



class PrivilegeRequestAction(TextualConvention, Integer32):
    status = "current"
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
        *(("undefined", 0),
          ("none", 1),
          ("approve", 2),
          ("deny", 3),
          ("cancel", 4))
    )



class PrivilegeRequestState(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 1),
          ("requestSent", 2),
          ("requestCanceled", 3),
          ("requestApproved", 4),
          ("requestDenied", 5),
          ("requestTimeout", 6),
          ("accessExpired", 7),
          ("accessCanceled", 8))
    )



# MIB Managed Objects in the order of their OIDs

_CmSecurityObjects_ObjectIdentity = ObjectIdentity
cmSecurityObjects = _CmSecurityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1)
)
_CmAuthProtocol_Type = CmRemoteAuthProtocol
_CmAuthProtocol_Object = MibScalar
cmAuthProtocol = _CmAuthProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 1),
    _CmAuthProtocol_Type()
)
cmAuthProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAuthProtocol.setStatus("current")
_CmAccessOrder_Type = CmSecurityAccessOrder
_CmAccessOrder_Object = MibScalar
cmAccessOrder = _CmAccessOrder_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 2),
    _CmAccessOrder_Type()
)
cmAccessOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAccessOrder.setStatus("current")
_CmAuthType_Type = CmSecurityAuthType
_CmAuthType_Object = MibScalar
cmAuthType = _CmAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 3),
    _CmAuthType_Type()
)
cmAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmAuthType.setStatus("current")
_CmNASIpAddress_Type = IpAddress
_CmNASIpAddress_Object = MibScalar
cmNASIpAddress = _CmNASIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 4),
    _CmNASIpAddress_Type()
)
cmNASIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmNASIpAddress.setStatus("current")
_CmSecurityUserTable_Object = MibTable
cmSecurityUserTable = _CmSecurityUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5)
)
if mibBuilder.loadTexts:
    cmSecurityUserTable.setStatus("current")
_CmSecurityUserEntry_Object = MibTableRow
cmSecurityUserEntry = _CmSecurityUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1)
)
cmSecurityUserEntry.setIndexNames(
    (0, "CM-SECURITY-MIB", "cmSecurityUserName"),
    (0, "CM-SECURITY-MIB", "cmSecurityUserRemoteUser"),
)
if mibBuilder.loadTexts:
    cmSecurityUserEntry.setStatus("current")


class _CmSecurityUserName_Type(DisplayString):
    """Custom type cmSecurityUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CmSecurityUserName_Type.__name__ = "DisplayString"
_CmSecurityUserName_Object = MibTableColumn
cmSecurityUserName = _CmSecurityUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 1),
    _CmSecurityUserName_Type()
)
cmSecurityUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserName.setStatus("current")


class _CmSecurityUserComment_Type(DisplayString):
    """Custom type cmSecurityUserComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CmSecurityUserComment_Type.__name__ = "DisplayString"
_CmSecurityUserComment_Object = MibTableColumn
cmSecurityUserComment = _CmSecurityUserComment_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 2),
    _CmSecurityUserComment_Type()
)
cmSecurityUserComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserComment.setStatus("current")
_CmSecurityUserPrivLevel_Type = CmSecurityPrivLevel
_CmSecurityUserPrivLevel_Object = MibTableColumn
cmSecurityUserPrivLevel = _CmSecurityUserPrivLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 3),
    _CmSecurityUserPrivLevel_Type()
)
cmSecurityUserPrivLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserPrivLevel.setStatus("current")
_CmSecurityUserLoginTimeout_Type = Integer32
_CmSecurityUserLoginTimeout_Object = MibTableColumn
cmSecurityUserLoginTimeout = _CmSecurityUserLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 4),
    _CmSecurityUserLoginTimeout_Type()
)
cmSecurityUserLoginTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserLoginTimeout.setStatus("current")
_CmSecurityUserNumFailedLoginAttempts_Type = Integer32
_CmSecurityUserNumFailedLoginAttempts_Object = MibTableColumn
cmSecurityUserNumFailedLoginAttempts = _CmSecurityUserNumFailedLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 5),
    _CmSecurityUserNumFailedLoginAttempts_Type()
)
cmSecurityUserNumFailedLoginAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSecurityUserNumFailedLoginAttempts.setStatus("current")
_CmSecurityUserLastLoginTime_Type = DateAndTime
_CmSecurityUserLastLoginTime_Object = MibTableColumn
cmSecurityUserLastLoginTime = _CmSecurityUserLastLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 6),
    _CmSecurityUserLastLoginTime_Type()
)
cmSecurityUserLastLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSecurityUserLastLoginTime.setStatus("current")
_CmSecurityUserLockedout_Type = TruthValue
_CmSecurityUserLockedout_Object = MibTableColumn
cmSecurityUserLockedout = _CmSecurityUserLockedout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 7),
    _CmSecurityUserLockedout_Type()
)
cmSecurityUserLockedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSecurityUserLockedout.setStatus("current")
_CmSecurityUserLastLockedoutTime_Type = DateAndTime
_CmSecurityUserLastLockedoutTime_Object = MibTableColumn
cmSecurityUserLastLockedoutTime = _CmSecurityUserLastLockedoutTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 8),
    _CmSecurityUserLastLockedoutTime_Type()
)
cmSecurityUserLastLockedoutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSecurityUserLastLockedoutTime.setStatus("current")
_CmSecurityUserCliPagingEnable_Type = TruthValue
_CmSecurityUserCliPagingEnable_Object = MibTableColumn
cmSecurityUserCliPagingEnable = _CmSecurityUserCliPagingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 9),
    _CmSecurityUserCliPagingEnable_Type()
)
cmSecurityUserCliPagingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserCliPagingEnable.setStatus("current")
_CmSecurityUserRemoteUser_Type = TruthValue
_CmSecurityUserRemoteUser_Object = MibTableColumn
cmSecurityUserRemoteUser = _CmSecurityUserRemoteUser_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 10),
    _CmSecurityUserRemoteUser_Type()
)
cmSecurityUserRemoteUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmSecurityUserRemoteUser.setStatus("current")


class _CmSecurityUserPassword_Type(DisplayString):
    """Custom type cmSecurityUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmSecurityUserPassword_Type.__name__ = "DisplayString"
_CmSecurityUserPassword_Object = MibTableColumn
cmSecurityUserPassword = _CmSecurityUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 11),
    _CmSecurityUserPassword_Type()
)
cmSecurityUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserPassword.setStatus("current")
_CmSecurityUserStorageType_Type = StorageType
_CmSecurityUserStorageType_Object = MibTableColumn
cmSecurityUserStorageType = _CmSecurityUserStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 12),
    _CmSecurityUserStorageType_Type()
)
cmSecurityUserStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserStorageType.setStatus("current")
_CmSecurityUserRowStatus_Type = RowStatus
_CmSecurityUserRowStatus_Object = MibTableColumn
cmSecurityUserRowStatus = _CmSecurityUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 13),
    _CmSecurityUserRowStatus_Type()
)
cmSecurityUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserRowStatus.setStatus("current")
_CmSecurityUserAction_Type = SecurityUserAction
_CmSecurityUserAction_Object = MibTableColumn
cmSecurityUserAction = _CmSecurityUserAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 14),
    _CmSecurityUserAction_Type()
)
cmSecurityUserAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSecurityUserAction.setStatus("current")


class _CmSecurityCryptoPassword_Type(DisplayString):
    """Custom type cmSecurityCryptoPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CmSecurityCryptoPassword_Type.__name__ = "DisplayString"
_CmSecurityCryptoPassword_Object = MibTableColumn
cmSecurityCryptoPassword = _CmSecurityCryptoPassword_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 15),
    _CmSecurityCryptoPassword_Type()
)
cmSecurityCryptoPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityCryptoPassword.setStatus("current")
_CmSecurityUserRemoteCryptoUser_Type = TruthValue
_CmSecurityUserRemoteCryptoUser_Object = MibTableColumn
cmSecurityUserRemoteCryptoUser = _CmSecurityUserRemoteCryptoUser_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 5, 1, 16),
    _CmSecurityUserRemoteCryptoUser_Type()
)
cmSecurityUserRemoteCryptoUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmSecurityUserRemoteCryptoUser.setStatus("current")
_CmRemoteAuthServerTable_Object = MibTable
cmRemoteAuthServerTable = _CmRemoteAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6)
)
if mibBuilder.loadTexts:
    cmRemoteAuthServerTable.setStatus("current")
_CmRemoteAuthServerEntry_Object = MibTableRow
cmRemoteAuthServerEntry = _CmRemoteAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1)
)
cmRemoteAuthServerEntry.setIndexNames(
    (0, "CM-SECURITY-MIB", "cmRemoteAuthServerIndex"),
)
if mibBuilder.loadTexts:
    cmRemoteAuthServerEntry.setStatus("current")
_CmRemoteAuthServerIndex_Type = Integer32
_CmRemoteAuthServerIndex_Object = MibTableColumn
cmRemoteAuthServerIndex = _CmRemoteAuthServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 1),
    _CmRemoteAuthServerIndex_Type()
)
cmRemoteAuthServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmRemoteAuthServerIndex.setStatus("current")
_CmRemoteAuthServerEnabled_Type = TruthValue
_CmRemoteAuthServerEnabled_Object = MibTableColumn
cmRemoteAuthServerEnabled = _CmRemoteAuthServerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 2),
    _CmRemoteAuthServerEnabled_Type()
)
cmRemoteAuthServerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerEnabled.setStatus("current")
_CmRemoteAuthServerOrder_Type = CmRemoteAuthOrder
_CmRemoteAuthServerOrder_Object = MibTableColumn
cmRemoteAuthServerOrder = _CmRemoteAuthServerOrder_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 3),
    _CmRemoteAuthServerOrder_Type()
)
cmRemoteAuthServerOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerOrder.setStatus("current")
_CmRemoteAuthServerIpAddress_Type = IpAddress
_CmRemoteAuthServerIpAddress_Object = MibTableColumn
cmRemoteAuthServerIpAddress = _CmRemoteAuthServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 4),
    _CmRemoteAuthServerIpAddress_Type()
)
cmRemoteAuthServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerIpAddress.setStatus("current")
_CmRemoteAuthServerPort_Type = Integer32
_CmRemoteAuthServerPort_Object = MibTableColumn
cmRemoteAuthServerPort = _CmRemoteAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 5),
    _CmRemoteAuthServerPort_Type()
)
cmRemoteAuthServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerPort.setStatus("current")
_CmRemoteAuthServerNumRetries_Type = Integer32
_CmRemoteAuthServerNumRetries_Object = MibTableColumn
cmRemoteAuthServerNumRetries = _CmRemoteAuthServerNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 6),
    _CmRemoteAuthServerNumRetries_Type()
)
cmRemoteAuthServerNumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerNumRetries.setStatus("current")
_CmRemoteAuthServerTimeout_Type = Integer32
_CmRemoteAuthServerTimeout_Object = MibTableColumn
cmRemoteAuthServerTimeout = _CmRemoteAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 7),
    _CmRemoteAuthServerTimeout_Type()
)
cmRemoteAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerTimeout.setStatus("current")


class _CmRemoteAuthServerSecret_Type(DisplayString):
    """Custom type cmRemoteAuthServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CmRemoteAuthServerSecret_Type.__name__ = "DisplayString"
_CmRemoteAuthServerSecret_Object = MibTableColumn
cmRemoteAuthServerSecret = _CmRemoteAuthServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 8),
    _CmRemoteAuthServerSecret_Type()
)
cmRemoteAuthServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerSecret.setStatus("current")
_CmRemoteAuthServerAccountingPort_Type = Integer32
_CmRemoteAuthServerAccountingPort_Object = MibTableColumn
cmRemoteAuthServerAccountingPort = _CmRemoteAuthServerAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 9),
    _CmRemoteAuthServerAccountingPort_Type()
)
cmRemoteAuthServerAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerAccountingPort.setStatus("current")
_CmRemoteAuthServerIpVersion_Type = IpVersion
_CmRemoteAuthServerIpVersion_Object = MibTableColumn
cmRemoteAuthServerIpVersion = _CmRemoteAuthServerIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 10),
    _CmRemoteAuthServerIpVersion_Type()
)
cmRemoteAuthServerIpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerIpVersion.setStatus("current")
_CmRemoteAuthServerIpv6Addr_Type = Ipv6Address
_CmRemoteAuthServerIpv6Addr_Object = MibTableColumn
cmRemoteAuthServerIpv6Addr = _CmRemoteAuthServerIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 6, 1, 11),
    _CmRemoteAuthServerIpv6Addr_Type()
)
cmRemoteAuthServerIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerIpv6Addr.setStatus("current")
_CmSecurityPolicyStrength_Type = CmSecurityPolicyStrength
_CmSecurityPolicyStrength_Object = MibScalar
cmSecurityPolicyStrength = _CmSecurityPolicyStrength_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 7),
    _CmSecurityPolicyStrength_Type()
)
cmSecurityPolicyStrength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmSecurityPolicyStrength.setStatus("current")
_CmRemoteAuthServerAccountingEnabled_Type = TruthValue
_CmRemoteAuthServerAccountingEnabled_Object = MibScalar
cmRemoteAuthServerAccountingEnabled = _CmRemoteAuthServerAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 8),
    _CmRemoteAuthServerAccountingEnabled_Type()
)
cmRemoteAuthServerAccountingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmRemoteAuthServerAccountingEnabled.setStatus("current")
_F3UsmUserTable_Object = MibTable
f3UsmUserTable = _F3UsmUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 9)
)
if mibBuilder.loadTexts:
    f3UsmUserTable.setStatus("current")
_F3UsmUserEntry_Object = MibTableRow
f3UsmUserEntry = _F3UsmUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 9, 1)
)
if mibBuilder.loadTexts:
    f3UsmUserEntry.setStatus("current")
_F3UsmUserAccessType_Type = UsmUserAccessType
_F3UsmUserAccessType_Object = MibTableColumn
f3UsmUserAccessType = _F3UsmUserAccessType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 9, 1, 1),
    _F3UsmUserAccessType_Type()
)
f3UsmUserAccessType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3UsmUserAccessType.setStatus("current")
_F3TacacsPrivLevelControlEnabled_Type = TruthValue
_F3TacacsPrivLevelControlEnabled_Object = MibScalar
f3TacacsPrivLevelControlEnabled = _F3TacacsPrivLevelControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 10),
    _F3TacacsPrivLevelControlEnabled_Type()
)
f3TacacsPrivLevelControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TacacsPrivLevelControlEnabled.setStatus("current")
_F3TacacsDefaultPrivLevel_Type = CmSecurityPrivLevel
_F3TacacsDefaultPrivLevel_Object = MibScalar
f3TacacsDefaultPrivLevel = _F3TacacsDefaultPrivLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 11),
    _F3TacacsDefaultPrivLevel_Type()
)
f3TacacsDefaultPrivLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3TacacsDefaultPrivLevel.setStatus("current")
_F3NasIpv6Addr_Type = Ipv6Address
_F3NasIpv6Addr_Object = MibScalar
f3NasIpv6Addr = _F3NasIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 12),
    _F3NasIpv6Addr_Type()
)
f3NasIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NasIpv6Addr.setStatus("current")
_F3SecurityTrapType_Type = SnmpSecurityTrapType
_F3SecurityTrapType_Object = MibScalar
f3SecurityTrapType = _F3SecurityTrapType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 13),
    _F3SecurityTrapType_Type()
)
f3SecurityTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3SecurityTrapType.setStatus("current")
_F3SecurityTrapInfo_Type = DisplayString
_F3SecurityTrapInfo_Object = MibScalar
f3SecurityTrapInfo = _F3SecurityTrapInfo_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 14),
    _F3SecurityTrapInfo_Type()
)
f3SecurityTrapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3SecurityTrapInfo.setStatus("current")
_F3PrivilegeChangeTable_Object = MibTable
f3PrivilegeChangeTable = _F3PrivilegeChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15)
)
if mibBuilder.loadTexts:
    f3PrivilegeChangeTable.setStatus("current")
_F3PrivilegeChangeEntry_Object = MibTableRow
f3PrivilegeChangeEntry = _F3PrivilegeChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1)
)
f3PrivilegeChangeEntry.setIndexNames(
    (0, "CM-SECURITY-MIB", "f3PrivilegeChangeId"),
)
if mibBuilder.loadTexts:
    f3PrivilegeChangeEntry.setStatus("current")


class _F3PrivilegeChangeId_Type(Unsigned32):
    """Custom type f3PrivilegeChangeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_F3PrivilegeChangeId_Type.__name__ = "Unsigned32"
_F3PrivilegeChangeId_Object = MibTableColumn
f3PrivilegeChangeId = _F3PrivilegeChangeId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 1),
    _F3PrivilegeChangeId_Type()
)
f3PrivilegeChangeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3PrivilegeChangeId.setStatus("current")
_F3PrivilegeChangeUserName_Type = SnmpAdminString
_F3PrivilegeChangeUserName_Object = MibTableColumn
f3PrivilegeChangeUserName = _F3PrivilegeChangeUserName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 2),
    _F3PrivilegeChangeUserName_Type()
)
f3PrivilegeChangeUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeUserName.setStatus("current")
_F3PrivilegeChangeIpv4Address_Type = IpAddress
_F3PrivilegeChangeIpv4Address_Object = MibTableColumn
f3PrivilegeChangeIpv4Address = _F3PrivilegeChangeIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 3),
    _F3PrivilegeChangeIpv4Address_Type()
)
f3PrivilegeChangeIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeIpv4Address.setStatus("current")
_F3PrivilegeChangeIpv6Address_Type = Ipv6Address
_F3PrivilegeChangeIpv6Address_Object = MibTableColumn
f3PrivilegeChangeIpv6Address = _F3PrivilegeChangeIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 4),
    _F3PrivilegeChangeIpv6Address_Type()
)
f3PrivilegeChangeIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeIpv6Address.setStatus("current")
_F3PrivilegeChangeTerminalIpv4Address_Type = IpAddress
_F3PrivilegeChangeTerminalIpv4Address_Object = MibTableColumn
f3PrivilegeChangeTerminalIpv4Address = _F3PrivilegeChangeTerminalIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 5),
    _F3PrivilegeChangeTerminalIpv4Address_Type()
)
f3PrivilegeChangeTerminalIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeTerminalIpv4Address.setStatus("current")
_F3PrivilegeChangeTerminalIpv6Address_Type = Ipv6Address
_F3PrivilegeChangeTerminalIpv6Address_Object = MibTableColumn
f3PrivilegeChangeTerminalIpv6Address = _F3PrivilegeChangeTerminalIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 6),
    _F3PrivilegeChangeTerminalIpv6Address_Type()
)
f3PrivilegeChangeTerminalIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeTerminalIpv6Address.setStatus("current")
_F3PrivilegeChangeInterface_Type = UserInterfaceType
_F3PrivilegeChangeInterface_Object = MibTableColumn
f3PrivilegeChangeInterface = _F3PrivilegeChangeInterface_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 7),
    _F3PrivilegeChangeInterface_Type()
)
f3PrivilegeChangeInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeInterface.setStatus("current")
_F3PrivilegeChangeCurrentPrivilege_Type = CmSecurityPrivLevel
_F3PrivilegeChangeCurrentPrivilege_Object = MibTableColumn
f3PrivilegeChangeCurrentPrivilege = _F3PrivilegeChangeCurrentPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 8),
    _F3PrivilegeChangeCurrentPrivilege_Type()
)
f3PrivilegeChangeCurrentPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeCurrentPrivilege.setStatus("current")
_F3PrivilegeChangeRequestedPrivilege_Type = CmSecurityPrivLevel
_F3PrivilegeChangeRequestedPrivilege_Object = MibTableColumn
f3PrivilegeChangeRequestedPrivilege = _F3PrivilegeChangeRequestedPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 9),
    _F3PrivilegeChangeRequestedPrivilege_Type()
)
f3PrivilegeChangeRequestedPrivilege.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeRequestedPrivilege.setStatus("current")


class _F3PrivilegeChangeDuration_Type(Unsigned32):
    """Custom type f3PrivilegeChangeDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 480),
    )


_F3PrivilegeChangeDuration_Type.__name__ = "Unsigned32"
_F3PrivilegeChangeDuration_Object = MibTableColumn
f3PrivilegeChangeDuration = _F3PrivilegeChangeDuration_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 10),
    _F3PrivilegeChangeDuration_Type()
)
f3PrivilegeChangeDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeDuration.setStatus("current")
if mibBuilder.loadTexts:
    f3PrivilegeChangeDuration.setUnits("minutes")
_F3PrivilegeChangeAction_Type = PrivilegeRequestAction
_F3PrivilegeChangeAction_Object = MibTableColumn
f3PrivilegeChangeAction = _F3PrivilegeChangeAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 11),
    _F3PrivilegeChangeAction_Type()
)
f3PrivilegeChangeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3PrivilegeChangeAction.setStatus("current")
_F3PrivilegeChangeState_Type = PrivilegeRequestState
_F3PrivilegeChangeState_Object = MibTableColumn
f3PrivilegeChangeState = _F3PrivilegeChangeState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 12),
    _F3PrivilegeChangeState_Type()
)
f3PrivilegeChangeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeState.setStatus("current")
_F3PrivilegeChangeRemainingTime_Type = Unsigned32
_F3PrivilegeChangeRemainingTime_Object = MibTableColumn
f3PrivilegeChangeRemainingTime = _F3PrivilegeChangeRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 13),
    _F3PrivilegeChangeRemainingTime_Type()
)
f3PrivilegeChangeRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    f3PrivilegeChangeRemainingTime.setUnits("seconds")
_F3PrivilegeChangeRemoteName_Type = SnmpAdminString
_F3PrivilegeChangeRemoteName_Object = MibTableColumn
f3PrivilegeChangeRemoteName = _F3PrivilegeChangeRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 15, 1, 14),
    _F3PrivilegeChangeRemoteName_Type()
)
f3PrivilegeChangeRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3PrivilegeChangeRemoteName.setStatus("current")
_F3UserPrivMgmtControl_Type = TruthValue
_F3UserPrivMgmtControl_Object = MibScalar
f3UserPrivMgmtControl = _F3UserPrivMgmtControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 16),
    _F3UserPrivMgmtControl_Type()
)
f3UserPrivMgmtControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3UserPrivMgmtControl.setStatus("current")


class _F3UserPrivRspTimeout_Type(Integer32):
    """Custom type f3UserPrivRspTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_F3UserPrivRspTimeout_Type.__name__ = "Integer32"
_F3UserPrivRspTimeout_Object = MibScalar
f3UserPrivRspTimeout = _F3UserPrivRspTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 1, 17),
    _F3UserPrivRspTimeout_Type()
)
f3UserPrivRspTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3UserPrivRspTimeout.setStatus("current")
if mibBuilder.loadTexts:
    f3UserPrivRspTimeout.setUnits("minutes")
_CmSecurityConformance_ObjectIdentity = ObjectIdentity
cmSecurityConformance = _CmSecurityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2)
)
_CmSecurityCompliances_ObjectIdentity = ObjectIdentity
cmSecurityCompliances = _CmSecurityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2, 1)
)
_CmSecurityGroups_ObjectIdentity = ObjectIdentity
cmSecurityGroups = _CmSecurityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2, 2)
)
_CmSecurityNotifications_ObjectIdentity = ObjectIdentity
cmSecurityNotifications = _CmSecurityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 3)
)
usmUserEntry.registerAugmentions(
    ("CM-SECURITY-MIB",
     "f3UsmUserEntry")
)
f3UsmUserEntry.setIndexNames(*usmUserEntry.getIndexNames())

# Managed Objects groups

cmSecurityObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2, 2, 1)
)
cmSecurityObjectGroup.setObjects(
      *(("CM-SECURITY-MIB", "cmAuthProtocol"),
        ("CM-SECURITY-MIB", "cmAccessOrder"),
        ("CM-SECURITY-MIB", "cmAuthType"),
        ("CM-SECURITY-MIB", "cmNASIpAddress"),
        ("CM-SECURITY-MIB", "cmSecurityPolicyStrength"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerAccountingEnabled"),
        ("CM-SECURITY-MIB", "f3TacacsPrivLevelControlEnabled"),
        ("CM-SECURITY-MIB", "f3TacacsDefaultPrivLevel"),
        ("CM-SECURITY-MIB", "f3NasIpv6Addr"),
        ("CM-SECURITY-MIB", "f3SecurityTrapType"),
        ("CM-SECURITY-MIB", "f3SecurityTrapInfo"),
        ("CM-SECURITY-MIB", "cmSecurityUserName"),
        ("CM-SECURITY-MIB", "cmSecurityUserComment"),
        ("CM-SECURITY-MIB", "cmSecurityUserPrivLevel"),
        ("CM-SECURITY-MIB", "cmSecurityUserLoginTimeout"),
        ("CM-SECURITY-MIB", "cmSecurityUserNumFailedLoginAttempts"),
        ("CM-SECURITY-MIB", "cmSecurityUserLastLoginTime"),
        ("CM-SECURITY-MIB", "cmSecurityUserLockedout"),
        ("CM-SECURITY-MIB", "cmSecurityUserLastLockedoutTime"),
        ("CM-SECURITY-MIB", "cmSecurityUserCliPagingEnable"),
        ("CM-SECURITY-MIB", "cmSecurityUserRemoteUser"),
        ("CM-SECURITY-MIB", "cmSecurityUserPassword"),
        ("CM-SECURITY-MIB", "cmSecurityUserStorageType"),
        ("CM-SECURITY-MIB", "cmSecurityUserRowStatus"),
        ("CM-SECURITY-MIB", "cmSecurityUserAction"),
        ("CM-SECURITY-MIB", "cmSecurityCryptoPassword"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerIndex"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerEnabled"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerOrder"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerIpAddress"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerPort"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerNumRetries"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerTimeout"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerSecret"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerAccountingPort"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerIpVersion"),
        ("CM-SECURITY-MIB", "cmRemoteAuthServerIpv6Addr"),
        ("CM-SECURITY-MIB", "f3UsmUserAccessType"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeUserName"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeIpv4Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeIpv6Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeTerminalIpv4Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeTerminalIpv6Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeInterface"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeCurrentPrivilege"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeRequestedPrivilege"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeDuration"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeAction"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeState"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeRemainingTime"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeRemoteName"))
)
if mibBuilder.loadTexts:
    cmSecurityObjectGroup.setStatus("current")


# Notification objects

f3SecurityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 3, 1)
)
if mibBuilder.loadTexts:
    f3SecurityTrap.setStatus(
        "current"
    )

f3PrivilegeChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 3, 2)
)
f3PrivilegeChangeTrap.setObjects(
      *(("CM-SECURITY-MIB", "f3PrivilegeChangeState"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeUserName"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeIpv4Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeIpv6Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeTerminalIpv4Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeTerminalIpv6Address"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeInterface"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeCurrentPrivilege"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeRequestedPrivilege"),
        ("CM-SECURITY-MIB", "f3PrivilegeChangeDuration"))
)
if mibBuilder.loadTexts:
    f3PrivilegeChangeTrap.setStatus(
        "current"
    )


# Notifications groups

cmSecurityNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2, 2, 2)
)
cmSecurityNotifGroup.setObjects(
    ("CM-SECURITY-MIB", "f3SecurityTrap")
)
if mibBuilder.loadTexts:
    cmSecurityNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cmSecurityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 10, 2, 1, 1)
)
cmSecurityCompliance.setObjects(
    ("CM-SECURITY-MIB", "cmSecurityObjectGroup")
)
if mibBuilder.loadTexts:
    cmSecurityCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CM-SECURITY-MIB",
    **{"CmRemoteAuthProtocol": CmRemoteAuthProtocol,
       "CmSecurityAccessOrder": CmSecurityAccessOrder,
       "CmSecurityAuthType": CmSecurityAuthType,
       "CmSecurityPrivLevel": CmSecurityPrivLevel,
       "CmRemoteAuthOrder": CmRemoteAuthOrder,
       "CmSecurityPolicyStrength": CmSecurityPolicyStrength,
       "UsmUserAccessType": UsmUserAccessType,
       "SecurityUserAction": SecurityUserAction,
       "SnmpSecurityTrapType": SnmpSecurityTrapType,
       "PrivilegeRequestAction": PrivilegeRequestAction,
       "PrivilegeRequestState": PrivilegeRequestState,
       "cmSecurityMIB": cmSecurityMIB,
       "cmSecurityObjects": cmSecurityObjects,
       "cmAuthProtocol": cmAuthProtocol,
       "cmAccessOrder": cmAccessOrder,
       "cmAuthType": cmAuthType,
       "cmNASIpAddress": cmNASIpAddress,
       "cmSecurityUserTable": cmSecurityUserTable,
       "cmSecurityUserEntry": cmSecurityUserEntry,
       "cmSecurityUserName": cmSecurityUserName,
       "cmSecurityUserComment": cmSecurityUserComment,
       "cmSecurityUserPrivLevel": cmSecurityUserPrivLevel,
       "cmSecurityUserLoginTimeout": cmSecurityUserLoginTimeout,
       "cmSecurityUserNumFailedLoginAttempts": cmSecurityUserNumFailedLoginAttempts,
       "cmSecurityUserLastLoginTime": cmSecurityUserLastLoginTime,
       "cmSecurityUserLockedout": cmSecurityUserLockedout,
       "cmSecurityUserLastLockedoutTime": cmSecurityUserLastLockedoutTime,
       "cmSecurityUserCliPagingEnable": cmSecurityUserCliPagingEnable,
       "cmSecurityUserRemoteUser": cmSecurityUserRemoteUser,
       "cmSecurityUserPassword": cmSecurityUserPassword,
       "cmSecurityUserStorageType": cmSecurityUserStorageType,
       "cmSecurityUserRowStatus": cmSecurityUserRowStatus,
       "cmSecurityUserAction": cmSecurityUserAction,
       "cmSecurityCryptoPassword": cmSecurityCryptoPassword,
       "cmSecurityUserRemoteCryptoUser": cmSecurityUserRemoteCryptoUser,
       "cmRemoteAuthServerTable": cmRemoteAuthServerTable,
       "cmRemoteAuthServerEntry": cmRemoteAuthServerEntry,
       "cmRemoteAuthServerIndex": cmRemoteAuthServerIndex,
       "cmRemoteAuthServerEnabled": cmRemoteAuthServerEnabled,
       "cmRemoteAuthServerOrder": cmRemoteAuthServerOrder,
       "cmRemoteAuthServerIpAddress": cmRemoteAuthServerIpAddress,
       "cmRemoteAuthServerPort": cmRemoteAuthServerPort,
       "cmRemoteAuthServerNumRetries": cmRemoteAuthServerNumRetries,
       "cmRemoteAuthServerTimeout": cmRemoteAuthServerTimeout,
       "cmRemoteAuthServerSecret": cmRemoteAuthServerSecret,
       "cmRemoteAuthServerAccountingPort": cmRemoteAuthServerAccountingPort,
       "cmRemoteAuthServerIpVersion": cmRemoteAuthServerIpVersion,
       "cmRemoteAuthServerIpv6Addr": cmRemoteAuthServerIpv6Addr,
       "cmSecurityPolicyStrength": cmSecurityPolicyStrength,
       "cmRemoteAuthServerAccountingEnabled": cmRemoteAuthServerAccountingEnabled,
       "f3UsmUserTable": f3UsmUserTable,
       "f3UsmUserEntry": f3UsmUserEntry,
       "f3UsmUserAccessType": f3UsmUserAccessType,
       "f3TacacsPrivLevelControlEnabled": f3TacacsPrivLevelControlEnabled,
       "f3TacacsDefaultPrivLevel": f3TacacsDefaultPrivLevel,
       "f3NasIpv6Addr": f3NasIpv6Addr,
       "f3SecurityTrapType": f3SecurityTrapType,
       "f3SecurityTrapInfo": f3SecurityTrapInfo,
       "f3PrivilegeChangeTable": f3PrivilegeChangeTable,
       "f3PrivilegeChangeEntry": f3PrivilegeChangeEntry,
       "f3PrivilegeChangeId": f3PrivilegeChangeId,
       "f3PrivilegeChangeUserName": f3PrivilegeChangeUserName,
       "f3PrivilegeChangeIpv4Address": f3PrivilegeChangeIpv4Address,
       "f3PrivilegeChangeIpv6Address": f3PrivilegeChangeIpv6Address,
       "f3PrivilegeChangeTerminalIpv4Address": f3PrivilegeChangeTerminalIpv4Address,
       "f3PrivilegeChangeTerminalIpv6Address": f3PrivilegeChangeTerminalIpv6Address,
       "f3PrivilegeChangeInterface": f3PrivilegeChangeInterface,
       "f3PrivilegeChangeCurrentPrivilege": f3PrivilegeChangeCurrentPrivilege,
       "f3PrivilegeChangeRequestedPrivilege": f3PrivilegeChangeRequestedPrivilege,
       "f3PrivilegeChangeDuration": f3PrivilegeChangeDuration,
       "f3PrivilegeChangeAction": f3PrivilegeChangeAction,
       "f3PrivilegeChangeState": f3PrivilegeChangeState,
       "f3PrivilegeChangeRemainingTime": f3PrivilegeChangeRemainingTime,
       "f3PrivilegeChangeRemoteName": f3PrivilegeChangeRemoteName,
       "f3UserPrivMgmtControl": f3UserPrivMgmtControl,
       "f3UserPrivRspTimeout": f3UserPrivRspTimeout,
       "cmSecurityConformance": cmSecurityConformance,
       "cmSecurityCompliances": cmSecurityCompliances,
       "cmSecurityCompliance": cmSecurityCompliance,
       "cmSecurityGroups": cmSecurityGroups,
       "cmSecurityObjectGroup": cmSecurityObjectGroup,
       "cmSecurityNotifGroup": cmSecurityNotifGroup,
       "cmSecurityNotifications": cmSecurityNotifications,
       "f3SecurityTrap": f3SecurityTrap,
       "f3PrivilegeChangeTrap": f3PrivilegeChangeTrap}
)
