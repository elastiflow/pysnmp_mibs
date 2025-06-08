# SNMP MIB module (RUIJIE-AUTH-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-AUTH-GATEWAY-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:06:23 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ruijieWebAuthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40)
)
if mibBuilder.loadTexts:
    ruijieWebAuthMIB.setRevisions(
        ("2010-03-08 00:00",
         "2010-02-22 00:00",
         "2009-04-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieWebAuthMIBObjects_ObjectIdentity = ObjectIdentity
ruijieWebAuthMIBObjects = _RuijieWebAuthMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1)
)
_RuijieWebAuthUserTable_Object = MibTable
ruijieWebAuthUserTable = _RuijieWebAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieWebAuthUserTable.setStatus("current")
_RuijieWebAuthUserEntry_Object = MibTableRow
ruijieWebAuthUserEntry = _RuijieWebAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1)
)
ruijieWebAuthUserEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "authUserIpAddr"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthUserEntry.setStatus("current")
_AuthUserIpAddr_Type = IpAddress
_AuthUserIpAddr_Object = MibTableColumn
authUserIpAddr = _AuthUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 1),
    _AuthUserIpAddr_Type()
)
authUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserIpAddr.setStatus("current")
_AuthUserOnlineFlag_Type = Gauge32
_AuthUserOnlineFlag_Object = MibTableColumn
authUserOnlineFlag = _AuthUserOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 2),
    _AuthUserOnlineFlag_Type()
)
authUserOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserOnlineFlag.setStatus("current")
_AuthUserTimeLimit_Type = Gauge32
_AuthUserTimeLimit_Object = MibTableColumn
authUserTimeLimit = _AuthUserTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 3),
    _AuthUserTimeLimit_Type()
)
authUserTimeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserTimeLimit.setStatus("current")
_AuthUserTimeUsed_Type = Gauge32
_AuthUserTimeUsed_Object = MibTableColumn
authUserTimeUsed = _AuthUserTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 4),
    _AuthUserTimeUsed_Type()
)
authUserTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserTimeUsed.setStatus("current")
_AuthUserStatus_Type = RowStatus
_AuthUserStatus_Object = MibTableColumn
authUserStatus = _AuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 19),
    _AuthUserStatus_Type()
)
authUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserStatus.setStatus("current")


class _AuthUserRoleName_Type(OctetString):
    """Custom type authUserRoleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_AuthUserRoleName_Type.__name__ = "OctetString"
_AuthUserRoleName_Object = MibTableColumn
authUserRoleName = _AuthUserRoleName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 20),
    _AuthUserRoleName_Type()
)
authUserRoleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserRoleName.setStatus("current")


class _AuthUserSecZoneName_Type(OctetString):
    """Custom type authUserSecZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_AuthUserSecZoneName_Type.__name__ = "OctetString"
_AuthUserSecZoneName_Object = MibTableColumn
authUserSecZoneName = _AuthUserSecZoneName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 21),
    _AuthUserSecZoneName_Type()
)
authUserSecZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserSecZoneName.setStatus("current")
_AuthUserSecZonePermissionType_Type = Gauge32
_AuthUserSecZonePermissionType_Object = MibTableColumn
authUserSecZonePermissionType = _AuthUserSecZonePermissionType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 22),
    _AuthUserSecZonePermissionType_Type()
)
authUserSecZonePermissionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserSecZonePermissionType.setStatus("current")


class _AuthUserSecZonePermissionList_Type(OctetString):
    """Custom type authUserSecZonePermissionList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_AuthUserSecZonePermissionList_Type.__name__ = "OctetString"
_AuthUserSecZonePermissionList_Object = MibTableColumn
authUserSecZonePermissionList = _AuthUserSecZonePermissionList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 23),
    _AuthUserSecZonePermissionList_Type()
)
authUserSecZonePermissionList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserSecZonePermissionList.setStatus("current")
_AuthUserOtherPermissionType_Type = Gauge32
_AuthUserOtherPermissionType_Object = MibTableColumn
authUserOtherPermissionType = _AuthUserOtherPermissionType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 24),
    _AuthUserOtherPermissionType_Type()
)
authUserOtherPermissionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserOtherPermissionType.setStatus("current")
_AuthUserTerminateCause_Type = Gauge32
_AuthUserTerminateCause_Object = MibTableColumn
authUserTerminateCause = _AuthUserTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 1, 1, 25),
    _AuthUserTerminateCause_Type()
)
authUserTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserTerminateCause.setStatus("current")
_RuijieWebAuthUserExtTable_Object = MibTable
ruijieWebAuthUserExtTable = _RuijieWebAuthUserExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2)
)
if mibBuilder.loadTexts:
    ruijieWebAuthUserExtTable.setStatus("current")
_RuijieWebAuthUserExtEntry_Object = MibTableRow
ruijieWebAuthUserExtEntry = _RuijieWebAuthUserExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2, 1)
)
ruijieWebAuthUserExtEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "authUserExtAddrType"),
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "authUserExtAddr"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthUserExtEntry.setStatus("current")
_AuthUserExtAddrType_Type = InetAddressType
_AuthUserExtAddrType_Object = MibTableColumn
authUserExtAddrType = _AuthUserExtAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2, 1, 1),
    _AuthUserExtAddrType_Type()
)
authUserExtAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtAddrType.setStatus("current")


class _AuthUserExtAddr_Type(InetAddress):
    """Custom type authUserExtAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AuthUserExtAddr_Type.__name__ = "InetAddress"
_AuthUserExtAddr_Object = MibTableColumn
authUserExtAddr = _AuthUserExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2, 1, 2),
    _AuthUserExtAddr_Type()
)
authUserExtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtAddr.setStatus("current")
_AuthUserExtMac_Type = MacAddress
_AuthUserExtMac_Object = MibTableColumn
authUserExtMac = _AuthUserExtMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2, 1, 3),
    _AuthUserExtMac_Type()
)
authUserExtMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtMac.setStatus("current")
_AuthUserExtIfIndex_Type = IfIndex
_AuthUserExtIfIndex_Object = MibTableColumn
authUserExtIfIndex = _AuthUserExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2, 1, 4),
    _AuthUserExtIfIndex_Type()
)
authUserExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtIfIndex.setStatus("current")
_AuthUserExtVlanId_Type = Unsigned32
_AuthUserExtVlanId_Object = MibTableColumn
authUserExtVlanId = _AuthUserExtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2, 1, 5),
    _AuthUserExtVlanId_Type()
)
authUserExtVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtVlanId.setStatus("current")
_AuthUserExtOnlineFlag_Type = Gauge32
_AuthUserExtOnlineFlag_Object = MibTableColumn
authUserExtOnlineFlag = _AuthUserExtOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2, 1, 6),
    _AuthUserExtOnlineFlag_Type()
)
authUserExtOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtOnlineFlag.setStatus("current")
_AuthUserExtTimeLimit_Type = Gauge32
_AuthUserExtTimeLimit_Object = MibTableColumn
authUserExtTimeLimit = _AuthUserExtTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2, 1, 7),
    _AuthUserExtTimeLimit_Type()
)
authUserExtTimeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserExtTimeLimit.setStatus("current")
_AuthUserExtTimeUsed_Type = Gauge32
_AuthUserExtTimeUsed_Object = MibTableColumn
authUserExtTimeUsed = _AuthUserExtTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2, 1, 8),
    _AuthUserExtTimeUsed_Type()
)
authUserExtTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtTimeUsed.setStatus("current")


class _AuthUserExtErrCause_Type(DisplayString):
    """Custom type authUserExtErrCause based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AuthUserExtErrCause_Type.__name__ = "DisplayString"
_AuthUserExtErrCause_Object = MibTableColumn
authUserExtErrCause = _AuthUserExtErrCause_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2, 1, 9),
    _AuthUserExtErrCause_Type()
)
authUserExtErrCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authUserExtErrCause.setStatus("current")
_AuthUserExtStatus_Type = RowStatus
_AuthUserExtStatus_Object = MibTableColumn
authUserExtStatus = _AuthUserExtStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 2, 1, 10),
    _AuthUserExtStatus_Type()
)
authUserExtStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authUserExtStatus.setStatus("current")
_RuijieWebAuthWhiteListTable_Object = MibTable
ruijieWebAuthWhiteListTable = _RuijieWebAuthWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3)
)
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListTable.setStatus("current")
_RuijieWebAuthWhiteListEntry_Object = MibTableRow
ruijieWebAuthWhiteListEntry = _RuijieWebAuthWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1)
)
ruijieWebAuthWhiteListEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListAddress"),
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListNetMask"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListEntry.setStatus("current")
_RuijieWebAuthWhiteListAddress_Type = IpAddress
_RuijieWebAuthWhiteListAddress_Object = MibTableColumn
ruijieWebAuthWhiteListAddress = _RuijieWebAuthWhiteListAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 1),
    _RuijieWebAuthWhiteListAddress_Type()
)
ruijieWebAuthWhiteListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListAddress.setStatus("current")
_RuijieWebAuthWhiteListNetMask_Type = IpAddress
_RuijieWebAuthWhiteListNetMask_Object = MibTableColumn
ruijieWebAuthWhiteListNetMask = _RuijieWebAuthWhiteListNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 2),
    _RuijieWebAuthWhiteListNetMask_Type()
)
ruijieWebAuthWhiteListNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListNetMask.setStatus("current")
_RuijieWebAuthWhiteListPort1_Type = Unsigned32
_RuijieWebAuthWhiteListPort1_Object = MibTableColumn
ruijieWebAuthWhiteListPort1 = _RuijieWebAuthWhiteListPort1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 3),
    _RuijieWebAuthWhiteListPort1_Type()
)
ruijieWebAuthWhiteListPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListPort1.setStatus("current")
_RuijieWebAuthWhiteListPort2_Type = Unsigned32
_RuijieWebAuthWhiteListPort2_Object = MibTableColumn
ruijieWebAuthWhiteListPort2 = _RuijieWebAuthWhiteListPort2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 4),
    _RuijieWebAuthWhiteListPort2_Type()
)
ruijieWebAuthWhiteListPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListPort2.setStatus("current")
_RuijieWebAuthWhiteListPort3_Type = Unsigned32
_RuijieWebAuthWhiteListPort3_Object = MibTableColumn
ruijieWebAuthWhiteListPort3 = _RuijieWebAuthWhiteListPort3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 5),
    _RuijieWebAuthWhiteListPort3_Type()
)
ruijieWebAuthWhiteListPort3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListPort3.setStatus("current")
_RuijieWebAuthWhiteListPort4_Type = Unsigned32
_RuijieWebAuthWhiteListPort4_Object = MibTableColumn
ruijieWebAuthWhiteListPort4 = _RuijieWebAuthWhiteListPort4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 6),
    _RuijieWebAuthWhiteListPort4_Type()
)
ruijieWebAuthWhiteListPort4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListPort4.setStatus("current")
_RuijieWebAuthWhiteListPort5_Type = Unsigned32
_RuijieWebAuthWhiteListPort5_Object = MibTableColumn
ruijieWebAuthWhiteListPort5 = _RuijieWebAuthWhiteListPort5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 7),
    _RuijieWebAuthWhiteListPort5_Type()
)
ruijieWebAuthWhiteListPort5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListPort5.setStatus("current")
_RuijieWebAuthWhiteListPort6_Type = Unsigned32
_RuijieWebAuthWhiteListPort6_Object = MibTableColumn
ruijieWebAuthWhiteListPort6 = _RuijieWebAuthWhiteListPort6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 8),
    _RuijieWebAuthWhiteListPort6_Type()
)
ruijieWebAuthWhiteListPort6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListPort6.setStatus("current")
_RuijieWebAuthWhiteListPort7_Type = Unsigned32
_RuijieWebAuthWhiteListPort7_Object = MibTableColumn
ruijieWebAuthWhiteListPort7 = _RuijieWebAuthWhiteListPort7_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 9),
    _RuijieWebAuthWhiteListPort7_Type()
)
ruijieWebAuthWhiteListPort7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListPort7.setStatus("current")
_RuijieWebAuthWhiteListPort8_Type = Unsigned32
_RuijieWebAuthWhiteListPort8_Object = MibTableColumn
ruijieWebAuthWhiteListPort8 = _RuijieWebAuthWhiteListPort8_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 10),
    _RuijieWebAuthWhiteListPort8_Type()
)
ruijieWebAuthWhiteListPort8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListPort8.setStatus("current")


class _RuijieWebAuthWhiteListBindArpFlag_Type(Integer32):
    """Custom type ruijieWebAuthWhiteListBindArpFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieWebAuthWhiteListBindArpFlag_Type.__name__ = "Integer32"
_RuijieWebAuthWhiteListBindArpFlag_Object = MibTableColumn
ruijieWebAuthWhiteListBindArpFlag = _RuijieWebAuthWhiteListBindArpFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 11),
    _RuijieWebAuthWhiteListBindArpFlag_Type()
)
ruijieWebAuthWhiteListBindArpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListBindArpFlag.setStatus("current")
_RuijieWebAuthWhiteListStatus_Type = RowStatus
_RuijieWebAuthWhiteListStatus_Object = MibTableColumn
ruijieWebAuthWhiteListStatus = _RuijieWebAuthWhiteListStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 3, 1, 12),
    _RuijieWebAuthWhiteListStatus_Type()
)
ruijieWebAuthWhiteListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthWhiteListStatus.setStatus("current")
_RuijieWebAuthSDGUserTable_Object = MibTable
ruijieWebAuthSDGUserTable = _RuijieWebAuthSDGUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4)
)
if mibBuilder.loadTexts:
    ruijieWebAuthSDGUserTable.setStatus("current")
_RuijieWebAuthSDGUserEntry_Object = MibTableRow
ruijieWebAuthSDGUserEntry = _RuijieWebAuthSDGUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1)
)
ruijieWebAuthSDGUserEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserVrfg"),
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserIpAddr"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthSDGUserEntry.setStatus("current")


class _AuthSDGUserVrfg_Type(DisplayString):
    """Custom type authSDGUserVrfg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AuthSDGUserVrfg_Type.__name__ = "DisplayString"
_AuthSDGUserVrfg_Object = MibTableColumn
authSDGUserVrfg = _AuthSDGUserVrfg_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 1),
    _AuthSDGUserVrfg_Type()
)
authSDGUserVrfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserVrfg.setStatus("current")
_AuthSDGUserIpAddr_Type = IpAddress
_AuthSDGUserIpAddr_Object = MibTableColumn
authSDGUserIpAddr = _AuthSDGUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 2),
    _AuthSDGUserIpAddr_Type()
)
authSDGUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserIpAddr.setStatus("current")
_AuthSDGUserOnlineFlag_Type = Gauge32
_AuthSDGUserOnlineFlag_Object = MibTableColumn
authSDGUserOnlineFlag = _AuthSDGUserOnlineFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 3),
    _AuthSDGUserOnlineFlag_Type()
)
authSDGUserOnlineFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserOnlineFlag.setStatus("current")
_AuthSDGUserTimeLimit_Type = Gauge32
_AuthSDGUserTimeLimit_Object = MibTableColumn
authSDGUserTimeLimit = _AuthSDGUserTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 4),
    _AuthSDGUserTimeLimit_Type()
)
authSDGUserTimeLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserTimeLimit.setStatus("current")
_AuthSDGUserTimeUsed_Type = Gauge32
_AuthSDGUserTimeUsed_Object = MibTableColumn
authSDGUserTimeUsed = _AuthSDGUserTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 5),
    _AuthSDGUserTimeUsed_Type()
)
authSDGUserTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserTimeUsed.setStatus("current")
_AuthSDGUserVrf_Type = DisplayString
_AuthSDGUserVrf_Object = MibTableColumn
authSDGUserVrf = _AuthSDGUserVrf_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 6),
    _AuthSDGUserVrf_Type()
)
authSDGUserVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserVrf.setStatus("current")


class _AuthSDGUserRoleName_Type(OctetString):
    """Custom type authSDGUserRoleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_AuthSDGUserRoleName_Type.__name__ = "OctetString"
_AuthSDGUserRoleName_Object = MibTableColumn
authSDGUserRoleName = _AuthSDGUserRoleName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 21),
    _AuthSDGUserRoleName_Type()
)
authSDGUserRoleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserRoleName.setStatus("current")


class _AuthSDGUserSecZoneName_Type(OctetString):
    """Custom type authSDGUserSecZoneName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_AuthSDGUserSecZoneName_Type.__name__ = "OctetString"
_AuthSDGUserSecZoneName_Object = MibTableColumn
authSDGUserSecZoneName = _AuthSDGUserSecZoneName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 22),
    _AuthSDGUserSecZoneName_Type()
)
authSDGUserSecZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserSecZoneName.setStatus("current")
_AuthSDGUserSecZonePermissionType_Type = Gauge32
_AuthSDGUserSecZonePermissionType_Object = MibTableColumn
authSDGUserSecZonePermissionType = _AuthSDGUserSecZonePermissionType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 23),
    _AuthSDGUserSecZonePermissionType_Type()
)
authSDGUserSecZonePermissionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserSecZonePermissionType.setStatus("current")


class _AuthSDGUserSecZonePermissionList_Type(OctetString):
    """Custom type authSDGUserSecZonePermissionList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_AuthSDGUserSecZonePermissionList_Type.__name__ = "OctetString"
_AuthSDGUserSecZonePermissionList_Object = MibTableColumn
authSDGUserSecZonePermissionList = _AuthSDGUserSecZonePermissionList_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 24),
    _AuthSDGUserSecZonePermissionList_Type()
)
authSDGUserSecZonePermissionList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserSecZonePermissionList.setStatus("current")
_AuthSDGUserOtherPermissionType_Type = Gauge32
_AuthSDGUserOtherPermissionType_Object = MibTableColumn
authSDGUserOtherPermissionType = _AuthSDGUserOtherPermissionType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 25),
    _AuthSDGUserOtherPermissionType_Type()
)
authSDGUserOtherPermissionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserOtherPermissionType.setStatus("current")
_AuthSDGUserTerminateCause_Type = Gauge32
_AuthSDGUserTerminateCause_Object = MibTableColumn
authSDGUserTerminateCause = _AuthSDGUserTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 26),
    _AuthSDGUserTerminateCause_Type()
)
authSDGUserTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authSDGUserTerminateCause.setStatus("current")
_AuthSDGUserStatus_Type = RowStatus
_AuthSDGUserStatus_Object = MibTableColumn
authSDGUserStatus = _AuthSDGUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 4, 1, 27),
    _AuthSDGUserStatus_Type()
)
authSDGUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    authSDGUserStatus.setStatus("current")
_RuijieWebAuthMacUserTable_Object = MibTable
ruijieWebAuthMacUserTable = _RuijieWebAuthMacUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 5)
)
if mibBuilder.loadTexts:
    ruijieWebAuthMacUserTable.setStatus("current")
_RuijieWebAuthMacUserEntry_Object = MibTableRow
ruijieWebAuthMacUserEntry = _RuijieWebAuthMacUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 5, 1)
)
ruijieWebAuthMacUserEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieAuthMacUserMacAddr"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthMacUserEntry.setStatus("current")
_RuijieAuthMacUserMacAddr_Type = MacAddress
_RuijieAuthMacUserMacAddr_Object = MibTableColumn
ruijieAuthMacUserMacAddr = _RuijieAuthMacUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 5, 1, 1),
    _RuijieAuthMacUserMacAddr_Type()
)
ruijieAuthMacUserMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthMacUserMacAddr.setStatus("current")


class _RuijieAuthMacUserName_Type(OctetString):
    """Custom type ruijieAuthMacUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(253, 253),
    )
    fixed_length = 253


_RuijieAuthMacUserName_Type.__name__ = "OctetString"
_RuijieAuthMacUserName_Object = MibTableColumn
ruijieAuthMacUserName = _RuijieAuthMacUserName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 5, 1, 2),
    _RuijieAuthMacUserName_Type()
)
ruijieAuthMacUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthMacUserName.setStatus("current")


class _RuijieAuthMacUserTerminalId_Type(OctetString):
    """Custom type ruijieAuthMacUserTerminalId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(253, 253),
    )
    fixed_length = 253


_RuijieAuthMacUserTerminalId_Type.__name__ = "OctetString"
_RuijieAuthMacUserTerminalId_Object = MibTableColumn
ruijieAuthMacUserTerminalId = _RuijieAuthMacUserTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 5, 1, 3),
    _RuijieAuthMacUserTerminalId_Type()
)
ruijieAuthMacUserTerminalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthMacUserTerminalId.setStatus("current")
_RuijieWebAuthUserMIB_ObjectIdentity = ObjectIdentity
ruijieWebAuthUserMIB = _RuijieWebAuthUserMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 6)
)
_RuijieWebAuthUserMIBTable_Object = MibTable
ruijieWebAuthUserMIBTable = _RuijieWebAuthUserMIBTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ruijieWebAuthUserMIBTable.setStatus("current")
_RuijieWebAuthUserMIBEntry_Object = MibTableRow
ruijieWebAuthUserMIBEntry = _RuijieWebAuthUserMIBEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 6, 1, 1)
)
ruijieWebAuthUserMIBEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieAuthUserMIBIpAddress"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthUserMIBEntry.setStatus("current")
_RuijieAuthUserMIBIpAddress_Type = IpAddress
_RuijieAuthUserMIBIpAddress_Object = MibTableColumn
ruijieAuthUserMIBIpAddress = _RuijieAuthUserMIBIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 6, 1, 1, 1),
    _RuijieAuthUserMIBIpAddress_Type()
)
ruijieAuthUserMIBIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserMIBIpAddress.setStatus("current")
_RuijieAuthUserMIBName_Type = OctetString
_RuijieAuthUserMIBName_Object = MibTableColumn
ruijieAuthUserMIBName = _RuijieAuthUserMIBName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 6, 1, 1, 2),
    _RuijieAuthUserMIBName_Type()
)
ruijieAuthUserMIBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserMIBName.setStatus("current")
_RuijieAuthUserMIBAuthType_Type = Gauge32
_RuijieAuthUserMIBAuthType_Object = MibTableColumn
ruijieAuthUserMIBAuthType = _RuijieAuthUserMIBAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 6, 1, 1, 3),
    _RuijieAuthUserMIBAuthType_Type()
)
ruijieAuthUserMIBAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserMIBAuthType.setStatus("current")
_RuijieAuthUserMIBMacAddress_Type = MacAddress
_RuijieAuthUserMIBMacAddress_Object = MibTableColumn
ruijieAuthUserMIBMacAddress = _RuijieAuthUserMIBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 6, 1, 1, 4),
    _RuijieAuthUserMIBMacAddress_Type()
)
ruijieAuthUserMIBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserMIBMacAddress.setStatus("current")
_RuijieAuthUserMIBVlanId_Type = Gauge32
_RuijieAuthUserMIBVlanId_Object = MibTableColumn
ruijieAuthUserMIBVlanId = _RuijieAuthUserMIBVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 6, 1, 1, 5),
    _RuijieAuthUserMIBVlanId_Type()
)
ruijieAuthUserMIBVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserMIBVlanId.setStatus("current")
_RuijieAuthUserMIBPortIndex_Type = Gauge32
_RuijieAuthUserMIBPortIndex_Object = MibTableColumn
ruijieAuthUserMIBPortIndex = _RuijieAuthUserMIBPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 6, 1, 1, 6),
    _RuijieAuthUserMIBPortIndex_Type()
)
ruijieAuthUserMIBPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserMIBPortIndex.setStatus("current")
_RuijieAuthUserMIBTimeUsed_Type = Gauge32
_RuijieAuthUserMIBTimeUsed_Object = MibTableColumn
ruijieAuthUserMIBTimeUsed = _RuijieAuthUserMIBTimeUsed_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 6, 1, 1, 7),
    _RuijieAuthUserMIBTimeUsed_Type()
)
ruijieAuthUserMIBTimeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieAuthUserMIBTimeUsed.setStatus("current")
_RuijieWebAuthDirectSiteTable_Object = MibTable
ruijieWebAuthDirectSiteTable = _RuijieWebAuthDirectSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 7)
)
if mibBuilder.loadTexts:
    ruijieWebAuthDirectSiteTable.setStatus("current")
_RuijieWebAuthDirectSiteEntry_Object = MibTableRow
ruijieWebAuthDirectSiteEntry = _RuijieWebAuthDirectSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 7, 1)
)
ruijieWebAuthDirectSiteEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectSiteAddress"),
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectSiteNetMask"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthDirectSiteEntry.setStatus("current")
_RuijieWebAuthDirectSiteAddress_Type = IpAddress
_RuijieWebAuthDirectSiteAddress_Object = MibTableColumn
ruijieWebAuthDirectSiteAddress = _RuijieWebAuthDirectSiteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 7, 1, 1),
    _RuijieWebAuthDirectSiteAddress_Type()
)
ruijieWebAuthDirectSiteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectSiteAddress.setStatus("current")
_RuijieWebAuthDirectSiteNetMask_Type = IpAddress
_RuijieWebAuthDirectSiteNetMask_Object = MibTableColumn
ruijieWebAuthDirectSiteNetMask = _RuijieWebAuthDirectSiteNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 7, 1, 2),
    _RuijieWebAuthDirectSiteNetMask_Type()
)
ruijieWebAuthDirectSiteNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectSiteNetMask.setStatus("current")
_RuijieWebAuthDirectSiteStatus_Type = RowStatus
_RuijieWebAuthDirectSiteStatus_Object = MibTableColumn
ruijieWebAuthDirectSiteStatus = _RuijieWebAuthDirectSiteStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 7, 1, 3),
    _RuijieWebAuthDirectSiteStatus_Type()
)
ruijieWebAuthDirectSiteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectSiteStatus.setStatus("current")


class _RuijieWebAuthDirectSiteBindArpFlag_Type(Integer32):
    """Custom type ruijieWebAuthDirectSiteBindArpFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieWebAuthDirectSiteBindArpFlag_Type.__name__ = "Integer32"
_RuijieWebAuthDirectSiteBindArpFlag_Object = MibTableColumn
ruijieWebAuthDirectSiteBindArpFlag = _RuijieWebAuthDirectSiteBindArpFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 7, 1, 4),
    _RuijieWebAuthDirectSiteBindArpFlag_Type()
)
ruijieWebAuthDirectSiteBindArpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectSiteBindArpFlag.setStatus("current")
_RuijieWebAuthDirectHostTable_Object = MibTable
ruijieWebAuthDirectHostTable = _RuijieWebAuthDirectHostTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8)
)
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostTable.setStatus("current")
_RuijieWebAuthDirectHostEntry_Object = MibTableRow
ruijieWebAuthDirectHostEntry = _RuijieWebAuthDirectHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1)
)
ruijieWebAuthDirectHostEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostAddress"),
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostNetMask"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostEntry.setStatus("current")
_RuijieWebAuthDirectHostAddress_Type = IpAddress
_RuijieWebAuthDirectHostAddress_Object = MibTableColumn
ruijieWebAuthDirectHostAddress = _RuijieWebAuthDirectHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 1),
    _RuijieWebAuthDirectHostAddress_Type()
)
ruijieWebAuthDirectHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostAddress.setStatus("current")
_RuijieWebAuthDirectHostNetMask_Type = IpAddress
_RuijieWebAuthDirectHostNetMask_Object = MibTableColumn
ruijieWebAuthDirectHostNetMask = _RuijieWebAuthDirectHostNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 2),
    _RuijieWebAuthDirectHostNetMask_Type()
)
ruijieWebAuthDirectHostNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostNetMask.setStatus("current")
_RuijieWebAuthDirectHostPort1_Type = Unsigned32
_RuijieWebAuthDirectHostPort1_Object = MibTableColumn
ruijieWebAuthDirectHostPort1 = _RuijieWebAuthDirectHostPort1_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 3),
    _RuijieWebAuthDirectHostPort1_Type()
)
ruijieWebAuthDirectHostPort1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostPort1.setStatus("current")
_RuijieWebAuthDirectHostPort2_Type = Unsigned32
_RuijieWebAuthDirectHostPort2_Object = MibTableColumn
ruijieWebAuthDirectHostPort2 = _RuijieWebAuthDirectHostPort2_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 4),
    _RuijieWebAuthDirectHostPort2_Type()
)
ruijieWebAuthDirectHostPort2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostPort2.setStatus("current")
_RuijieWebAuthDirectHostPort3_Type = Unsigned32
_RuijieWebAuthDirectHostPort3_Object = MibTableColumn
ruijieWebAuthDirectHostPort3 = _RuijieWebAuthDirectHostPort3_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 5),
    _RuijieWebAuthDirectHostPort3_Type()
)
ruijieWebAuthDirectHostPort3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostPort3.setStatus("current")
_RuijieWebAuthDirectHostPort4_Type = Unsigned32
_RuijieWebAuthDirectHostPort4_Object = MibTableColumn
ruijieWebAuthDirectHostPort4 = _RuijieWebAuthDirectHostPort4_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 6),
    _RuijieWebAuthDirectHostPort4_Type()
)
ruijieWebAuthDirectHostPort4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostPort4.setStatus("current")
_RuijieWebAuthDirectHostPort5_Type = Unsigned32
_RuijieWebAuthDirectHostPort5_Object = MibTableColumn
ruijieWebAuthDirectHostPort5 = _RuijieWebAuthDirectHostPort5_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 7),
    _RuijieWebAuthDirectHostPort5_Type()
)
ruijieWebAuthDirectHostPort5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostPort5.setStatus("current")
_RuijieWebAuthDirectHostPort6_Type = Unsigned32
_RuijieWebAuthDirectHostPort6_Object = MibTableColumn
ruijieWebAuthDirectHostPort6 = _RuijieWebAuthDirectHostPort6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 8),
    _RuijieWebAuthDirectHostPort6_Type()
)
ruijieWebAuthDirectHostPort6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostPort6.setStatus("current")
_RuijieWebAuthDirectHostPort7_Type = Unsigned32
_RuijieWebAuthDirectHostPort7_Object = MibTableColumn
ruijieWebAuthDirectHostPort7 = _RuijieWebAuthDirectHostPort7_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 9),
    _RuijieWebAuthDirectHostPort7_Type()
)
ruijieWebAuthDirectHostPort7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostPort7.setStatus("current")
_RuijieWebAuthDirectHostPort8_Type = Unsigned32
_RuijieWebAuthDirectHostPort8_Object = MibTableColumn
ruijieWebAuthDirectHostPort8 = _RuijieWebAuthDirectHostPort8_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 10),
    _RuijieWebAuthDirectHostPort8_Type()
)
ruijieWebAuthDirectHostPort8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostPort8.setStatus("current")


class _RuijieWebAuthDirectHostBindArpFlag_Type(Integer32):
    """Custom type ruijieWebAuthDirectHostBindArpFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_RuijieWebAuthDirectHostBindArpFlag_Type.__name__ = "Integer32"
_RuijieWebAuthDirectHostBindArpFlag_Object = MibTableColumn
ruijieWebAuthDirectHostBindArpFlag = _RuijieWebAuthDirectHostBindArpFlag_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 11),
    _RuijieWebAuthDirectHostBindArpFlag_Type()
)
ruijieWebAuthDirectHostBindArpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostBindArpFlag.setStatus("current")
_RuijieWebAuthDirectHostStatus_Type = RowStatus
_RuijieWebAuthDirectHostStatus_Object = MibTableColumn
ruijieWebAuthDirectHostStatus = _RuijieWebAuthDirectHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 12),
    _RuijieWebAuthDirectHostStatus_Type()
)
ruijieWebAuthDirectHostStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostStatus.setStatus("current")
_RuijieWebAuthDirectHostPortIfx_Type = Gauge32
_RuijieWebAuthDirectHostPortIfx_Object = MibTableColumn
ruijieWebAuthDirectHostPortIfx = _RuijieWebAuthDirectHostPortIfx_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 8, 1, 13),
    _RuijieWebAuthDirectHostPortIfx_Type()
)
ruijieWebAuthDirectHostPortIfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthDirectHostPortIfx.setStatus("current")
_RuijieWebAuthFreeAcctIpTable_Object = MibTable
ruijieWebAuthFreeAcctIpTable = _RuijieWebAuthFreeAcctIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 9)
)
if mibBuilder.loadTexts:
    ruijieWebAuthFreeAcctIpTable.setStatus("current")
_RuijieWebAuthFreeAcctIpEntry_Object = MibTableRow
ruijieWebAuthFreeAcctIpEntry = _RuijieWebAuthFreeAcctIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 9, 1)
)
ruijieWebAuthFreeAcctIpEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthFreeAcctIpAddress"),
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthFreeAcctIpNetMask"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthFreeAcctIpEntry.setStatus("current")
_RuijieWebAuthFreeAcctIpAddress_Type = IpAddress
_RuijieWebAuthFreeAcctIpAddress_Object = MibTableColumn
ruijieWebAuthFreeAcctIpAddress = _RuijieWebAuthFreeAcctIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 9, 1, 1),
    _RuijieWebAuthFreeAcctIpAddress_Type()
)
ruijieWebAuthFreeAcctIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthFreeAcctIpAddress.setStatus("current")
_RuijieWebAuthFreeAcctIpNetMask_Type = IpAddress
_RuijieWebAuthFreeAcctIpNetMask_Object = MibTableColumn
ruijieWebAuthFreeAcctIpNetMask = _RuijieWebAuthFreeAcctIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 9, 1, 2),
    _RuijieWebAuthFreeAcctIpNetMask_Type()
)
ruijieWebAuthFreeAcctIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthFreeAcctIpNetMask.setStatus("current")
_RuijieWebAuthFreeAcctIpStatus_Type = RowStatus
_RuijieWebAuthFreeAcctIpStatus_Object = MibTableColumn
ruijieWebAuthFreeAcctIpStatus = _RuijieWebAuthFreeAcctIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 9, 1, 3),
    _RuijieWebAuthFreeAcctIpStatus_Type()
)
ruijieWebAuthFreeAcctIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthFreeAcctIpStatus.setStatus("current")
_RuijieWebAuthFreeAcctUrlTable_Object = MibTable
ruijieWebAuthFreeAcctUrlTable = _RuijieWebAuthFreeAcctUrlTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 10)
)
if mibBuilder.loadTexts:
    ruijieWebAuthFreeAcctUrlTable.setStatus("current")
_RuijieWebAuthFreeAcctUrlEntry_Object = MibTableRow
ruijieWebAuthFreeAcctUrlEntry = _RuijieWebAuthFreeAcctUrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 10, 1)
)
ruijieWebAuthFreeAcctUrlEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthFreeAcctUrl"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthFreeAcctUrlEntry.setStatus("current")
_RuijieWebAuthFreeAcctUrl_Type = OctetString
_RuijieWebAuthFreeAcctUrl_Object = MibTableColumn
ruijieWebAuthFreeAcctUrl = _RuijieWebAuthFreeAcctUrl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 10, 1, 1),
    _RuijieWebAuthFreeAcctUrl_Type()
)
ruijieWebAuthFreeAcctUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthFreeAcctUrl.setStatus("current")
_RuijieWebAuthFreeAcctUrlStatus_Type = RowStatus
_RuijieWebAuthFreeAcctUrlStatus_Object = MibTableColumn
ruijieWebAuthFreeAcctUrlStatus = _RuijieWebAuthFreeAcctUrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 10, 1, 2),
    _RuijieWebAuthFreeAcctUrlStatus_Type()
)
ruijieWebAuthFreeAcctUrlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthFreeAcctUrlStatus.setStatus("current")
_RuijieWebAuthOfflineDetectTable_Object = MibTable
ruijieWebAuthOfflineDetectTable = _RuijieWebAuthOfflineDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 11)
)
if mibBuilder.loadTexts:
    ruijieWebAuthOfflineDetectTable.setStatus("current")
_RuijieWebAuthOfflineDetectEntry_Object = MibTableRow
ruijieWebAuthOfflineDetectEntry = _RuijieWebAuthOfflineDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 11, 1)
)
ruijieWebAuthOfflineDetectEntry.setIndexNames(
    (0, "RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthOfflineDetectime"),
)
if mibBuilder.loadTexts:
    ruijieWebAuthOfflineDetectEntry.setStatus("current")
_RuijieWebAuthOfflineDetectime_Type = Unsigned32
_RuijieWebAuthOfflineDetectime_Object = MibTableColumn
ruijieWebAuthOfflineDetectime = _RuijieWebAuthOfflineDetectime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 11, 1, 1),
    _RuijieWebAuthOfflineDetectime_Type()
)
ruijieWebAuthOfflineDetectime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthOfflineDetectime.setStatus("current")
_RuijieWebAuthOfflineDetectStatus_Type = RowStatus
_RuijieWebAuthOfflineDetectStatus_Object = MibTableColumn
ruijieWebAuthOfflineDetectStatus = _RuijieWebAuthOfflineDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 11, 1, 2),
    _RuijieWebAuthOfflineDetectStatus_Type()
)
ruijieWebAuthOfflineDetectStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijieWebAuthOfflineDetectStatus.setStatus("current")
_RuijieWebAuthCurrentOnlineUser_Type = Integer32
_RuijieWebAuthCurrentOnlineUser_Object = MibScalar
ruijieWebAuthCurrentOnlineUser = _RuijieWebAuthCurrentOnlineUser_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 12),
    _RuijieWebAuthCurrentOnlineUser_Type()
)
ruijieWebAuthCurrentOnlineUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthCurrentOnlineUser.setStatus("current")
_RuijieWebAuthCurrentUser_Type = Integer32
_RuijieWebAuthCurrentUser_Object = MibScalar
ruijieWebAuthCurrentUser = _RuijieWebAuthCurrentUser_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 13),
    _RuijieWebAuthCurrentUser_Type()
)
ruijieWebAuthCurrentUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthCurrentUser.setStatus("current")
_RuijieWebAuthMaximumOnlineUser_Type = Integer32
_RuijieWebAuthMaximumOnlineUser_Object = MibScalar
ruijieWebAuthMaximumOnlineUser = _RuijieWebAuthMaximumOnlineUser_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 1, 14),
    _RuijieWebAuthMaximumOnlineUser_Type()
)
ruijieWebAuthMaximumOnlineUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieWebAuthMaximumOnlineUser.setStatus("current")
_RuijieWebAuthMIBTraps_ObjectIdentity = ObjectIdentity
ruijieWebAuthMIBTraps = _RuijieWebAuthMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 2)
)
_RuijieWebAuthMIBConformance_ObjectIdentity = ObjectIdentity
ruijieWebAuthMIBConformance = _RuijieWebAuthMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 3)
)
_RuijieWebAuthMIBCompliances_ObjectIdentity = ObjectIdentity
ruijieWebAuthMIBCompliances = _RuijieWebAuthMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 3, 1)
)
_RuijieWebAuthMIBGroups_ObjectIdentity = ObjectIdentity
ruijieWebAuthMIBGroups = _RuijieWebAuthMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 3, 2)
)
_RuijieWebAuthMIBTrapsObjects_ObjectIdentity = ObjectIdentity
ruijieWebAuthMIBTrapsObjects = _RuijieWebAuthMIBTrapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4)
)
_RuijieWebAuthApMac_Type = MacAddress
_RuijieWebAuthApMac_Object = MibScalar
ruijieWebAuthApMac = _RuijieWebAuthApMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 1),
    _RuijieWebAuthApMac_Type()
)
ruijieWebAuthApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthApMac.setStatus("current")
_RuijieWebAuthApIp_Type = IpAddress
_RuijieWebAuthApIp_Object = MibScalar
ruijieWebAuthApIp = _RuijieWebAuthApIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 2),
    _RuijieWebAuthApIp_Type()
)
ruijieWebAuthApIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthApIp.setStatus("current")
_RuijieWebAuthStaMac_Type = MacAddress
_RuijieWebAuthStaMac_Object = MibScalar
ruijieWebAuthStaMac = _RuijieWebAuthStaMac_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 3),
    _RuijieWebAuthStaMac_Type()
)
ruijieWebAuthStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaMac.setStatus("current")
_RuijieWebAuthStaIp_Type = IpAddress
_RuijieWebAuthStaIp_Object = MibScalar
ruijieWebAuthStaIp = _RuijieWebAuthStaIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 4),
    _RuijieWebAuthStaIp_Type()
)
ruijieWebAuthStaIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaIp.setStatus("current")
_RuijieWebAuthStaIpv6_Type = InetAddress
_RuijieWebAuthStaIpv6_Object = MibScalar
ruijieWebAuthStaIpv6 = _RuijieWebAuthStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 5),
    _RuijieWebAuthStaIpv6_Type()
)
ruijieWebAuthStaIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaIpv6.setStatus("current")


class _RuijieWebAuthStaOperType_Type(Integer32):
    """Custom type ruijieWebAuthStaOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RuijieWebAuthStaOperType_Type.__name__ = "Integer32"
_RuijieWebAuthStaOperType_Object = MibScalar
ruijieWebAuthStaOperType = _RuijieWebAuthStaOperType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 6),
    _RuijieWebAuthStaOperType_Type()
)
ruijieWebAuthStaOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaOperType.setStatus("current")


class _RuijieWebAuthStaApRadioId_Type(Integer32):
    """Custom type ruijieWebAuthStaApRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieWebAuthStaApRadioId_Type.__name__ = "Integer32"
_RuijieWebAuthStaApRadioId_Object = MibScalar
ruijieWebAuthStaApRadioId = _RuijieWebAuthStaApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 7),
    _RuijieWebAuthStaApRadioId_Type()
)
ruijieWebAuthStaApRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaApRadioId.setStatus("current")


class _RuijieWebAuthStaApRadioType_Type(Integer32):
    """Custom type ruijieWebAuthStaApRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieWebAuthStaApRadioType_Type.__name__ = "Integer32"
_RuijieWebAuthStaApRadioType_Object = MibScalar
ruijieWebAuthStaApRadioType = _RuijieWebAuthStaApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 8),
    _RuijieWebAuthStaApRadioType_Type()
)
ruijieWebAuthStaApRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaApRadioType.setStatus("current")


class _RuijieWebAuthStaVlanId_Type(Integer32):
    """Custom type ruijieWebAuthStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuijieWebAuthStaVlanId_Type.__name__ = "Integer32"
_RuijieWebAuthStaVlanId_Object = MibScalar
ruijieWebAuthStaVlanId = _RuijieWebAuthStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 9),
    _RuijieWebAuthStaVlanId_Type()
)
ruijieWebAuthStaVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaVlanId.setStatus("current")


class _RuijieWebAuthStaWlanId_Type(Integer32):
    """Custom type ruijieWebAuthStaWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_RuijieWebAuthStaWlanId_Type.__name__ = "Integer32"
_RuijieWebAuthStaWlanId_Object = MibScalar
ruijieWebAuthStaWlanId = _RuijieWebAuthStaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 10),
    _RuijieWebAuthStaWlanId_Type()
)
ruijieWebAuthStaWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaWlanId.setStatus("current")
_RuijieWebAuthOperTime_Type = TimeTicks
_RuijieWebAuthOperTime_Object = MibScalar
ruijieWebAuthOperTime = _RuijieWebAuthOperTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 11),
    _RuijieWebAuthOperTime_Type()
)
ruijieWebAuthOperTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthOperTime.setStatus("current")


class _RuijieWebAuthStaAssoAuthMode_Type(Integer32):
    """Custom type ruijieWebAuthStaAssoAuthMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("wep", 1),
          ("dot1x-wep", 2),
          ("dot1x-wpa", 3),
          ("dot1x-wpa2", 4),
          ("mab", 5),
          ("psk-wpa", 6),
          ("psk-wpa2", 7),
          ("wapi", 8))
    )


_RuijieWebAuthStaAssoAuthMode_Type.__name__ = "Integer32"
_RuijieWebAuthStaAssoAuthMode_Object = MibScalar
ruijieWebAuthStaAssoAuthMode = _RuijieWebAuthStaAssoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 12),
    _RuijieWebAuthStaAssoAuthMode_Type()
)
ruijieWebAuthStaAssoAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaAssoAuthMode.setStatus("current")


class _RuijieWebAuthStaNetAuthMode_Type(Integer32):
    """Custom type ruijieWebAuthStaNetAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("web", 1))
    )


_RuijieWebAuthStaNetAuthMode_Type.__name__ = "Integer32"
_RuijieWebAuthStaNetAuthMode_Object = MibScalar
ruijieWebAuthStaNetAuthMode = _RuijieWebAuthStaNetAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 13),
    _RuijieWebAuthStaNetAuthMode_Type()
)
ruijieWebAuthStaNetAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaNetAuthMode.setStatus("current")
_RuijieWebAuthStaRssi_Type = Integer32
_RuijieWebAuthStaRssi_Object = MibScalar
ruijieWebAuthStaRssi = _RuijieWebAuthStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 14),
    _RuijieWebAuthStaRssi_Type()
)
ruijieWebAuthStaRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaRssi.setStatus("current")
_RuijieWebAuthStaSsid_Type = DisplayString
_RuijieWebAuthStaSsid_Object = MibScalar
ruijieWebAuthStaSsid = _RuijieWebAuthStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 15),
    _RuijieWebAuthStaSsid_Type()
)
ruijieWebAuthStaSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaSsid.setStatus("current")
_RuijieWebAuthStaLinkRate_Type = Integer32
_RuijieWebAuthStaLinkRate_Object = MibScalar
ruijieWebAuthStaLinkRate = _RuijieWebAuthStaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 16),
    _RuijieWebAuthStaLinkRate_Type()
)
ruijieWebAuthStaLinkRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaLinkRate.setStatus("current")
_RuijieWebAuthStaCurChannel_Type = Integer32
_RuijieWebAuthStaCurChannel_Object = MibScalar
ruijieWebAuthStaCurChannel = _RuijieWebAuthStaCurChannel_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 17),
    _RuijieWebAuthStaCurChannel_Type()
)
ruijieWebAuthStaCurChannel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaCurChannel.setStatus("current")


class _RuijieWebAuthStaUsername_Type(DisplayString):
    """Custom type ruijieWebAuthStaUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuijieWebAuthStaUsername_Type.__name__ = "DisplayString"
_RuijieWebAuthStaUsername_Object = MibScalar
ruijieWebAuthStaUsername = _RuijieWebAuthStaUsername_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 18),
    _RuijieWebAuthStaUsername_Type()
)
ruijieWebAuthStaUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaUsername.setStatus("current")
_RuijieWebAuthStaTerminalType_Type = DisplayString
_RuijieWebAuthStaTerminalType_Object = MibScalar
ruijieWebAuthStaTerminalType = _RuijieWebAuthStaTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 19),
    _RuijieWebAuthStaTerminalType_Type()
)
ruijieWebAuthStaTerminalType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaTerminalType.setStatus("current")
_RuijieWebAuthStaTerminateCause_Type = Integer32
_RuijieWebAuthStaTerminateCause_Object = MibScalar
ruijieWebAuthStaTerminateCause = _RuijieWebAuthStaTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 20),
    _RuijieWebAuthStaTerminateCause_Type()
)
ruijieWebAuthStaTerminateCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaTerminateCause.setStatus("current")
_RuijieWebAuthStaReplyMessage_Type = DisplayString
_RuijieWebAuthStaReplyMessage_Object = MibScalar
ruijieWebAuthStaReplyMessage = _RuijieWebAuthStaReplyMessage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 21),
    _RuijieWebAuthStaReplyMessage_Type()
)
ruijieWebAuthStaReplyMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaReplyMessage.setStatus("current")
_RuijieWebAuthStaTerminalId_Type = DisplayString
_RuijieWebAuthStaTerminalId_Object = MibScalar
ruijieWebAuthStaTerminalId = _RuijieWebAuthStaTerminalId_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 22),
    _RuijieWebAuthStaTerminalId_Type()
)
ruijieWebAuthStaTerminalId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthStaTerminalId.setStatus("current")


class _RuijieWebAuthType_Type(Integer32):
    """Custom type ruijieWebAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RuijieWebAuthType_Type.__name__ = "Integer32"
_RuijieWebAuthType_Object = MibScalar
ruijieWebAuthType = _RuijieWebAuthType_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 23),
    _RuijieWebAuthType_Type()
)
ruijieWebAuthType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthType.setStatus("current")
_RuijieWebAuthPortIndex_Type = Integer32
_RuijieWebAuthPortIndex_Object = MibScalar
ruijieWebAuthPortIndex = _RuijieWebAuthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 24),
    _RuijieWebAuthPortIndex_Type()
)
ruijieWebAuthPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthPortIndex.setStatus("current")
_RuijieWebAuthTlvNum_Type = Integer32
_RuijieWebAuthTlvNum_Object = MibScalar
ruijieWebAuthTlvNum = _RuijieWebAuthTlvNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 25),
    _RuijieWebAuthTlvNum_Type()
)
ruijieWebAuthTlvNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthTlvNum.setStatus("current")
_RuijieWebAuthTlv_Type = DisplayString
_RuijieWebAuthTlv_Object = MibScalar
ruijieWebAuthTlv = _RuijieWebAuthTlv_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 4, 26),
    _RuijieWebAuthTlv_Type()
)
ruijieWebAuthTlv.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ruijieWebAuthTlv.setStatus("current")

# Managed Objects groups

ruijieWebAuthMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 3, 2, 1)
)
ruijieWebAuthMIBGroup.setObjects(
      *(("RUIJIE-AUTH-GATEWAY-MIB", "authUserIpAddr"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserOnlineFlag"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserTimeLimit"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserTimeUsed"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserStatus"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserRoleName"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserSecZoneName"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserSecZonePermissionType"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserSecZonePermissionList"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserOtherPermissionType"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserTerminateCause"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtAddrType"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtAddr"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtMac"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtIfIndex"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtVlanId"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtOnlineFlag"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtTimeLimit"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtTimeUsed"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtErrCause"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtStatus"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListAddress"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListNetMask"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListPort1"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListPort2"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListPort3"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListPort4"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListPort5"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListPort6"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListPort7"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListPort8"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListBindArpFlag"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthWhiteListStatus"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserVrfg"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserIpAddr"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserOnlineFlag"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserTimeLimit"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserTimeUsed"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserVrf"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserRoleName"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserSecZoneName"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserSecZonePermissionType"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserSecZonePermissionList"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserOtherPermissionType"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserTerminateCause"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserStatus"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectSiteAddress"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectSiteNetMask"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectSiteStatus"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectSiteBindArpFlag"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostAddress"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostNetMask"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostPort1"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostPort2"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostPort3"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostPort4"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostPort5"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostPort6"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostPort7"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostPort8"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostBindArpFlag"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostStatus"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthDirectHostPortIfx"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthFreeAcctIpAddress"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthFreeAcctIpNetMask"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthFreeAcctIpStatus"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthFreeAcctUrl"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthFreeAcctUrlStatus"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthOfflineDetectime"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthOfflineDetectStatus"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthCurrentOnlineUser"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthCurrentUser"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthMaximumOnlineUser"))
)
if mibBuilder.loadTexts:
    ruijieWebAuthMIBGroup.setStatus("current")


# Notification objects

ruijieWebAuthUserLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 2, 1)
)
ruijieWebAuthUserLeave.setObjects(
      *(("RUIJIE-AUTH-GATEWAY-MIB", "authUserIpAddr"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserTimeUsed"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserTerminateCause"))
)
if mibBuilder.loadTexts:
    ruijieWebAuthUserLeave.setStatus(
        "current"
    )

ruijieWebAuthUserExtLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 2, 2)
)
ruijieWebAuthUserExtLeave.setObjects(
      *(("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtAddrType"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtAddr"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtMac"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtIfIndex"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtVlanId"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtTimeUsed"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authUserExtErrCause"))
)
if mibBuilder.loadTexts:
    ruijieWebAuthUserExtLeave.setStatus(
        "current"
    )

ruijieWebAuthSDGUserLeave = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 2, 3)
)
ruijieWebAuthSDGUserLeave.setObjects(
      *(("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserVrfg"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserIpAddr"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserTimeUsed"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "authSDGUserTerminateCause"))
)
if mibBuilder.loadTexts:
    ruijieWebAuthSDGUserLeave.setStatus(
        "current"
    )

ruijieWebAuthWlanMgmt = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 2, 4)
)
ruijieWebAuthWlanMgmt.setObjects(
      *(("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthApMac"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthApIp"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaMac"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaIp"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaIpv6"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaOperType"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaApRadioId"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaApRadioType"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaVlanId"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaWlanId"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthOperTime"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaAssoAuthMode"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaNetAuthMode"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaRssi"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaSsid"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaLinkRate"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaCurChannel"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaUsername"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaTerminalType"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaTerminateCause"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaReplyMessage"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaTerminalId"))
)
if mibBuilder.loadTexts:
    ruijieWebAuthWlanMgmt.setStatus(
        "current"
    )

ruijieWebAuthUserOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 2, 5)
)
ruijieWebAuthUserOper.setObjects(
      *(("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaOperType"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthType"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaUsername"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaIp"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaMac"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaVlanId"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthPortIndex"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthStaTerminateCause"))
)
if mibBuilder.loadTexts:
    ruijieWebAuthUserOper.setStatus(
        "current"
    )

ruijieWebAuthRedirectInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 2, 6)
)
ruijieWebAuthRedirectInfo.setObjects(
      *(("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthTlvNum"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthTlv"))
)
if mibBuilder.loadTexts:
    ruijieWebAuthRedirectInfo.setStatus(
        "current"
    )


# Notifications groups

ruijieWebAuthTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 3, 2, 2)
)
ruijieWebAuthTrapGroup.setObjects(
      *(("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthUserLeave"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthUserExtLeave"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthSDGUserLeave"))
)
if mibBuilder.loadTexts:
    ruijieWebAuthTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijieWebAuthMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 40, 3, 1, 1)
)
ruijieWebAuthMIBCompliance.setObjects(
      *(("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthMIBGroup"),
        ("RUIJIE-AUTH-GATEWAY-MIB", "ruijieWebAuthTrapGroup"))
)
if mibBuilder.loadTexts:
    ruijieWebAuthMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-AUTH-GATEWAY-MIB",
    **{"ruijieWebAuthMIB": ruijieWebAuthMIB,
       "ruijieWebAuthMIBObjects": ruijieWebAuthMIBObjects,
       "ruijieWebAuthUserTable": ruijieWebAuthUserTable,
       "ruijieWebAuthUserEntry": ruijieWebAuthUserEntry,
       "authUserIpAddr": authUserIpAddr,
       "authUserOnlineFlag": authUserOnlineFlag,
       "authUserTimeLimit": authUserTimeLimit,
       "authUserTimeUsed": authUserTimeUsed,
       "authUserStatus": authUserStatus,
       "authUserRoleName": authUserRoleName,
       "authUserSecZoneName": authUserSecZoneName,
       "authUserSecZonePermissionType": authUserSecZonePermissionType,
       "authUserSecZonePermissionList": authUserSecZonePermissionList,
       "authUserOtherPermissionType": authUserOtherPermissionType,
       "authUserTerminateCause": authUserTerminateCause,
       "ruijieWebAuthUserExtTable": ruijieWebAuthUserExtTable,
       "ruijieWebAuthUserExtEntry": ruijieWebAuthUserExtEntry,
       "authUserExtAddrType": authUserExtAddrType,
       "authUserExtAddr": authUserExtAddr,
       "authUserExtMac": authUserExtMac,
       "authUserExtIfIndex": authUserExtIfIndex,
       "authUserExtVlanId": authUserExtVlanId,
       "authUserExtOnlineFlag": authUserExtOnlineFlag,
       "authUserExtTimeLimit": authUserExtTimeLimit,
       "authUserExtTimeUsed": authUserExtTimeUsed,
       "authUserExtErrCause": authUserExtErrCause,
       "authUserExtStatus": authUserExtStatus,
       "ruijieWebAuthWhiteListTable": ruijieWebAuthWhiteListTable,
       "ruijieWebAuthWhiteListEntry": ruijieWebAuthWhiteListEntry,
       "ruijieWebAuthWhiteListAddress": ruijieWebAuthWhiteListAddress,
       "ruijieWebAuthWhiteListNetMask": ruijieWebAuthWhiteListNetMask,
       "ruijieWebAuthWhiteListPort1": ruijieWebAuthWhiteListPort1,
       "ruijieWebAuthWhiteListPort2": ruijieWebAuthWhiteListPort2,
       "ruijieWebAuthWhiteListPort3": ruijieWebAuthWhiteListPort3,
       "ruijieWebAuthWhiteListPort4": ruijieWebAuthWhiteListPort4,
       "ruijieWebAuthWhiteListPort5": ruijieWebAuthWhiteListPort5,
       "ruijieWebAuthWhiteListPort6": ruijieWebAuthWhiteListPort6,
       "ruijieWebAuthWhiteListPort7": ruijieWebAuthWhiteListPort7,
       "ruijieWebAuthWhiteListPort8": ruijieWebAuthWhiteListPort8,
       "ruijieWebAuthWhiteListBindArpFlag": ruijieWebAuthWhiteListBindArpFlag,
       "ruijieWebAuthWhiteListStatus": ruijieWebAuthWhiteListStatus,
       "ruijieWebAuthSDGUserTable": ruijieWebAuthSDGUserTable,
       "ruijieWebAuthSDGUserEntry": ruijieWebAuthSDGUserEntry,
       "authSDGUserVrfg": authSDGUserVrfg,
       "authSDGUserIpAddr": authSDGUserIpAddr,
       "authSDGUserOnlineFlag": authSDGUserOnlineFlag,
       "authSDGUserTimeLimit": authSDGUserTimeLimit,
       "authSDGUserTimeUsed": authSDGUserTimeUsed,
       "authSDGUserVrf": authSDGUserVrf,
       "authSDGUserRoleName": authSDGUserRoleName,
       "authSDGUserSecZoneName": authSDGUserSecZoneName,
       "authSDGUserSecZonePermissionType": authSDGUserSecZonePermissionType,
       "authSDGUserSecZonePermissionList": authSDGUserSecZonePermissionList,
       "authSDGUserOtherPermissionType": authSDGUserOtherPermissionType,
       "authSDGUserTerminateCause": authSDGUserTerminateCause,
       "authSDGUserStatus": authSDGUserStatus,
       "ruijieWebAuthMacUserTable": ruijieWebAuthMacUserTable,
       "ruijieWebAuthMacUserEntry": ruijieWebAuthMacUserEntry,
       "ruijieAuthMacUserMacAddr": ruijieAuthMacUserMacAddr,
       "ruijieAuthMacUserName": ruijieAuthMacUserName,
       "ruijieAuthMacUserTerminalId": ruijieAuthMacUserTerminalId,
       "ruijieWebAuthUserMIB": ruijieWebAuthUserMIB,
       "ruijieWebAuthUserMIBTable": ruijieWebAuthUserMIBTable,
       "ruijieWebAuthUserMIBEntry": ruijieWebAuthUserMIBEntry,
       "ruijieAuthUserMIBIpAddress": ruijieAuthUserMIBIpAddress,
       "ruijieAuthUserMIBName": ruijieAuthUserMIBName,
       "ruijieAuthUserMIBAuthType": ruijieAuthUserMIBAuthType,
       "ruijieAuthUserMIBMacAddress": ruijieAuthUserMIBMacAddress,
       "ruijieAuthUserMIBVlanId": ruijieAuthUserMIBVlanId,
       "ruijieAuthUserMIBPortIndex": ruijieAuthUserMIBPortIndex,
       "ruijieAuthUserMIBTimeUsed": ruijieAuthUserMIBTimeUsed,
       "ruijieWebAuthDirectSiteTable": ruijieWebAuthDirectSiteTable,
       "ruijieWebAuthDirectSiteEntry": ruijieWebAuthDirectSiteEntry,
       "ruijieWebAuthDirectSiteAddress": ruijieWebAuthDirectSiteAddress,
       "ruijieWebAuthDirectSiteNetMask": ruijieWebAuthDirectSiteNetMask,
       "ruijieWebAuthDirectSiteStatus": ruijieWebAuthDirectSiteStatus,
       "ruijieWebAuthDirectSiteBindArpFlag": ruijieWebAuthDirectSiteBindArpFlag,
       "ruijieWebAuthDirectHostTable": ruijieWebAuthDirectHostTable,
       "ruijieWebAuthDirectHostEntry": ruijieWebAuthDirectHostEntry,
       "ruijieWebAuthDirectHostAddress": ruijieWebAuthDirectHostAddress,
       "ruijieWebAuthDirectHostNetMask": ruijieWebAuthDirectHostNetMask,
       "ruijieWebAuthDirectHostPort1": ruijieWebAuthDirectHostPort1,
       "ruijieWebAuthDirectHostPort2": ruijieWebAuthDirectHostPort2,
       "ruijieWebAuthDirectHostPort3": ruijieWebAuthDirectHostPort3,
       "ruijieWebAuthDirectHostPort4": ruijieWebAuthDirectHostPort4,
       "ruijieWebAuthDirectHostPort5": ruijieWebAuthDirectHostPort5,
       "ruijieWebAuthDirectHostPort6": ruijieWebAuthDirectHostPort6,
       "ruijieWebAuthDirectHostPort7": ruijieWebAuthDirectHostPort7,
       "ruijieWebAuthDirectHostPort8": ruijieWebAuthDirectHostPort8,
       "ruijieWebAuthDirectHostBindArpFlag": ruijieWebAuthDirectHostBindArpFlag,
       "ruijieWebAuthDirectHostStatus": ruijieWebAuthDirectHostStatus,
       "ruijieWebAuthDirectHostPortIfx": ruijieWebAuthDirectHostPortIfx,
       "ruijieWebAuthFreeAcctIpTable": ruijieWebAuthFreeAcctIpTable,
       "ruijieWebAuthFreeAcctIpEntry": ruijieWebAuthFreeAcctIpEntry,
       "ruijieWebAuthFreeAcctIpAddress": ruijieWebAuthFreeAcctIpAddress,
       "ruijieWebAuthFreeAcctIpNetMask": ruijieWebAuthFreeAcctIpNetMask,
       "ruijieWebAuthFreeAcctIpStatus": ruijieWebAuthFreeAcctIpStatus,
       "ruijieWebAuthFreeAcctUrlTable": ruijieWebAuthFreeAcctUrlTable,
       "ruijieWebAuthFreeAcctUrlEntry": ruijieWebAuthFreeAcctUrlEntry,
       "ruijieWebAuthFreeAcctUrl": ruijieWebAuthFreeAcctUrl,
       "ruijieWebAuthFreeAcctUrlStatus": ruijieWebAuthFreeAcctUrlStatus,
       "ruijieWebAuthOfflineDetectTable": ruijieWebAuthOfflineDetectTable,
       "ruijieWebAuthOfflineDetectEntry": ruijieWebAuthOfflineDetectEntry,
       "ruijieWebAuthOfflineDetectime": ruijieWebAuthOfflineDetectime,
       "ruijieWebAuthOfflineDetectStatus": ruijieWebAuthOfflineDetectStatus,
       "ruijieWebAuthCurrentOnlineUser": ruijieWebAuthCurrentOnlineUser,
       "ruijieWebAuthCurrentUser": ruijieWebAuthCurrentUser,
       "ruijieWebAuthMaximumOnlineUser": ruijieWebAuthMaximumOnlineUser,
       "ruijieWebAuthMIBTraps": ruijieWebAuthMIBTraps,
       "ruijieWebAuthUserLeave": ruijieWebAuthUserLeave,
       "ruijieWebAuthUserExtLeave": ruijieWebAuthUserExtLeave,
       "ruijieWebAuthSDGUserLeave": ruijieWebAuthSDGUserLeave,
       "ruijieWebAuthWlanMgmt": ruijieWebAuthWlanMgmt,
       "ruijieWebAuthUserOper": ruijieWebAuthUserOper,
       "ruijieWebAuthRedirectInfo": ruijieWebAuthRedirectInfo,
       "ruijieWebAuthMIBConformance": ruijieWebAuthMIBConformance,
       "ruijieWebAuthMIBCompliances": ruijieWebAuthMIBCompliances,
       "ruijieWebAuthMIBCompliance": ruijieWebAuthMIBCompliance,
       "ruijieWebAuthMIBGroups": ruijieWebAuthMIBGroups,
       "ruijieWebAuthMIBGroup": ruijieWebAuthMIBGroup,
       "ruijieWebAuthTrapGroup": ruijieWebAuthTrapGroup,
       "ruijieWebAuthMIBTrapsObjects": ruijieWebAuthMIBTrapsObjects,
       "ruijieWebAuthApMac": ruijieWebAuthApMac,
       "ruijieWebAuthApIp": ruijieWebAuthApIp,
       "ruijieWebAuthStaMac": ruijieWebAuthStaMac,
       "ruijieWebAuthStaIp": ruijieWebAuthStaIp,
       "ruijieWebAuthStaIpv6": ruijieWebAuthStaIpv6,
       "ruijieWebAuthStaOperType": ruijieWebAuthStaOperType,
       "ruijieWebAuthStaApRadioId": ruijieWebAuthStaApRadioId,
       "ruijieWebAuthStaApRadioType": ruijieWebAuthStaApRadioType,
       "ruijieWebAuthStaVlanId": ruijieWebAuthStaVlanId,
       "ruijieWebAuthStaWlanId": ruijieWebAuthStaWlanId,
       "ruijieWebAuthOperTime": ruijieWebAuthOperTime,
       "ruijieWebAuthStaAssoAuthMode": ruijieWebAuthStaAssoAuthMode,
       "ruijieWebAuthStaNetAuthMode": ruijieWebAuthStaNetAuthMode,
       "ruijieWebAuthStaRssi": ruijieWebAuthStaRssi,
       "ruijieWebAuthStaSsid": ruijieWebAuthStaSsid,
       "ruijieWebAuthStaLinkRate": ruijieWebAuthStaLinkRate,
       "ruijieWebAuthStaCurChannel": ruijieWebAuthStaCurChannel,
       "ruijieWebAuthStaUsername": ruijieWebAuthStaUsername,
       "ruijieWebAuthStaTerminalType": ruijieWebAuthStaTerminalType,
       "ruijieWebAuthStaTerminateCause": ruijieWebAuthStaTerminateCause,
       "ruijieWebAuthStaReplyMessage": ruijieWebAuthStaReplyMessage,
       "ruijieWebAuthStaTerminalId": ruijieWebAuthStaTerminalId,
       "ruijieWebAuthType": ruijieWebAuthType,
       "ruijieWebAuthPortIndex": ruijieWebAuthPortIndex,
       "ruijieWebAuthTlvNum": ruijieWebAuthTlvNum,
       "ruijieWebAuthTlv": ruijieWebAuthTlv}
)
