# SNMP MIB module (BELAIR-IP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-IP.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairGeneric,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairGeneric")

(BelAirAdminState,
 BelAirVlanIdOrZero) = mibBuilder.importSymbols(
    "BELAIR-TC",
    "BelAirAdminState",
    "BelAirVlanIdOrZero")

(ifIndex,
 ifPhysAddress) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifPhysAddress")

(ipAdEntIfIndex,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntIfIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

belairIpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2)
)
if mibBuilder.loadTexts:
    belairIpMib.setRevisions(
        ("2009-05-27 11:00",
         "2008-06-10 17:50")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BelairIpMibObjects_ObjectIdentity = ObjectIdentity
belairIpMibObjects = _BelairIpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1)
)
_BaSysConfiguredIpAddress_Type = IpAddress
_BaSysConfiguredIpAddress_Object = MibScalar
baSysConfiguredIpAddress = _BaSysConfiguredIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 1),
    _BaSysConfiguredIpAddress_Type()
)
baSysConfiguredIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baSysConfiguredIpAddress.setStatus("current")
_BaSysConfiguredNetMask_Type = IpAddress
_BaSysConfiguredNetMask_Object = MibScalar
baSysConfiguredNetMask = _BaSysConfiguredNetMask_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 2),
    _BaSysConfiguredNetMask_Type()
)
baSysConfiguredNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baSysConfiguredNetMask.setStatus("current")


class _BaSysConfiguredIpConfigMode_Type(Integer32):
    """Custom type baSysConfiguredIpConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("dhcp", 2))
    )


_BaSysConfiguredIpConfigMode_Type.__name__ = "Integer32"
_BaSysConfiguredIpConfigMode_Object = MibScalar
baSysConfiguredIpConfigMode = _BaSysConfiguredIpConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 3),
    _BaSysConfiguredIpConfigMode_Type()
)
baSysConfiguredIpConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baSysConfiguredIpConfigMode.setStatus("current")
_BelairIfIpTable_Object = MibTable
belairIfIpTable = _BelairIfIpTable_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    belairIfIpTable.setStatus("current")
_BelairIfIpEntry_Object = MibTableRow
belairIfIpEntry = _BelairIfIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 4, 1)
)
belairIfIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    belairIfIpEntry.setStatus("current")


class _BelairIfIpAddrAllocMethod_Type(Integer32):
    """Custom type belairIfIpAddrAllocMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("dhcp", 2))
    )


_BelairIfIpAddrAllocMethod_Type.__name__ = "Integer32"
_BelairIfIpAddrAllocMethod_Object = MibTableColumn
belairIfIpAddrAllocMethod = _BelairIfIpAddrAllocMethod_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 4, 1, 1),
    _BelairIfIpAddrAllocMethod_Type()
)
belairIfIpAddrAllocMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairIfIpAddrAllocMethod.setStatus("current")


class _BelairIfIpAddr_Type(IpAddress):
    """Custom type belairIfIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_BelairIfIpAddr_Type.__name__ = "IpAddress"
_BelairIfIpAddr_Object = MibTableColumn
belairIfIpAddr = _BelairIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 4, 1, 2),
    _BelairIfIpAddr_Type()
)
belairIfIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairIfIpAddr.setStatus("current")
_BelairIfIpSubnetMask_Type = IpAddress
_BelairIfIpSubnetMask_Object = MibTableColumn
belairIfIpSubnetMask = _BelairIfIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 4, 1, 3),
    _BelairIfIpSubnetMask_Type()
)
belairIfIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairIfIpSubnetMask.setStatus("current")
_BelairIfIpVlanId_Type = BelAirVlanIdOrZero
_BelairIfIpVlanId_Object = MibTableColumn
belairIfIpVlanId = _BelairIfIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 4, 1, 4),
    _BelairIfIpVlanId_Type()
)
belairIfIpVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairIfIpVlanId.setStatus("current")


class _BelairIfIpDhcpAction_Type(Integer32):
    """Custom type belairIfIpDhcpAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("renew", 2))
    )


_BelairIfIpDhcpAction_Type.__name__ = "Integer32"
_BelairIfIpDhcpAction_Object = MibTableColumn
belairIfIpDhcpAction = _BelairIfIpDhcpAction_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 4, 1, 5),
    _BelairIfIpDhcpAction_Type()
)
belairIfIpDhcpAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairIfIpDhcpAction.setStatus("current")
_BelairIfIpRowStatus_Type = RowStatus
_BelairIfIpRowStatus_Object = MibTableColumn
belairIfIpRowStatus = _BelairIfIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 4, 1, 6),
    _BelairIfIpRowStatus_Type()
)
belairIfIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    belairIfIpRowStatus.setStatus("current")
_BaIpNotificationAdminState_Type = BelAirAdminState
_BaIpNotificationAdminState_Object = MibScalar
baIpNotificationAdminState = _BaIpNotificationAdminState_Object(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 1, 5),
    _BaIpNotificationAdminState_Type()
)
baIpNotificationAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    baIpNotificationAdminState.setStatus("current")
_BelairIfIpTrapObjects_ObjectIdentity = ObjectIdentity
belairIfIpTrapObjects = _BelairIfIpTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 2)
)
_BelairIfIpTrapV2_ObjectIdentity = ObjectIdentity
belairIfIpTrapV2 = _BelairIfIpTrapV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 2, 0)
)
_BelairIfIpConformance_ObjectIdentity = ObjectIdentity
belairIfIpConformance = _BelairIfIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 3)
)

# Managed Objects groups

belairIfIpObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 3, 1)
)
belairIfIpObjectGroup.setObjects(
      *(("BELAIR-IP", "belairIfIpAddr"),
        ("BELAIR-IP", "belairIfIpSubnetMask"),
        ("BELAIR-IP", "belairIfIpAddrAllocMethod"),
        ("BELAIR-IP", "belairIfIpDhcpAction"),
        ("BELAIR-IP", "belairIfIpVlanId"),
        ("BELAIR-IP", "belairIfIpRowStatus"),
        ("BELAIR-IP", "baSysConfiguredIpConfigMode"),
        ("BELAIR-IP", "baIpNotificationAdminState"),
        ("BELAIR-IP", "baSysConfiguredNetMask"),
        ("BELAIR-IP", "baSysConfiguredIpAddress"))
)
if mibBuilder.loadTexts:
    belairIfIpObjectGroup.setStatus("current")


# Notification objects

belairIpAddressChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 2, 0, 1)
)
belairIpAddressChange.setObjects(
      *(("IP-MIB", "ipAdEntIfIndex"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    belairIpAddressChange.setStatus(
        "current"
    )

belairIpAddressNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 2, 0, 2)
)
belairIpAddressNotification.setObjects(
      *(("IP-MIB", "ipAdEntIfIndex"),
        ("IF-MIB", "ifPhysAddress"))
)
if mibBuilder.loadTexts:
    belairIpAddressNotification.setStatus(
        "current"
    )


# Notifications groups

belairIfIpTrapObjGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 15768, 3, 2, 3, 2)
)
belairIfIpTrapObjGroup.setObjects(
      *(("BELAIR-IP", "belairIpAddressChange"),
        ("BELAIR-IP", "belairIpAddressNotification"))
)
if mibBuilder.loadTexts:
    belairIfIpTrapObjGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-IP",
    **{"belairIpMib": belairIpMib,
       "belairIpMibObjects": belairIpMibObjects,
       "baSysConfiguredIpAddress": baSysConfiguredIpAddress,
       "baSysConfiguredNetMask": baSysConfiguredNetMask,
       "baSysConfiguredIpConfigMode": baSysConfiguredIpConfigMode,
       "belairIfIpTable": belairIfIpTable,
       "belairIfIpEntry": belairIfIpEntry,
       "belairIfIpAddrAllocMethod": belairIfIpAddrAllocMethod,
       "belairIfIpAddr": belairIfIpAddr,
       "belairIfIpSubnetMask": belairIfIpSubnetMask,
       "belairIfIpVlanId": belairIfIpVlanId,
       "belairIfIpDhcpAction": belairIfIpDhcpAction,
       "belairIfIpRowStatus": belairIfIpRowStatus,
       "baIpNotificationAdminState": baIpNotificationAdminState,
       "belairIfIpTrapObjects": belairIfIpTrapObjects,
       "belairIfIpTrapV2": belairIfIpTrapV2,
       "belairIpAddressChange": belairIpAddressChange,
       "belairIpAddressNotification": belairIpAddressNotification,
       "belairIfIpConformance": belairIfIpConformance,
       "belairIfIpObjectGroup": belairIfIpObjectGroup,
       "belairIfIpTrapObjGroup": belairIfIpTrapObjGroup}
)
