# SNMP MIB module (VRRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/VRRP-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:44:02 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

vrrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 68)
)
if mibBuilder.loadTexts:
    vrrpMIB.setRevisions(
        ("2000-03-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VrId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_VrrpNotifications_ObjectIdentity = ObjectIdentity
vrrpNotifications = _VrrpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 0)
)
_VrrpOperations_ObjectIdentity = ObjectIdentity
vrrpOperations = _VrrpOperations_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 1)
)
_VrrpNodeVersion_Type = Integer32
_VrrpNodeVersion_Object = MibScalar
vrrpNodeVersion = _VrrpNodeVersion_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 1),
    _VrrpNodeVersion_Type()
)
vrrpNodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpNodeVersion.setStatus("current")


class _VrrpNotificationCntl_Type(Integer32):
    """Custom type vrrpNotificationCntl based on Integer32"""
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


_VrrpNotificationCntl_Type.__name__ = "Integer32"
_VrrpNotificationCntl_Object = MibScalar
vrrpNotificationCntl = _VrrpNotificationCntl_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 2),
    _VrrpNotificationCntl_Type()
)
vrrpNotificationCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpNotificationCntl.setStatus("current")
_VrrpOperTable_Object = MibTable
vrrpOperTable = _VrrpOperTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3)
)
if mibBuilder.loadTexts:
    vrrpOperTable.setStatus("current")
_VrrpOperEntry_Object = MibTableRow
vrrpOperEntry = _VrrpOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1)
)
vrrpOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
)
if mibBuilder.loadTexts:
    vrrpOperEntry.setStatus("current")
_VrrpOperVrId_Type = VrId
_VrrpOperVrId_Object = MibTableColumn
vrrpOperVrId = _VrrpOperVrId_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 1),
    _VrrpOperVrId_Type()
)
vrrpOperVrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpOperVrId.setStatus("current")
_VrrpOperVirtualMacAddr_Type = MacAddress
_VrrpOperVirtualMacAddr_Object = MibTableColumn
vrrpOperVirtualMacAddr = _VrrpOperVirtualMacAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 2),
    _VrrpOperVirtualMacAddr_Type()
)
vrrpOperVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperVirtualMacAddr.setStatus("current")


class _VrrpOperState_Type(Integer32):
    """Custom type vrrpOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("initialize", 1),
          ("backup", 2),
          ("master", 3))
    )


_VrrpOperState_Type.__name__ = "Integer32"
_VrrpOperState_Object = MibTableColumn
vrrpOperState = _VrrpOperState_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 3),
    _VrrpOperState_Type()
)
vrrpOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperState.setStatus("current")


class _VrrpOperAdminState_Type(Integer32):
    """Custom type vrrpOperAdminState based on Integer32"""
    defaultValue = 2

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


_VrrpOperAdminState_Type.__name__ = "Integer32"
_VrrpOperAdminState_Object = MibTableColumn
vrrpOperAdminState = _VrrpOperAdminState_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 4),
    _VrrpOperAdminState_Type()
)
vrrpOperAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperAdminState.setStatus("current")


class _VrrpOperPriority_Type(Integer32):
    """Custom type vrrpOperPriority based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrrpOperPriority_Type.__name__ = "Integer32"
_VrrpOperPriority_Object = MibTableColumn
vrrpOperPriority = _VrrpOperPriority_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 5),
    _VrrpOperPriority_Type()
)
vrrpOperPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperPriority.setStatus("current")


class _VrrpOperIpAddrCount_Type(Integer32):
    """Custom type vrrpOperIpAddrCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrrpOperIpAddrCount_Type.__name__ = "Integer32"
_VrrpOperIpAddrCount_Object = MibTableColumn
vrrpOperIpAddrCount = _VrrpOperIpAddrCount_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 6),
    _VrrpOperIpAddrCount_Type()
)
vrrpOperIpAddrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperIpAddrCount.setStatus("current")
_VrrpOperMasterIpAddr_Type = IpAddress
_VrrpOperMasterIpAddr_Object = MibTableColumn
vrrpOperMasterIpAddr = _VrrpOperMasterIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 7),
    _VrrpOperMasterIpAddr_Type()
)
vrrpOperMasterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperMasterIpAddr.setStatus("current")


class _VrrpOperPrimaryIpAddr_Type(IpAddress):
    """Custom type vrrpOperPrimaryIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_VrrpOperPrimaryIpAddr_Type.__name__ = "IpAddress"
_VrrpOperPrimaryIpAddr_Object = MibTableColumn
vrrpOperPrimaryIpAddr = _VrrpOperPrimaryIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 8),
    _VrrpOperPrimaryIpAddr_Type()
)
vrrpOperPrimaryIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperPrimaryIpAddr.setStatus("current")


class _VrrpOperAuthType_Type(Integer32):
    """Custom type vrrpOperAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthentication", 1),
          ("simpleTextPassword", 2),
          ("ipAuthenticationHeader", 3))
    )


_VrrpOperAuthType_Type.__name__ = "Integer32"
_VrrpOperAuthType_Object = MibTableColumn
vrrpOperAuthType = _VrrpOperAuthType_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 9),
    _VrrpOperAuthType_Type()
)
vrrpOperAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperAuthType.setStatus("current")


class _VrrpOperAuthKey_Type(OctetString):
    """Custom type vrrpOperAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VrrpOperAuthKey_Type.__name__ = "OctetString"
_VrrpOperAuthKey_Object = MibTableColumn
vrrpOperAuthKey = _VrrpOperAuthKey_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 10),
    _VrrpOperAuthKey_Type()
)
vrrpOperAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperAuthKey.setStatus("current")


class _VrrpOperAdvertisementInterval_Type(Integer32):
    """Custom type vrrpOperAdvertisementInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VrrpOperAdvertisementInterval_Type.__name__ = "Integer32"
_VrrpOperAdvertisementInterval_Object = MibTableColumn
vrrpOperAdvertisementInterval = _VrrpOperAdvertisementInterval_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 11),
    _VrrpOperAdvertisementInterval_Type()
)
vrrpOperAdvertisementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    vrrpOperAdvertisementInterval.setUnits("seconds")


class _VrrpOperPreemptMode_Type(TruthValue):
    """Custom type vrrpOperPreemptMode based on TruthValue"""
    defaultValue = 1


_VrrpOperPreemptMode_Type.__name__ = "TruthValue"
_VrrpOperPreemptMode_Object = MibTableColumn
vrrpOperPreemptMode = _VrrpOperPreemptMode_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 12),
    _VrrpOperPreemptMode_Type()
)
vrrpOperPreemptMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperPreemptMode.setStatus("current")
_VrrpOperVirtualRouterUpTime_Type = TimeStamp
_VrrpOperVirtualRouterUpTime_Object = MibTableColumn
vrrpOperVirtualRouterUpTime = _VrrpOperVirtualRouterUpTime_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 13),
    _VrrpOperVirtualRouterUpTime_Type()
)
vrrpOperVirtualRouterUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpOperVirtualRouterUpTime.setStatus("current")


class _VrrpOperProtocol_Type(Integer32):
    """Custom type vrrpOperProtocol based on Integer32"""
    defaultValue = 1

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
        *(("ip", 1),
          ("bridge", 2),
          ("decnet", 3),
          ("other", 4))
    )


_VrrpOperProtocol_Type.__name__ = "Integer32"
_VrrpOperProtocol_Object = MibTableColumn
vrrpOperProtocol = _VrrpOperProtocol_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 14),
    _VrrpOperProtocol_Type()
)
vrrpOperProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperProtocol.setStatus("current")
_VrrpOperRowStatus_Type = RowStatus
_VrrpOperRowStatus_Object = MibTableColumn
vrrpOperRowStatus = _VrrpOperRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 3, 1, 15),
    _VrrpOperRowStatus_Type()
)
vrrpOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpOperRowStatus.setStatus("current")
_VrrpAssoIpAddrTable_Object = MibTable
vrrpAssoIpAddrTable = _VrrpAssoIpAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 4)
)
if mibBuilder.loadTexts:
    vrrpAssoIpAddrTable.setStatus("current")
_VrrpAssoIpAddrEntry_Object = MibTableRow
vrrpAssoIpAddrEntry = _VrrpAssoIpAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 4, 1)
)
vrrpAssoIpAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VRRP-MIB", "vrrpOperVrId"),
    (0, "VRRP-MIB", "vrrpAssoIpAddr"),
)
if mibBuilder.loadTexts:
    vrrpAssoIpAddrEntry.setStatus("current")
_VrrpAssoIpAddr_Type = IpAddress
_VrrpAssoIpAddr_Object = MibTableColumn
vrrpAssoIpAddr = _VrrpAssoIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 1),
    _VrrpAssoIpAddr_Type()
)
vrrpAssoIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpAssoIpAddr.setStatus("current")
_VrrpAssoIpAddrRowStatus_Type = RowStatus
_VrrpAssoIpAddrRowStatus_Object = MibTableColumn
vrrpAssoIpAddrRowStatus = _VrrpAssoIpAddrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 4, 1, 2),
    _VrrpAssoIpAddrRowStatus_Type()
)
vrrpAssoIpAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vrrpAssoIpAddrRowStatus.setStatus("current")
_VrrpTrapPacketSrc_Type = IpAddress
_VrrpTrapPacketSrc_Object = MibScalar
vrrpTrapPacketSrc = _VrrpTrapPacketSrc_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 5),
    _VrrpTrapPacketSrc_Type()
)
vrrpTrapPacketSrc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vrrpTrapPacketSrc.setStatus("current")


class _VrrpTrapAuthErrorType_Type(Integer32):
    """Custom type vrrpTrapAuthErrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalidAuthType", 1),
          ("authTypeMismatch", 2),
          ("authFailure", 3))
    )


_VrrpTrapAuthErrorType_Type.__name__ = "Integer32"
_VrrpTrapAuthErrorType_Object = MibScalar
vrrpTrapAuthErrorType = _VrrpTrapAuthErrorType_Object(
    (1, 3, 6, 1, 2, 1, 68, 1, 6),
    _VrrpTrapAuthErrorType_Type()
)
vrrpTrapAuthErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vrrpTrapAuthErrorType.setStatus("current")
_VrrpStatistics_ObjectIdentity = ObjectIdentity
vrrpStatistics = _VrrpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 2)
)
_VrrpRouterChecksumErrors_Type = Counter32
_VrrpRouterChecksumErrors_Object = MibScalar
vrrpRouterChecksumErrors = _VrrpRouterChecksumErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 1),
    _VrrpRouterChecksumErrors_Type()
)
vrrpRouterChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouterChecksumErrors.setStatus("current")
_VrrpRouterVersionErrors_Type = Counter32
_VrrpRouterVersionErrors_Object = MibScalar
vrrpRouterVersionErrors = _VrrpRouterVersionErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 2),
    _VrrpRouterVersionErrors_Type()
)
vrrpRouterVersionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouterVersionErrors.setStatus("current")
_VrrpRouterVrIdErrors_Type = Counter32
_VrrpRouterVrIdErrors_Object = MibScalar
vrrpRouterVrIdErrors = _VrrpRouterVrIdErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 3),
    _VrrpRouterVrIdErrors_Type()
)
vrrpRouterVrIdErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouterVrIdErrors.setStatus("current")
_VrrpRouterStatsTable_Object = MibTable
vrrpRouterStatsTable = _VrrpRouterStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4)
)
if mibBuilder.loadTexts:
    vrrpRouterStatsTable.setStatus("current")
_VrrpRouterStatsEntry_Object = MibTableRow
vrrpRouterStatsEntry = _VrrpRouterStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1)
)
if mibBuilder.loadTexts:
    vrrpRouterStatsEntry.setStatus("current")
_VrrpStatsBecomeMaster_Type = Counter32
_VrrpStatsBecomeMaster_Object = MibTableColumn
vrrpStatsBecomeMaster = _VrrpStatsBecomeMaster_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 1),
    _VrrpStatsBecomeMaster_Type()
)
vrrpStatsBecomeMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsBecomeMaster.setStatus("current")
_VrrpStatsAdvertiseRcvd_Type = Counter32
_VrrpStatsAdvertiseRcvd_Object = MibTableColumn
vrrpStatsAdvertiseRcvd = _VrrpStatsAdvertiseRcvd_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 2),
    _VrrpStatsAdvertiseRcvd_Type()
)
vrrpStatsAdvertiseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsAdvertiseRcvd.setStatus("current")
_VrrpStatsAdvertiseIntervalErrors_Type = Counter32
_VrrpStatsAdvertiseIntervalErrors_Object = MibTableColumn
vrrpStatsAdvertiseIntervalErrors = _VrrpStatsAdvertiseIntervalErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 3),
    _VrrpStatsAdvertiseIntervalErrors_Type()
)
vrrpStatsAdvertiseIntervalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsAdvertiseIntervalErrors.setStatus("current")
_VrrpStatsAuthFailures_Type = Counter32
_VrrpStatsAuthFailures_Object = MibTableColumn
vrrpStatsAuthFailures = _VrrpStatsAuthFailures_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 4),
    _VrrpStatsAuthFailures_Type()
)
vrrpStatsAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsAuthFailures.setStatus("current")
_VrrpStatsIpTtlErrors_Type = Counter32
_VrrpStatsIpTtlErrors_Object = MibTableColumn
vrrpStatsIpTtlErrors = _VrrpStatsIpTtlErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 5),
    _VrrpStatsIpTtlErrors_Type()
)
vrrpStatsIpTtlErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsIpTtlErrors.setStatus("current")
_VrrpStatsPriorityZeroPktsRcvd_Type = Counter32
_VrrpStatsPriorityZeroPktsRcvd_Object = MibTableColumn
vrrpStatsPriorityZeroPktsRcvd = _VrrpStatsPriorityZeroPktsRcvd_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 6),
    _VrrpStatsPriorityZeroPktsRcvd_Type()
)
vrrpStatsPriorityZeroPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsPriorityZeroPktsRcvd.setStatus("current")
_VrrpStatsPriorityZeroPktsSent_Type = Counter32
_VrrpStatsPriorityZeroPktsSent_Object = MibTableColumn
vrrpStatsPriorityZeroPktsSent = _VrrpStatsPriorityZeroPktsSent_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 7),
    _VrrpStatsPriorityZeroPktsSent_Type()
)
vrrpStatsPriorityZeroPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsPriorityZeroPktsSent.setStatus("current")
_VrrpStatsInvalidTypePktsRcvd_Type = Counter32
_VrrpStatsInvalidTypePktsRcvd_Object = MibTableColumn
vrrpStatsInvalidTypePktsRcvd = _VrrpStatsInvalidTypePktsRcvd_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 8),
    _VrrpStatsInvalidTypePktsRcvd_Type()
)
vrrpStatsInvalidTypePktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsInvalidTypePktsRcvd.setStatus("current")
_VrrpStatsAddressListErrors_Type = Counter32
_VrrpStatsAddressListErrors_Object = MibTableColumn
vrrpStatsAddressListErrors = _VrrpStatsAddressListErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 9),
    _VrrpStatsAddressListErrors_Type()
)
vrrpStatsAddressListErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsAddressListErrors.setStatus("current")
_VrrpStatsInvalidAuthType_Type = Counter32
_VrrpStatsInvalidAuthType_Object = MibTableColumn
vrrpStatsInvalidAuthType = _VrrpStatsInvalidAuthType_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 10),
    _VrrpStatsInvalidAuthType_Type()
)
vrrpStatsInvalidAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsInvalidAuthType.setStatus("current")
_VrrpStatsAuthTypeMismatch_Type = Counter32
_VrrpStatsAuthTypeMismatch_Object = MibTableColumn
vrrpStatsAuthTypeMismatch = _VrrpStatsAuthTypeMismatch_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 11),
    _VrrpStatsAuthTypeMismatch_Type()
)
vrrpStatsAuthTypeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsAuthTypeMismatch.setStatus("current")
_VrrpStatsPacketLengthErrors_Type = Counter32
_VrrpStatsPacketLengthErrors_Object = MibTableColumn
vrrpStatsPacketLengthErrors = _VrrpStatsPacketLengthErrors_Object(
    (1, 3, 6, 1, 2, 1, 68, 2, 4, 1, 12),
    _VrrpStatsPacketLengthErrors_Type()
)
vrrpStatsPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatsPacketLengthErrors.setStatus("current")
_VrrpConformance_ObjectIdentity = ObjectIdentity
vrrpConformance = _VrrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 3)
)
_VrrpMIBCompliances_ObjectIdentity = ObjectIdentity
vrrpMIBCompliances = _VrrpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 3, 1)
)
_VrrpMIBGroups_ObjectIdentity = ObjectIdentity
vrrpMIBGroups = _VrrpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 68, 3, 2)
)
vrrpOperEntry.registerAugmentions(
    ("VRRP-MIB",
     "vrrpRouterStatsEntry")
)
vrrpRouterStatsEntry.setIndexNames(*vrrpOperEntry.getIndexNames())

# Managed Objects groups

vrrpOperGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 1)
)
vrrpOperGroup.setObjects(
      *(("VRRP-MIB", "vrrpNodeVersion"),
        ("VRRP-MIB", "vrrpNotificationCntl"),
        ("VRRP-MIB", "vrrpOperVirtualMacAddr"),
        ("VRRP-MIB", "vrrpOperState"),
        ("VRRP-MIB", "vrrpOperAdminState"),
        ("VRRP-MIB", "vrrpOperPriority"),
        ("VRRP-MIB", "vrrpOperIpAddrCount"),
        ("VRRP-MIB", "vrrpOperMasterIpAddr"),
        ("VRRP-MIB", "vrrpOperPrimaryIpAddr"),
        ("VRRP-MIB", "vrrpOperAuthType"),
        ("VRRP-MIB", "vrrpOperAuthKey"),
        ("VRRP-MIB", "vrrpOperAdvertisementInterval"),
        ("VRRP-MIB", "vrrpOperPreemptMode"),
        ("VRRP-MIB", "vrrpOperVirtualRouterUpTime"),
        ("VRRP-MIB", "vrrpOperProtocol"),
        ("VRRP-MIB", "vrrpOperRowStatus"),
        ("VRRP-MIB", "vrrpAssoIpAddrRowStatus"))
)
if mibBuilder.loadTexts:
    vrrpOperGroup.setStatus("current")

vrrpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 2)
)
vrrpStatsGroup.setObjects(
      *(("VRRP-MIB", "vrrpRouterChecksumErrors"),
        ("VRRP-MIB", "vrrpRouterVersionErrors"),
        ("VRRP-MIB", "vrrpRouterVrIdErrors"),
        ("VRRP-MIB", "vrrpStatsBecomeMaster"),
        ("VRRP-MIB", "vrrpStatsAdvertiseRcvd"),
        ("VRRP-MIB", "vrrpStatsAdvertiseIntervalErrors"),
        ("VRRP-MIB", "vrrpStatsAuthFailures"),
        ("VRRP-MIB", "vrrpStatsIpTtlErrors"),
        ("VRRP-MIB", "vrrpStatsPriorityZeroPktsRcvd"),
        ("VRRP-MIB", "vrrpStatsPriorityZeroPktsSent"),
        ("VRRP-MIB", "vrrpStatsInvalidTypePktsRcvd"),
        ("VRRP-MIB", "vrrpStatsAddressListErrors"),
        ("VRRP-MIB", "vrrpStatsInvalidAuthType"),
        ("VRRP-MIB", "vrrpStatsAuthTypeMismatch"),
        ("VRRP-MIB", "vrrpStatsPacketLengthErrors"))
)
if mibBuilder.loadTexts:
    vrrpStatsGroup.setStatus("current")

vrrpTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 3)
)
vrrpTrapGroup.setObjects(
      *(("VRRP-MIB", "vrrpTrapPacketSrc"),
        ("VRRP-MIB", "vrrpTrapAuthErrorType"))
)
if mibBuilder.loadTexts:
    vrrpTrapGroup.setStatus("current")


# Notification objects

vrrpTrapNewMaster = NotificationType(
    (1, 3, 6, 1, 2, 1, 68, 0, 1)
)
vrrpTrapNewMaster.setObjects(
    ("VRRP-MIB", "vrrpOperMasterIpAddr")
)
if mibBuilder.loadTexts:
    vrrpTrapNewMaster.setStatus(
        "current"
    )

vrrpTrapAuthFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 68, 0, 2)
)
vrrpTrapAuthFailure.setObjects(
      *(("VRRP-MIB", "vrrpTrapPacketSrc"),
        ("VRRP-MIB", "vrrpTrapAuthErrorType"))
)
if mibBuilder.loadTexts:
    vrrpTrapAuthFailure.setStatus(
        "current"
    )


# Notifications groups

vrrpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 68, 3, 2, 4)
)
vrrpNotificationGroup.setObjects(
      *(("VRRP-MIB", "vrrpTrapNewMaster"),
        ("VRRP-MIB", "vrrpTrapAuthFailure"))
)
if mibBuilder.loadTexts:
    vrrpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vrrpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 68, 3, 1, 1)
)
vrrpMIBCompliance.setObjects(
      *(("VRRP-MIB", "vrrpOperGroup"),
        ("VRRP-MIB", "vrrpStatsGroup"))
)
if mibBuilder.loadTexts:
    vrrpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VRRP-MIB",
    **{"VrId": VrId,
       "vrrpMIB": vrrpMIB,
       "vrrpNotifications": vrrpNotifications,
       "vrrpTrapNewMaster": vrrpTrapNewMaster,
       "vrrpTrapAuthFailure": vrrpTrapAuthFailure,
       "vrrpOperations": vrrpOperations,
       "vrrpNodeVersion": vrrpNodeVersion,
       "vrrpNotificationCntl": vrrpNotificationCntl,
       "vrrpOperTable": vrrpOperTable,
       "vrrpOperEntry": vrrpOperEntry,
       "vrrpOperVrId": vrrpOperVrId,
       "vrrpOperVirtualMacAddr": vrrpOperVirtualMacAddr,
       "vrrpOperState": vrrpOperState,
       "vrrpOperAdminState": vrrpOperAdminState,
       "vrrpOperPriority": vrrpOperPriority,
       "vrrpOperIpAddrCount": vrrpOperIpAddrCount,
       "vrrpOperMasterIpAddr": vrrpOperMasterIpAddr,
       "vrrpOperPrimaryIpAddr": vrrpOperPrimaryIpAddr,
       "vrrpOperAuthType": vrrpOperAuthType,
       "vrrpOperAuthKey": vrrpOperAuthKey,
       "vrrpOperAdvertisementInterval": vrrpOperAdvertisementInterval,
       "vrrpOperPreemptMode": vrrpOperPreemptMode,
       "vrrpOperVirtualRouterUpTime": vrrpOperVirtualRouterUpTime,
       "vrrpOperProtocol": vrrpOperProtocol,
       "vrrpOperRowStatus": vrrpOperRowStatus,
       "vrrpAssoIpAddrTable": vrrpAssoIpAddrTable,
       "vrrpAssoIpAddrEntry": vrrpAssoIpAddrEntry,
       "vrrpAssoIpAddr": vrrpAssoIpAddr,
       "vrrpAssoIpAddrRowStatus": vrrpAssoIpAddrRowStatus,
       "vrrpTrapPacketSrc": vrrpTrapPacketSrc,
       "vrrpTrapAuthErrorType": vrrpTrapAuthErrorType,
       "vrrpStatistics": vrrpStatistics,
       "vrrpRouterChecksumErrors": vrrpRouterChecksumErrors,
       "vrrpRouterVersionErrors": vrrpRouterVersionErrors,
       "vrrpRouterVrIdErrors": vrrpRouterVrIdErrors,
       "vrrpRouterStatsTable": vrrpRouterStatsTable,
       "vrrpRouterStatsEntry": vrrpRouterStatsEntry,
       "vrrpStatsBecomeMaster": vrrpStatsBecomeMaster,
       "vrrpStatsAdvertiseRcvd": vrrpStatsAdvertiseRcvd,
       "vrrpStatsAdvertiseIntervalErrors": vrrpStatsAdvertiseIntervalErrors,
       "vrrpStatsAuthFailures": vrrpStatsAuthFailures,
       "vrrpStatsIpTtlErrors": vrrpStatsIpTtlErrors,
       "vrrpStatsPriorityZeroPktsRcvd": vrrpStatsPriorityZeroPktsRcvd,
       "vrrpStatsPriorityZeroPktsSent": vrrpStatsPriorityZeroPktsSent,
       "vrrpStatsInvalidTypePktsRcvd": vrrpStatsInvalidTypePktsRcvd,
       "vrrpStatsAddressListErrors": vrrpStatsAddressListErrors,
       "vrrpStatsInvalidAuthType": vrrpStatsInvalidAuthType,
       "vrrpStatsAuthTypeMismatch": vrrpStatsAuthTypeMismatch,
       "vrrpStatsPacketLengthErrors": vrrpStatsPacketLengthErrors,
       "vrrpConformance": vrrpConformance,
       "vrrpMIBCompliances": vrrpMIBCompliances,
       "vrrpMIBCompliance": vrrpMIBCompliance,
       "vrrpMIBGroups": vrrpMIBGroups,
       "vrrpOperGroup": vrrpOperGroup,
       "vrrpStatsGroup": vrrpStatsGroup,
       "vrrpTrapGroup": vrrpTrapGroup,
       "vrrpNotificationGroup": vrrpNotificationGroup}
)
