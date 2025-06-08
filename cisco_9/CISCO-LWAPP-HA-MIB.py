# SNMP MIB module (CISCO-LWAPP-HA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-HA-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:55:05 2025
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

(cRFStatusPeerUnitState,
 cRFStatusUnitState) = mibBuilder.importSymbols(
    "CISCO-RF-MIB",
    "cRFStatusPeerUnitState",
    "cRFStatusUnitState")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappHaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843)
)
if mibBuilder.loadTexts:
    ciscoLwappHaMIB.setRevisions(
        ("2020-06-07 00:00",
         "2019-07-08 00:00",
         "2017-11-08 00:00",
         "2017-03-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappHaMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappHaMIBNotifs = _CiscoLwappHaMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 0)
)
_CiscoLwappHaMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappHaMIBObjects = _CiscoLwappHaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1)
)
_CiscoLwappHaGlobalConfig_ObjectIdentity = ObjectIdentity
ciscoLwappHaGlobalConfig = _CiscoLwappHaGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1)
)


class _CLHaApSsoConfig_Type(TruthValue):
    """Custom type cLHaApSsoConfig based on TruthValue"""
    defaultValue = 2


_CLHaApSsoConfig_Type.__name__ = "TruthValue"
_CLHaApSsoConfig_Object = MibScalar
cLHaApSsoConfig = _CLHaApSsoConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 1),
    _CLHaApSsoConfig_Type()
)
cLHaApSsoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaApSsoConfig.setStatus("current")
_CLHaPeerIpAddressType_Type = InetAddressType
_CLHaPeerIpAddressType_Object = MibScalar
cLHaPeerIpAddressType = _CLHaPeerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 2),
    _CLHaPeerIpAddressType_Type()
)
cLHaPeerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaPeerIpAddressType.setStatus("current")
_CLHaPeerIpAddress_Type = InetAddress
_CLHaPeerIpAddress_Object = MibScalar
cLHaPeerIpAddress = _CLHaPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 3),
    _CLHaPeerIpAddress_Type()
)
cLHaPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaPeerIpAddress.setStatus("current")
_CLHaServicePortPeerIpAddressType_Type = InetAddressType
_CLHaServicePortPeerIpAddressType_Object = MibScalar
cLHaServicePortPeerIpAddressType = _CLHaServicePortPeerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 4),
    _CLHaServicePortPeerIpAddressType_Type()
)
cLHaServicePortPeerIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaServicePortPeerIpAddressType.setStatus("current")
_CLHaServicePortPeerIpAddress_Type = InetAddress
_CLHaServicePortPeerIpAddress_Object = MibScalar
cLHaServicePortPeerIpAddress = _CLHaServicePortPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 5),
    _CLHaServicePortPeerIpAddress_Type()
)
cLHaServicePortPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaServicePortPeerIpAddress.setStatus("current")
_CLHaServicePortPeerIpNetMaskType_Type = InetAddressType
_CLHaServicePortPeerIpNetMaskType_Object = MibScalar
cLHaServicePortPeerIpNetMaskType = _CLHaServicePortPeerIpNetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 6),
    _CLHaServicePortPeerIpNetMaskType_Type()
)
cLHaServicePortPeerIpNetMaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaServicePortPeerIpNetMaskType.setStatus("current")
_CLHaServicePortPeerIpNetMask_Type = InetAddress
_CLHaServicePortPeerIpNetMask_Object = MibScalar
cLHaServicePortPeerIpNetMask = _CLHaServicePortPeerIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 7),
    _CLHaServicePortPeerIpNetMask_Type()
)
cLHaServicePortPeerIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaServicePortPeerIpNetMask.setStatus("current")
_CLHaRedundancyIpAddressType_Type = InetAddressType
_CLHaRedundancyIpAddressType_Object = MibScalar
cLHaRedundancyIpAddressType = _CLHaRedundancyIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 8),
    _CLHaRedundancyIpAddressType_Type()
)
cLHaRedundancyIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaRedundancyIpAddressType.setStatus("current")
_CLHaRedundancyIpAddress_Type = InetAddress
_CLHaRedundancyIpAddress_Object = MibScalar
cLHaRedundancyIpAddress = _CLHaRedundancyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 9),
    _CLHaRedundancyIpAddress_Type()
)
cLHaRedundancyIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaRedundancyIpAddress.setStatus("current")
_CLHaPeerMacAddress_Type = MacAddress
_CLHaPeerMacAddress_Object = MibScalar
cLHaPeerMacAddress = _CLHaPeerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 10),
    _CLHaPeerMacAddress_Type()
)
cLHaPeerMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaPeerMacAddress.setStatus("current")
_CLHaVirtualMacAddress_Type = MacAddress
_CLHaVirtualMacAddress_Object = MibScalar
cLHaVirtualMacAddress = _CLHaVirtualMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 11),
    _CLHaVirtualMacAddress_Type()
)
cLHaVirtualMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaVirtualMacAddress.setStatus("current")


class _CLHaPrimaryUnit_Type(TruthValue):
    """Custom type cLHaPrimaryUnit based on TruthValue"""
    defaultValue = 2


_CLHaPrimaryUnit_Type.__name__ = "TruthValue"
_CLHaPrimaryUnit_Object = MibScalar
cLHaPrimaryUnit = _CLHaPrimaryUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 12),
    _CLHaPrimaryUnit_Type()
)
cLHaPrimaryUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaPrimaryUnit.setStatus("current")


class _CLHaLinkEncryption_Type(TruthValue):
    """Custom type cLHaLinkEncryption based on TruthValue"""
    defaultValue = 2


_CLHaLinkEncryption_Type.__name__ = "TruthValue"
_CLHaLinkEncryption_Object = MibScalar
cLHaLinkEncryption = _CLHaLinkEncryption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 13),
    _CLHaLinkEncryption_Type()
)
cLHaLinkEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaLinkEncryption.setStatus("current")


class _CLHaNetworkFailOver_Type(TruthValue):
    """Custom type cLHaNetworkFailOver based on TruthValue"""
    defaultValue = 2


_CLHaNetworkFailOver_Type.__name__ = "TruthValue"
_CLHaNetworkFailOver_Object = MibScalar
cLHaNetworkFailOver = _CLHaNetworkFailOver_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 14),
    _CLHaNetworkFailOver_Type()
)
cLHaNetworkFailOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaNetworkFailOver.setStatus("current")
_CLHaRFStatusUnitIp_Type = InetAddress
_CLHaRFStatusUnitIp_Object = MibScalar
cLHaRFStatusUnitIp = _CLHaRFStatusUnitIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 15),
    _CLHaRFStatusUnitIp_Type()
)
cLHaRFStatusUnitIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaRFStatusUnitIp.setStatus("current")


class _CLHaKATimeout_Type(Unsigned32):
    """Custom type cLHaKATimeout based on Unsigned32"""
    defaultValue = 100


_CLHaKATimeout_Type.__name__ = "Unsigned32"
_CLHaKATimeout_Object = MibScalar
cLHaKATimeout = _CLHaKATimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 16),
    _CLHaKATimeout_Type()
)
cLHaKATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaKATimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLHaKATimeout.setUnits("milliseconds")


class _CLHaKARetryCount_Type(Unsigned32):
    """Custom type cLHaKARetryCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_CLHaKARetryCount_Type.__name__ = "Unsigned32"
_CLHaKARetryCount_Object = MibScalar
cLHaKARetryCount = _CLHaKARetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 17),
    _CLHaKARetryCount_Type()
)
cLHaKARetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaKARetryCount.setStatus("current")


class _CLHaGwRetryCount_Type(Unsigned32):
    """Custom type cLHaGwRetryCount based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 12),
    )


_CLHaGwRetryCount_Type.__name__ = "Unsigned32"
_CLHaGwRetryCount_Object = MibScalar
cLHaGwRetryCount = _CLHaGwRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 18),
    _CLHaGwRetryCount_Type()
)
cLHaGwRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaGwRetryCount.setStatus("current")


class _CLHaPeerSearchTimeout_Type(Unsigned32):
    """Custom type cLHaPeerSearchTimeout based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_CLHaPeerSearchTimeout_Type.__name__ = "Unsigned32"
_CLHaPeerSearchTimeout_Object = MibScalar
cLHaPeerSearchTimeout = _CLHaPeerSearchTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 19),
    _CLHaPeerSearchTimeout_Type()
)
cLHaPeerSearchTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLHaPeerSearchTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cLHaPeerSearchTimeout.setUnits("seconds")
_CLHaRFStatusUnitIpType_Type = InetAddressType
_CLHaRFStatusUnitIpType_Object = MibScalar
cLHaRFStatusUnitIpType = _CLHaRFStatusUnitIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 1, 20),
    _CLHaRFStatusUnitIpType_Type()
)
cLHaRFStatusUnitIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaRFStatusUnitIpType.setStatus("current")
_CiscoLwappHaNetworkConfig_ObjectIdentity = ObjectIdentity
ciscoLwappHaNetworkConfig = _CiscoLwappHaNetworkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 2)
)
_CLHaNetworkRoutePeerConfigTable_Object = MibTable
cLHaNetworkRoutePeerConfigTable = _CLHaNetworkRoutePeerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerConfigTable.setStatus("current")
_CLHaNetworkRoutePeerConfigEntry_Object = MibTableRow
cLHaNetworkRoutePeerConfigEntry = _CLHaNetworkRoutePeerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 2, 1, 1)
)
cLHaNetworkRoutePeerConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-HA-MIB", "cLHaNetworkRoutePeerIPAddressType"),
    (0, "CISCO-LWAPP-HA-MIB", "cLHaNetworkRoutePeerIPAddress"),
)
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerConfigEntry.setStatus("current")
_CLHaNetworkRoutePeerIPAddressType_Type = InetAddressType
_CLHaNetworkRoutePeerIPAddressType_Object = MibTableColumn
cLHaNetworkRoutePeerIPAddressType = _CLHaNetworkRoutePeerIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 2, 1, 1, 1),
    _CLHaNetworkRoutePeerIPAddressType_Type()
)
cLHaNetworkRoutePeerIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerIPAddressType.setStatus("current")
_CLHaNetworkRoutePeerIPAddress_Type = InetAddress
_CLHaNetworkRoutePeerIPAddress_Object = MibTableColumn
cLHaNetworkRoutePeerIPAddress = _CLHaNetworkRoutePeerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 2, 1, 1, 2),
    _CLHaNetworkRoutePeerIPAddress_Type()
)
cLHaNetworkRoutePeerIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerIPAddress.setStatus("current")
_CLHaNetworkRoutePeerIPNetmaskType_Type = InetAddressType
_CLHaNetworkRoutePeerIPNetmaskType_Object = MibTableColumn
cLHaNetworkRoutePeerIPNetmaskType = _CLHaNetworkRoutePeerIPNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 2, 1, 1, 3),
    _CLHaNetworkRoutePeerIPNetmaskType_Type()
)
cLHaNetworkRoutePeerIPNetmaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerIPNetmaskType.setStatus("current")
_CLHaNetworkRoutePeerIPNetmask_Type = InetAddress
_CLHaNetworkRoutePeerIPNetmask_Object = MibTableColumn
cLHaNetworkRoutePeerIPNetmask = _CLHaNetworkRoutePeerIPNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 2, 1, 1, 4),
    _CLHaNetworkRoutePeerIPNetmask_Type()
)
cLHaNetworkRoutePeerIPNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerIPNetmask.setStatus("current")
_CLHaNetworkRoutePeerGatewayType_Type = InetAddressType
_CLHaNetworkRoutePeerGatewayType_Object = MibTableColumn
cLHaNetworkRoutePeerGatewayType = _CLHaNetworkRoutePeerGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 2, 1, 1, 5),
    _CLHaNetworkRoutePeerGatewayType_Type()
)
cLHaNetworkRoutePeerGatewayType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerGatewayType.setStatus("current")
_CLHaNetworkRoutePeerGateway_Type = InetAddress
_CLHaNetworkRoutePeerGateway_Object = MibTableColumn
cLHaNetworkRoutePeerGateway = _CLHaNetworkRoutePeerGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 2, 1, 1, 6),
    _CLHaNetworkRoutePeerGateway_Type()
)
cLHaNetworkRoutePeerGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerGateway.setStatus("current")


class _CLHaNetworkRoutePeerTransferStatus_Type(Integer32):
    """Custom type cLHaNetworkRoutePeerTransferStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("initiate", 1),
          ("inProgress", 2),
          ("success", 3),
          ("failure", 4),
          ("timeout", 5))
    )


_CLHaNetworkRoutePeerTransferStatus_Type.__name__ = "Integer32"
_CLHaNetworkRoutePeerTransferStatus_Object = MibTableColumn
cLHaNetworkRoutePeerTransferStatus = _CLHaNetworkRoutePeerTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 2, 1, 1, 7),
    _CLHaNetworkRoutePeerTransferStatus_Type()
)
cLHaNetworkRoutePeerTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerTransferStatus.setStatus("current")
_CLHaNetworkRoutePeerRowStatus_Type = RowStatus
_CLHaNetworkRoutePeerRowStatus_Object = MibTableColumn
cLHaNetworkRoutePeerRowStatus = _CLHaNetworkRoutePeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 2, 1, 1, 8),
    _CLHaNetworkRoutePeerRowStatus_Type()
)
cLHaNetworkRoutePeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLHaNetworkRoutePeerRowStatus.setStatus("current")
_CiscoLwappHaNotificationVariable_ObjectIdentity = ObjectIdentity
ciscoLwappHaNotificationVariable = _CiscoLwappHaNotificationVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 3)
)


class _CLHaSecondaryControllerUsageTrapType_Type(Integer32):
    """Custom type cLHaSecondaryControllerUsageTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("usageStart", 1),
          ("usageComplete", 2),
          ("overUsage", 3))
    )


_CLHaSecondaryControllerUsageTrapType_Type.__name__ = "Integer32"
_CLHaSecondaryControllerUsageTrapType_Object = MibScalar
cLHaSecondaryControllerUsageTrapType = _CLHaSecondaryControllerUsageTrapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 3, 1),
    _CLHaSecondaryControllerUsageTrapType_Type()
)
cLHaSecondaryControllerUsageTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaSecondaryControllerUsageTrapType.setStatus("current")
_CLHaSecondaryControllerUsageDayCounter_Type = Counter32
_CLHaSecondaryControllerUsageDayCounter_Object = MibScalar
cLHaSecondaryControllerUsageDayCounter = _CLHaSecondaryControllerUsageDayCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 3, 2),
    _CLHaSecondaryControllerUsageDayCounter_Type()
)
cLHaSecondaryControllerUsageDayCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaSecondaryControllerUsageDayCounter.setStatus("current")


class _CLHaBulkSyncCompleteEvent_Type(Integer32):
    """Custom type cLHaBulkSyncCompleteEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bulkSyncComplete", 1)
    )


_CLHaBulkSyncCompleteEvent_Type.__name__ = "Integer32"
_CLHaBulkSyncCompleteEvent_Object = MibScalar
cLHaBulkSyncCompleteEvent = _CLHaBulkSyncCompleteEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 3, 3),
    _CLHaBulkSyncCompleteEvent_Type()
)
cLHaBulkSyncCompleteEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaBulkSyncCompleteEvent.setStatus("current")


class _CLHaPeerHotStandbyEvent_Type(Integer32):
    """Custom type cLHaPeerHotStandbyEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("haPeerHotstandby", 1)
    )


_CLHaPeerHotStandbyEvent_Type.__name__ = "Integer32"
_CLHaPeerHotStandbyEvent_Object = MibScalar
cLHaPeerHotStandbyEvent = _CLHaPeerHotStandbyEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 3, 4),
    _CLHaPeerHotStandbyEvent_Type()
)
cLHaPeerHotStandbyEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaPeerHotStandbyEvent.setStatus("current")
_CiscoLwappHaPeerStatisticsVariable_ObjectIdentity = ObjectIdentity
ciscoLwappHaPeerStatisticsVariable = _CiscoLwappHaPeerStatisticsVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4)
)
_CiscoLwappHaSystemStatistics_ObjectIdentity = ObjectIdentity
ciscoLwappHaSystemStatistics = _CiscoLwappHaSystemStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1)
)
_CiscoLwappHaCpuStatistics_ObjectIdentity = ObjectIdentity
ciscoLwappHaCpuStatistics = _CiscoLwappHaCpuStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 1)
)


class _CLHaAllCpuUsage_Type(SnmpAdminString):
    """Custom type cLHaAllCpuUsage based on SnmpAdminString"""
    defaultValue = OctetString("")


_CLHaAllCpuUsage_Type.__name__ = "SnmpAdminString"
_CLHaAllCpuUsage_Object = MibScalar
cLHaAllCpuUsage = _CLHaAllCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 1, 1),
    _CLHaAllCpuUsage_Type()
)
cLHaAllCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaAllCpuUsage.setStatus("current")
_CiscoLwappHaPowerSupplyStatistics_ObjectIdentity = ObjectIdentity
ciscoLwappHaPowerSupplyStatistics = _CiscoLwappHaPowerSupplyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 2)
)


class _CLHaPowerSupply1Present_Type(TruthValue):
    """Custom type cLHaPowerSupply1Present based on TruthValue"""
    defaultValue = 2


_CLHaPowerSupply1Present_Type.__name__ = "TruthValue"
_CLHaPowerSupply1Present_Object = MibScalar
cLHaPowerSupply1Present = _CLHaPowerSupply1Present_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 2, 1),
    _CLHaPowerSupply1Present_Type()
)
cLHaPowerSupply1Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaPowerSupply1Present.setStatus("current")


class _CLHaPowerSupply1Operational_Type(TruthValue):
    """Custom type cLHaPowerSupply1Operational based on TruthValue"""
    defaultValue = 2


_CLHaPowerSupply1Operational_Type.__name__ = "TruthValue"
_CLHaPowerSupply1Operational_Object = MibScalar
cLHaPowerSupply1Operational = _CLHaPowerSupply1Operational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 2, 2),
    _CLHaPowerSupply1Operational_Type()
)
cLHaPowerSupply1Operational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaPowerSupply1Operational.setStatus("current")


class _CLHaPowerSupply2Present_Type(TruthValue):
    """Custom type cLHaPowerSupply2Present based on TruthValue"""
    defaultValue = 2


_CLHaPowerSupply2Present_Type.__name__ = "TruthValue"
_CLHaPowerSupply2Present_Object = MibScalar
cLHaPowerSupply2Present = _CLHaPowerSupply2Present_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 2, 3),
    _CLHaPowerSupply2Present_Type()
)
cLHaPowerSupply2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaPowerSupply2Present.setStatus("current")


class _CLHaPowerSupply2Operational_Type(TruthValue):
    """Custom type cLHaPowerSupply2Operational based on TruthValue"""
    defaultValue = 2


_CLHaPowerSupply2Operational_Type.__name__ = "TruthValue"
_CLHaPowerSupply2Operational_Object = MibScalar
cLHaPowerSupply2Operational = _CLHaPowerSupply2Operational_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 2, 4),
    _CLHaPowerSupply2Operational_Type()
)
cLHaPowerSupply2Operational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaPowerSupply2Operational.setStatus("current")
_CiscoLwappHaMemoryStatistics_ObjectIdentity = ObjectIdentity
ciscoLwappHaMemoryStatistics = _CiscoLwappHaMemoryStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3)
)


class _CLHaTotalSystemMemory_Type(Integer32):
    """Custom type cLHaTotalSystemMemory based on Integer32"""
    defaultValue = 0


_CLHaTotalSystemMemory_Type.__name__ = "Integer32"
_CLHaTotalSystemMemory_Object = MibScalar
cLHaTotalSystemMemory = _CLHaTotalSystemMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 1),
    _CLHaTotalSystemMemory_Type()
)
cLHaTotalSystemMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaTotalSystemMemory.setStatus("current")
if mibBuilder.loadTexts:
    cLHaTotalSystemMemory.setUnits("KBytes")


class _CLHaFreeSystemMemory_Type(Integer32):
    """Custom type cLHaFreeSystemMemory based on Integer32"""
    defaultValue = 0


_CLHaFreeSystemMemory_Type.__name__ = "Integer32"
_CLHaFreeSystemMemory_Object = MibScalar
cLHaFreeSystemMemory = _CLHaFreeSystemMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 2),
    _CLHaFreeSystemMemory_Type()
)
cLHaFreeSystemMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaFreeSystemMemory.setStatus("current")
if mibBuilder.loadTexts:
    cLHaFreeSystemMemory.setUnits("KBytes")


class _CLHaUsedSystemMemory_Type(Integer32):
    """Custom type cLHaUsedSystemMemory based on Integer32"""
    defaultValue = 0


_CLHaUsedSystemMemory_Type.__name__ = "Integer32"
_CLHaUsedSystemMemory_Object = MibScalar
cLHaUsedSystemMemory = _CLHaUsedSystemMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 3),
    _CLHaUsedSystemMemory_Type()
)
cLHaUsedSystemMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaUsedSystemMemory.setStatus("current")
if mibBuilder.loadTexts:
    cLHaUsedSystemMemory.setUnits("KBytes")


class _CLHaAllocatedFromRtos_Type(Integer32):
    """Custom type cLHaAllocatedFromRtos based on Integer32"""
    defaultValue = 0


_CLHaAllocatedFromRtos_Type.__name__ = "Integer32"
_CLHaAllocatedFromRtos_Object = MibScalar
cLHaAllocatedFromRtos = _CLHaAllocatedFromRtos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 4),
    _CLHaAllocatedFromRtos_Type()
)
cLHaAllocatedFromRtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaAllocatedFromRtos.setStatus("current")
if mibBuilder.loadTexts:
    cLHaAllocatedFromRtos.setUnits("KBytes")


class _CLHaChunksFree_Type(Integer32):
    """Custom type cLHaChunksFree based on Integer32"""
    defaultValue = 0


_CLHaChunksFree_Type.__name__ = "Integer32"
_CLHaChunksFree_Object = MibScalar
cLHaChunksFree = _CLHaChunksFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 5),
    _CLHaChunksFree_Type()
)
cLHaChunksFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaChunksFree.setStatus("current")


class _CLHaMmappedRegions_Type(Integer32):
    """Custom type cLHaMmappedRegions based on Integer32"""
    defaultValue = 0


_CLHaMmappedRegions_Type.__name__ = "Integer32"
_CLHaMmappedRegions_Object = MibScalar
cLHaMmappedRegions = _CLHaMmappedRegions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 6),
    _CLHaMmappedRegions_Type()
)
cLHaMmappedRegions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaMmappedRegions.setStatus("current")


class _CLHaSpaceInMmappedRegions_Type(Integer32):
    """Custom type cLHaSpaceInMmappedRegions based on Integer32"""
    defaultValue = 0


_CLHaSpaceInMmappedRegions_Type.__name__ = "Integer32"
_CLHaSpaceInMmappedRegions_Object = MibScalar
cLHaSpaceInMmappedRegions = _CLHaSpaceInMmappedRegions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 7),
    _CLHaSpaceInMmappedRegions_Type()
)
cLHaSpaceInMmappedRegions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaSpaceInMmappedRegions.setStatus("current")
if mibBuilder.loadTexts:
    cLHaSpaceInMmappedRegions.setUnits("KBytes")


class _CLHaTotalAllocatedSpace_Type(Integer32):
    """Custom type cLHaTotalAllocatedSpace based on Integer32"""
    defaultValue = 0


_CLHaTotalAllocatedSpace_Type.__name__ = "Integer32"
_CLHaTotalAllocatedSpace_Object = MibScalar
cLHaTotalAllocatedSpace = _CLHaTotalAllocatedSpace_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 8),
    _CLHaTotalAllocatedSpace_Type()
)
cLHaTotalAllocatedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaTotalAllocatedSpace.setStatus("current")
if mibBuilder.loadTexts:
    cLHaTotalAllocatedSpace.setUnits("KBytes")


class _CLHaTotalNotInUseSpace_Type(Integer32):
    """Custom type cLHaTotalNotInUseSpace based on Integer32"""
    defaultValue = 0


_CLHaTotalNotInUseSpace_Type.__name__ = "Integer32"
_CLHaTotalNotInUseSpace_Object = MibScalar
cLHaTotalNotInUseSpace = _CLHaTotalNotInUseSpace_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 9),
    _CLHaTotalNotInUseSpace_Type()
)
cLHaTotalNotInUseSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaTotalNotInUseSpace.setStatus("current")
if mibBuilder.loadTexts:
    cLHaTotalNotInUseSpace.setUnits("KBytes")


class _CLHaTopMostReleasableSpace_Type(Integer32):
    """Custom type cLHaTopMostReleasableSpace based on Integer32"""
    defaultValue = 0


_CLHaTopMostReleasableSpace_Type.__name__ = "Integer32"
_CLHaTopMostReleasableSpace_Object = MibScalar
cLHaTopMostReleasableSpace = _CLHaTopMostReleasableSpace_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 10),
    _CLHaTopMostReleasableSpace_Type()
)
cLHaTopMostReleasableSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaTopMostReleasableSpace.setStatus("current")
if mibBuilder.loadTexts:
    cLHaTopMostReleasableSpace.setUnits("KBytes")


class _CLHaTotalAllocatedInclMmap_Type(Integer32):
    """Custom type cLHaTotalAllocatedInclMmap based on Integer32"""
    defaultValue = 0


_CLHaTotalAllocatedInclMmap_Type.__name__ = "Integer32"
_CLHaTotalAllocatedInclMmap_Object = MibScalar
cLHaTotalAllocatedInclMmap = _CLHaTotalAllocatedInclMmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 11),
    _CLHaTotalAllocatedInclMmap_Type()
)
cLHaTotalAllocatedInclMmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaTotalAllocatedInclMmap.setStatus("current")
if mibBuilder.loadTexts:
    cLHaTotalAllocatedInclMmap.setUnits("KBytes")


class _CLHaTotalUsedMmap_Type(Integer32):
    """Custom type cLHaTotalUsedMmap based on Integer32"""
    defaultValue = 0


_CLHaTotalUsedMmap_Type.__name__ = "Integer32"
_CLHaTotalUsedMmap_Object = MibScalar
cLHaTotalUsedMmap = _CLHaTotalUsedMmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 12),
    _CLHaTotalUsedMmap_Type()
)
cLHaTotalUsedMmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaTotalUsedMmap.setStatus("current")
if mibBuilder.loadTexts:
    cLHaTotalUsedMmap.setUnits("KBytes")


class _CLHaTotalFreeInclMmap_Type(Integer32):
    """Custom type cLHaTotalFreeInclMmap based on Integer32"""
    defaultValue = 0


_CLHaTotalFreeInclMmap_Type.__name__ = "Integer32"
_CLHaTotalFreeInclMmap_Object = MibScalar
cLHaTotalFreeInclMmap = _CLHaTotalFreeInclMmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 4, 1, 3, 13),
    _CLHaTotalFreeInclMmap_Type()
)
cLHaTotalFreeInclMmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaTotalFreeInclMmap.setStatus("current")
if mibBuilder.loadTexts:
    cLHaTotalFreeInclMmap.setUnits("KBytes")
_CiscoLwappHaStatisticsVariable_ObjectIdentity = ObjectIdentity
ciscoLwappHaStatisticsVariable = _CiscoLwappHaStatisticsVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 5)
)


class _CLHaAvgPeerReachLatency_Type(Integer32):
    """Custom type cLHaAvgPeerReachLatency based on Integer32"""
    defaultValue = 0


_CLHaAvgPeerReachLatency_Type.__name__ = "Integer32"
_CLHaAvgPeerReachLatency_Object = MibScalar
cLHaAvgPeerReachLatency = _CLHaAvgPeerReachLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 5, 1),
    _CLHaAvgPeerReachLatency_Type()
)
cLHaAvgPeerReachLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaAvgPeerReachLatency.setStatus("current")
if mibBuilder.loadTexts:
    cLHaAvgPeerReachLatency.setUnits("Microseconds")


class _CLHaAvgGwReachLatency_Type(Integer32):
    """Custom type cLHaAvgGwReachLatency based on Integer32"""
    defaultValue = 0


_CLHaAvgGwReachLatency_Type.__name__ = "Integer32"
_CLHaAvgGwReachLatency_Object = MibScalar
cLHaAvgGwReachLatency = _CLHaAvgGwReachLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 5, 2),
    _CLHaAvgGwReachLatency_Type()
)
cLHaAvgGwReachLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaAvgGwReachLatency.setStatus("current")
if mibBuilder.loadTexts:
    cLHaAvgGwReachLatency.setUnits("Microseconds")


class _CLHaBulkSyncStatus_Type(SnmpAdminString):
    """Custom type cLHaBulkSyncStatus based on SnmpAdminString"""
    defaultValue = OctetString("")


_CLHaBulkSyncStatus_Type.__name__ = "SnmpAdminString"
_CLHaBulkSyncStatus_Object = MibScalar
cLHaBulkSyncStatus = _CLHaBulkSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 5, 3),
    _CLHaBulkSyncStatus_Type()
)
cLHaBulkSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLHaBulkSyncStatus.setStatus("current")
_CiscoLwappMcHaConfig_ObjectIdentity = ObjectIdentity
ciscoLwappMcHaConfig = _CiscoLwappMcHaConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 6)
)
_CLMcHaPortName_Type = DisplayString
_CLMcHaPortName_Object = MibScalar
cLMcHaPortName = _CLMcHaPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 6, 1),
    _CLMcHaPortName_Type()
)
cLMcHaPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcHaPortName.setStatus("current")
_CLMcHaPortLocIpAddrType_Type = InetAddressType
_CLMcHaPortLocIpAddrType_Object = MibScalar
cLMcHaPortLocIpAddrType = _CLMcHaPortLocIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 6, 2),
    _CLMcHaPortLocIpAddrType_Type()
)
cLMcHaPortLocIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcHaPortLocIpAddrType.setStatus("current")
_CLMcHaPortLocIp_Type = InetAddress
_CLMcHaPortLocIp_Object = MibScalar
cLMcHaPortLocIp = _CLMcHaPortLocIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 6, 3),
    _CLMcHaPortLocIp_Type()
)
cLMcHaPortLocIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcHaPortLocIp.setStatus("current")
_CLMcHaPortMask_Type = InetAddress
_CLMcHaPortMask_Object = MibScalar
cLMcHaPortMask = _CLMcHaPortMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 6, 4),
    _CLMcHaPortMask_Type()
)
cLMcHaPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcHaPortMask.setStatus("current")
_CLMcHaPortRemoteIpAddrType_Type = InetAddressType
_CLMcHaPortRemoteIpAddrType_Object = MibScalar
cLMcHaPortRemoteIpAddrType = _CLMcHaPortRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 6, 5),
    _CLMcHaPortRemoteIpAddrType_Type()
)
cLMcHaPortRemoteIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcHaPortRemoteIpAddrType.setStatus("current")
_CLMcHaPortRemIp_Type = InetAddress
_CLMcHaPortRemIp_Object = MibScalar
cLMcHaPortRemIp = _CLMcHaPortRemIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 6, 6),
    _CLMcHaPortRemIp_Type()
)
cLMcHaPortRemIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcHaPortRemIp.setStatus("current")


class _CLMcHaKeepAliveTimeOut_Type(Unsigned32):
    """Custom type cLMcHaKeepAliveTimeOut based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CLMcHaKeepAliveTimeOut_Type.__name__ = "Unsigned32"
_CLMcHaKeepAliveTimeOut_Object = MibScalar
cLMcHaKeepAliveTimeOut = _CLMcHaKeepAliveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 6, 7),
    _CLMcHaKeepAliveTimeOut_Type()
)
cLMcHaKeepAliveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcHaKeepAliveTimeOut.setStatus("current")


class _CLMcHaChassisPriority_Type(Unsigned32):
    """Custom type cLMcHaChassisPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CLMcHaChassisPriority_Type.__name__ = "Unsigned32"
_CLMcHaChassisPriority_Object = MibScalar
cLMcHaChassisPriority = _CLMcHaChassisPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 6, 8),
    _CLMcHaChassisPriority_Type()
)
cLMcHaChassisPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcHaChassisPriority.setStatus("current")


class _CLMcHaClearConfig_Type(TruthValue):
    """Custom type cLMcHaClearConfig based on TruthValue"""
    defaultValue = 2


_CLMcHaClearConfig_Type.__name__ = "TruthValue"
_CLMcHaClearConfig_Object = MibScalar
cLMcHaClearConfig = _CLMcHaClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 6, 9),
    _CLMcHaClearConfig_Type()
)
cLMcHaClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcHaClearConfig.setStatus("current")


class _CLMcHaKeepAliveRetryCount_Type(Unsigned32):
    """Custom type cLMcHaKeepAliveRetryCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_CLMcHaKeepAliveRetryCount_Type.__name__ = "Unsigned32"
_CLMcHaKeepAliveRetryCount_Object = MibScalar
cLMcHaKeepAliveRetryCount = _CLMcHaKeepAliveRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 6, 10),
    _CLMcHaKeepAliveRetryCount_Type()
)
cLMcHaKeepAliveRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcHaKeepAliveRetryCount.setStatus("current")
_CiscoLwappMcRmiConfig_ObjectIdentity = ObjectIdentity
ciscoLwappMcRmiConfig = _CiscoLwappMcRmiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 7)
)


class _CLMcRmiConfigAction_Type(Unsigned32):
    """Custom type cLMcRmiConfigAction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CLMcRmiConfigAction_Type.__name__ = "Unsigned32"
_CLMcRmiConfigAction_Object = MibScalar
cLMcRmiConfigAction = _CLMcRmiConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 7, 1),
    _CLMcRmiConfigAction_Type()
)
cLMcRmiConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcRmiConfigAction.setStatus("current")
_CLMcRmiInterface_Type = SnmpAdminString
_CLMcRmiInterface_Object = MibScalar
cLMcRmiInterface = _CLMcRmiInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 7, 2),
    _CLMcRmiInterface_Type()
)
cLMcRmiInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcRmiInterface.setStatus("current")


class _CLMcRmiChassisANum_Type(Unsigned32):
    """Custom type cLMcRmiChassisANum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CLMcRmiChassisANum_Type.__name__ = "Unsigned32"
_CLMcRmiChassisANum_Object = MibScalar
cLMcRmiChassisANum = _CLMcRmiChassisANum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 7, 3),
    _CLMcRmiChassisANum_Type()
)
cLMcRmiChassisANum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcRmiChassisANum.setStatus("current")
_CLMcRmiChassisAIpAddrType_Type = InetAddressType
_CLMcRmiChassisAIpAddrType_Object = MibScalar
cLMcRmiChassisAIpAddrType = _CLMcRmiChassisAIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 7, 4),
    _CLMcRmiChassisAIpAddrType_Type()
)
cLMcRmiChassisAIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcRmiChassisAIpAddrType.setStatus("current")
_CLMcRmiChassisAIp_Type = InetAddress
_CLMcRmiChassisAIp_Object = MibScalar
cLMcRmiChassisAIp = _CLMcRmiChassisAIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 7, 5),
    _CLMcRmiChassisAIp_Type()
)
cLMcRmiChassisAIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcRmiChassisAIp.setStatus("current")


class _CLMcRmiChassisBNum_Type(Unsigned32):
    """Custom type cLMcRmiChassisBNum based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CLMcRmiChassisBNum_Type.__name__ = "Unsigned32"
_CLMcRmiChassisBNum_Object = MibScalar
cLMcRmiChassisBNum = _CLMcRmiChassisBNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 7, 6),
    _CLMcRmiChassisBNum_Type()
)
cLMcRmiChassisBNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcRmiChassisBNum.setStatus("current")
_CLMcRmiChassisBIpAddrType_Type = InetAddressType
_CLMcRmiChassisBIpAddrType_Object = MibScalar
cLMcRmiChassisBIpAddrType = _CLMcRmiChassisBIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 7, 7),
    _CLMcRmiChassisBIpAddrType_Type()
)
cLMcRmiChassisBIpAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcRmiChassisBIpAddrType.setStatus("current")
_CLMcRmiChassisBIp_Type = InetAddress
_CLMcRmiChassisBIp_Object = MibScalar
cLMcRmiChassisBIp = _CLMcRmiChassisBIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 7, 8),
    _CLMcRmiChassisBIp_Type()
)
cLMcRmiChassisBIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcRmiChassisBIp.setStatus("current")


class _CLMcRmiGatewayFailover_Type(TruthValue):
    """Custom type cLMcRmiGatewayFailover based on TruthValue"""
    defaultValue = 1


_CLMcRmiGatewayFailover_Type.__name__ = "TruthValue"
_CLMcRmiGatewayFailover_Object = MibScalar
cLMcRmiGatewayFailover = _CLMcRmiGatewayFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 7, 9),
    _CLMcRmiGatewayFailover_Type()
)
cLMcRmiGatewayFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcRmiGatewayFailover.setStatus("current")


class _CLMcRmiGatewayFailoverInterval_Type(Unsigned32):
    """Custom type cLMcRmiGatewayFailoverInterval based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 12),
    )


_CLMcRmiGatewayFailoverInterval_Type.__name__ = "Unsigned32"
_CLMcRmiGatewayFailoverInterval_Object = MibScalar
cLMcRmiGatewayFailoverInterval = _CLMcRmiGatewayFailoverInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 1, 7, 10),
    _CLMcRmiGatewayFailoverInterval_Type()
)
cLMcRmiGatewayFailoverInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMcRmiGatewayFailoverInterval.setStatus("current")
_CiscoLwappHaMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappHaMIBConform = _CiscoLwappHaMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2)
)
_CiscoLwappHaMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappHaMIBCompliances = _CiscoLwappHaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2, 1)
)
_CiscoLwappHaMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappHaMIBGroups = _CiscoLwappHaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2, 2)
)

# Managed Objects groups

ciscoLwappHaGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2, 2, 1)
)
ciscoLwappHaGlobalConfigGroup.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "cLHaApSsoConfig"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPeerIpAddressType"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPeerIpAddress"),
        ("CISCO-LWAPP-HA-MIB", "cLHaServicePortPeerIpAddressType"),
        ("CISCO-LWAPP-HA-MIB", "cLHaServicePortPeerIpAddress"),
        ("CISCO-LWAPP-HA-MIB", "cLHaServicePortPeerIpNetMaskType"),
        ("CISCO-LWAPP-HA-MIB", "cLHaServicePortPeerIpNetMask"),
        ("CISCO-LWAPP-HA-MIB", "cLHaRedundancyIpAddressType"),
        ("CISCO-LWAPP-HA-MIB", "cLHaRedundancyIpAddress"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPeerMacAddress"),
        ("CISCO-LWAPP-HA-MIB", "cLHaVirtualMacAddress"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPrimaryUnit"),
        ("CISCO-LWAPP-HA-MIB", "cLHaLinkEncryption"),
        ("CISCO-LWAPP-HA-MIB", "cLHaNetworkFailOver"),
        ("CISCO-LWAPP-HA-MIB", "cLHaRFStatusUnitIpType"),
        ("CISCO-LWAPP-HA-MIB", "cLHaRFStatusUnitIp"),
        ("CISCO-LWAPP-HA-MIB", "cLHaKATimeout"),
        ("CISCO-LWAPP-HA-MIB", "cLHaKARetryCount"),
        ("CISCO-LWAPP-HA-MIB", "cLHaGwRetryCount"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPeerSearchTimeout"))
)
if mibBuilder.loadTexts:
    ciscoLwappHaGlobalConfigGroup.setStatus("current")

ciscoLwappHaNetworkConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2, 2, 2)
)
ciscoLwappHaNetworkConfigGroup.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "cLHaNetworkRoutePeerIPNetmaskType"),
        ("CISCO-LWAPP-HA-MIB", "cLHaNetworkRoutePeerIPNetmask"),
        ("CISCO-LWAPP-HA-MIB", "cLHaNetworkRoutePeerGatewayType"),
        ("CISCO-LWAPP-HA-MIB", "cLHaNetworkRoutePeerGateway"),
        ("CISCO-LWAPP-HA-MIB", "cLHaNetworkRoutePeerTransferStatus"),
        ("CISCO-LWAPP-HA-MIB", "cLHaNetworkRoutePeerRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappHaNetworkConfigGroup.setStatus("current")

ciscoLwappHaStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2, 2, 3)
)
ciscoLwappHaStatisticsGroup.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "cLHaAvgPeerReachLatency"),
        ("CISCO-LWAPP-HA-MIB", "cLHaAvgGwReachLatency"),
        ("CISCO-LWAPP-HA-MIB", "cLHaBulkSyncStatus"),
        ("CISCO-LWAPP-HA-MIB", "cLHaTotalSystemMemory"),
        ("CISCO-LWAPP-HA-MIB", "cLHaFreeSystemMemory"),
        ("CISCO-LWAPP-HA-MIB", "cLHaUsedSystemMemory"),
        ("CISCO-LWAPP-HA-MIB", "cLHaAllocatedFromRtos"),
        ("CISCO-LWAPP-HA-MIB", "cLHaChunksFree"),
        ("CISCO-LWAPP-HA-MIB", "cLHaMmappedRegions"),
        ("CISCO-LWAPP-HA-MIB", "cLHaSpaceInMmappedRegions"),
        ("CISCO-LWAPP-HA-MIB", "cLHaTotalAllocatedSpace"),
        ("CISCO-LWAPP-HA-MIB", "cLHaTotalNotInUseSpace"),
        ("CISCO-LWAPP-HA-MIB", "cLHaTopMostReleasableSpace"),
        ("CISCO-LWAPP-HA-MIB", "cLHaTotalAllocatedInclMmap"),
        ("CISCO-LWAPP-HA-MIB", "cLHaTotalUsedMmap"),
        ("CISCO-LWAPP-HA-MIB", "cLHaTotalFreeInclMmap"),
        ("CISCO-LWAPP-HA-MIB", "cLHaAllCpuUsage"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPowerSupply1Present"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPowerSupply1Operational"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPowerSupply2Present"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPowerSupply2Operational"))
)
if mibBuilder.loadTexts:
    ciscoLwappHaStatisticsGroup.setStatus("current")

ciscoLwappHaMIBNotificationVariableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2, 2, 4)
)
ciscoLwappHaMIBNotificationVariableGroup.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "cLHaSecondaryControllerUsageTrapType"),
        ("CISCO-LWAPP-HA-MIB", "cLHaSecondaryControllerUsageDayCounter"),
        ("CISCO-LWAPP-HA-MIB", "cLHaBulkSyncCompleteEvent"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPeerHotStandbyEvent"))
)
if mibBuilder.loadTexts:
    ciscoLwappHaMIBNotificationVariableGroup.setStatus("current")

ciscoLwappMcHaConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2, 2, 6)
)
ciscoLwappMcHaConfigGroup.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "cLMcHaPortName"),
        ("CISCO-LWAPP-HA-MIB", "cLMcHaPortLocIpAddrType"),
        ("CISCO-LWAPP-HA-MIB", "cLMcHaPortLocIp"),
        ("CISCO-LWAPP-HA-MIB", "cLMcHaPortMask"),
        ("CISCO-LWAPP-HA-MIB", "cLMcHaPortRemoteIpAddrType"),
        ("CISCO-LWAPP-HA-MIB", "cLMcHaPortRemIp"),
        ("CISCO-LWAPP-HA-MIB", "cLMcHaKeepAliveTimeOut"),
        ("CISCO-LWAPP-HA-MIB", "cLMcHaChassisPriority"),
        ("CISCO-LWAPP-HA-MIB", "cLMcHaClearConfig"),
        ("CISCO-LWAPP-HA-MIB", "cLMcHaKeepAliveRetryCount"))
)
if mibBuilder.loadTexts:
    ciscoLwappMcHaConfigGroup.setStatus("current")

ciscoLwappMcRmiConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2, 2, 7)
)
ciscoLwappMcRmiConfigGroup.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "cLMcRmiConfigAction"),
        ("CISCO-LWAPP-HA-MIB", "cLMcRmiInterface"),
        ("CISCO-LWAPP-HA-MIB", "cLMcRmiChassisANum"),
        ("CISCO-LWAPP-HA-MIB", "cLMcRmiChassisAIpAddrType"),
        ("CISCO-LWAPP-HA-MIB", "cLMcRmiChassisAIp"),
        ("CISCO-LWAPP-HA-MIB", "cLMcRmiChassisBNum"),
        ("CISCO-LWAPP-HA-MIB", "cLMcRmiChassisBIpAddrType"),
        ("CISCO-LWAPP-HA-MIB", "cLMcRmiChassisBIp"),
        ("CISCO-LWAPP-HA-MIB", "cLMcRmiGatewayFailover"),
        ("CISCO-LWAPP-HA-MIB", "cLMcRmiGatewayFailoverInterval"))
)
if mibBuilder.loadTexts:
    ciscoLwappMcRmiConfigGroup.setStatus("current")


# Notification objects

cLHaSecondaryControllerUsageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 0, 1)
)
cLHaSecondaryControllerUsageTrap.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "cLHaSecondaryControllerUsageTrapType"),
        ("CISCO-LWAPP-HA-MIB", "cLHaSecondaryControllerUsageDayCounter"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    cLHaSecondaryControllerUsageTrap.setStatus(
        "current"
    )

cLHaRFSwapInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 0, 2)
)
cLHaRFSwapInfoTrap.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "cLHaRFStatusUnitIp"),
        ("CISCO-RF-MIB", "cRFStatusUnitState"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPeerIpAddress"),
        ("CISCO-RF-MIB", "cRFStatusPeerUnitState"))
)
if mibBuilder.loadTexts:
    cLHaRFSwapInfoTrap.setStatus(
        "current"
    )

cLHaBulkSyncCompleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 0, 3)
)
cLHaBulkSyncCompleteTrap.setObjects(
    ("CISCO-LWAPP-HA-MIB", "cLHaBulkSyncCompleteEvent")
)
if mibBuilder.loadTexts:
    cLHaBulkSyncCompleteTrap.setStatus(
        "current"
    )

cLHaPeerHotStandbyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 0, 4)
)
cLHaPeerHotStandbyTrap.setObjects(
    ("CISCO-LWAPP-HA-MIB", "cLHaPeerHotStandbyEvent")
)
if mibBuilder.loadTexts:
    cLHaPeerHotStandbyTrap.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappHaMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2, 2, 5)
)
ciscoLwappHaMIBNotificationGroup.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "cLHaSecondaryControllerUsageTrap"),
        ("CISCO-LWAPP-HA-MIB", "cLHaRFSwapInfoTrap"),
        ("CISCO-LWAPP-HA-MIB", "cLHaBulkSyncCompleteTrap"),
        ("CISCO-LWAPP-HA-MIB", "cLHaPeerHotStandbyTrap"))
)
if mibBuilder.loadTexts:
    ciscoLwappHaMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappHaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2, 1, 1)
)
ciscoLwappHaMIBCompliance.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "ciscoLwappHaGlobalConfigGroup"),
        ("CISCO-LWAPP-HA-MIB", "ciscoLwappHaNetworkConfigGroup"),
        ("CISCO-LWAPP-HA-MIB", "ciscoLwappHaStatisticsGroup"),
        ("CISCO-LWAPP-HA-MIB", "ciscoLwappHaMIBNotificationVariableGroup"),
        ("CISCO-LWAPP-HA-MIB", "ciscoLwappHaMIBNotificationGroup"),
        ("CISCO-LWAPP-HA-MIB", "ciscoLwappMcHaConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappHaMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappHaMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 843, 2, 1, 2)
)
ciscoLwappHaMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-HA-MIB", "ciscoLwappHaGlobalConfigGroup"),
        ("CISCO-LWAPP-HA-MIB", "ciscoLwappHaNetworkConfigGroup"),
        ("CISCO-LWAPP-HA-MIB", "ciscoLwappHaStatisticsGroup"),
        ("CISCO-LWAPP-HA-MIB", "ciscoLwappHaMIBNotificationVariableGroup"),
        ("CISCO-LWAPP-HA-MIB", "ciscoLwappHaMIBNotificationGroup"),
        ("CISCO-LWAPP-HA-MIB", "ciscoLwappMcHaConfigGroup"),
        ("CISCO-LWAPP-HA-MIB", "ciscoLwappMcRmiConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappHaMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-HA-MIB",
    **{"ciscoLwappHaMIB": ciscoLwappHaMIB,
       "ciscoLwappHaMIBNotifs": ciscoLwappHaMIBNotifs,
       "cLHaSecondaryControllerUsageTrap": cLHaSecondaryControllerUsageTrap,
       "cLHaRFSwapInfoTrap": cLHaRFSwapInfoTrap,
       "cLHaBulkSyncCompleteTrap": cLHaBulkSyncCompleteTrap,
       "cLHaPeerHotStandbyTrap": cLHaPeerHotStandbyTrap,
       "ciscoLwappHaMIBObjects": ciscoLwappHaMIBObjects,
       "ciscoLwappHaGlobalConfig": ciscoLwappHaGlobalConfig,
       "cLHaApSsoConfig": cLHaApSsoConfig,
       "cLHaPeerIpAddressType": cLHaPeerIpAddressType,
       "cLHaPeerIpAddress": cLHaPeerIpAddress,
       "cLHaServicePortPeerIpAddressType": cLHaServicePortPeerIpAddressType,
       "cLHaServicePortPeerIpAddress": cLHaServicePortPeerIpAddress,
       "cLHaServicePortPeerIpNetMaskType": cLHaServicePortPeerIpNetMaskType,
       "cLHaServicePortPeerIpNetMask": cLHaServicePortPeerIpNetMask,
       "cLHaRedundancyIpAddressType": cLHaRedundancyIpAddressType,
       "cLHaRedundancyIpAddress": cLHaRedundancyIpAddress,
       "cLHaPeerMacAddress": cLHaPeerMacAddress,
       "cLHaVirtualMacAddress": cLHaVirtualMacAddress,
       "cLHaPrimaryUnit": cLHaPrimaryUnit,
       "cLHaLinkEncryption": cLHaLinkEncryption,
       "cLHaNetworkFailOver": cLHaNetworkFailOver,
       "cLHaRFStatusUnitIp": cLHaRFStatusUnitIp,
       "cLHaKATimeout": cLHaKATimeout,
       "cLHaKARetryCount": cLHaKARetryCount,
       "cLHaGwRetryCount": cLHaGwRetryCount,
       "cLHaPeerSearchTimeout": cLHaPeerSearchTimeout,
       "cLHaRFStatusUnitIpType": cLHaRFStatusUnitIpType,
       "ciscoLwappHaNetworkConfig": ciscoLwappHaNetworkConfig,
       "cLHaNetworkRoutePeerConfigTable": cLHaNetworkRoutePeerConfigTable,
       "cLHaNetworkRoutePeerConfigEntry": cLHaNetworkRoutePeerConfigEntry,
       "cLHaNetworkRoutePeerIPAddressType": cLHaNetworkRoutePeerIPAddressType,
       "cLHaNetworkRoutePeerIPAddress": cLHaNetworkRoutePeerIPAddress,
       "cLHaNetworkRoutePeerIPNetmaskType": cLHaNetworkRoutePeerIPNetmaskType,
       "cLHaNetworkRoutePeerIPNetmask": cLHaNetworkRoutePeerIPNetmask,
       "cLHaNetworkRoutePeerGatewayType": cLHaNetworkRoutePeerGatewayType,
       "cLHaNetworkRoutePeerGateway": cLHaNetworkRoutePeerGateway,
       "cLHaNetworkRoutePeerTransferStatus": cLHaNetworkRoutePeerTransferStatus,
       "cLHaNetworkRoutePeerRowStatus": cLHaNetworkRoutePeerRowStatus,
       "ciscoLwappHaNotificationVariable": ciscoLwappHaNotificationVariable,
       "cLHaSecondaryControllerUsageTrapType": cLHaSecondaryControllerUsageTrapType,
       "cLHaSecondaryControllerUsageDayCounter": cLHaSecondaryControllerUsageDayCounter,
       "cLHaBulkSyncCompleteEvent": cLHaBulkSyncCompleteEvent,
       "cLHaPeerHotStandbyEvent": cLHaPeerHotStandbyEvent,
       "ciscoLwappHaPeerStatisticsVariable": ciscoLwappHaPeerStatisticsVariable,
       "ciscoLwappHaSystemStatistics": ciscoLwappHaSystemStatistics,
       "ciscoLwappHaCpuStatistics": ciscoLwappHaCpuStatistics,
       "cLHaAllCpuUsage": cLHaAllCpuUsage,
       "ciscoLwappHaPowerSupplyStatistics": ciscoLwappHaPowerSupplyStatistics,
       "cLHaPowerSupply1Present": cLHaPowerSupply1Present,
       "cLHaPowerSupply1Operational": cLHaPowerSupply1Operational,
       "cLHaPowerSupply2Present": cLHaPowerSupply2Present,
       "cLHaPowerSupply2Operational": cLHaPowerSupply2Operational,
       "ciscoLwappHaMemoryStatistics": ciscoLwappHaMemoryStatistics,
       "cLHaTotalSystemMemory": cLHaTotalSystemMemory,
       "cLHaFreeSystemMemory": cLHaFreeSystemMemory,
       "cLHaUsedSystemMemory": cLHaUsedSystemMemory,
       "cLHaAllocatedFromRtos": cLHaAllocatedFromRtos,
       "cLHaChunksFree": cLHaChunksFree,
       "cLHaMmappedRegions": cLHaMmappedRegions,
       "cLHaSpaceInMmappedRegions": cLHaSpaceInMmappedRegions,
       "cLHaTotalAllocatedSpace": cLHaTotalAllocatedSpace,
       "cLHaTotalNotInUseSpace": cLHaTotalNotInUseSpace,
       "cLHaTopMostReleasableSpace": cLHaTopMostReleasableSpace,
       "cLHaTotalAllocatedInclMmap": cLHaTotalAllocatedInclMmap,
       "cLHaTotalUsedMmap": cLHaTotalUsedMmap,
       "cLHaTotalFreeInclMmap": cLHaTotalFreeInclMmap,
       "ciscoLwappHaStatisticsVariable": ciscoLwappHaStatisticsVariable,
       "cLHaAvgPeerReachLatency": cLHaAvgPeerReachLatency,
       "cLHaAvgGwReachLatency": cLHaAvgGwReachLatency,
       "cLHaBulkSyncStatus": cLHaBulkSyncStatus,
       "ciscoLwappMcHaConfig": ciscoLwappMcHaConfig,
       "cLMcHaPortName": cLMcHaPortName,
       "cLMcHaPortLocIpAddrType": cLMcHaPortLocIpAddrType,
       "cLMcHaPortLocIp": cLMcHaPortLocIp,
       "cLMcHaPortMask": cLMcHaPortMask,
       "cLMcHaPortRemoteIpAddrType": cLMcHaPortRemoteIpAddrType,
       "cLMcHaPortRemIp": cLMcHaPortRemIp,
       "cLMcHaKeepAliveTimeOut": cLMcHaKeepAliveTimeOut,
       "cLMcHaChassisPriority": cLMcHaChassisPriority,
       "cLMcHaClearConfig": cLMcHaClearConfig,
       "cLMcHaKeepAliveRetryCount": cLMcHaKeepAliveRetryCount,
       "ciscoLwappMcRmiConfig": ciscoLwappMcRmiConfig,
       "cLMcRmiConfigAction": cLMcRmiConfigAction,
       "cLMcRmiInterface": cLMcRmiInterface,
       "cLMcRmiChassisANum": cLMcRmiChassisANum,
       "cLMcRmiChassisAIpAddrType": cLMcRmiChassisAIpAddrType,
       "cLMcRmiChassisAIp": cLMcRmiChassisAIp,
       "cLMcRmiChassisBNum": cLMcRmiChassisBNum,
       "cLMcRmiChassisBIpAddrType": cLMcRmiChassisBIpAddrType,
       "cLMcRmiChassisBIp": cLMcRmiChassisBIp,
       "cLMcRmiGatewayFailover": cLMcRmiGatewayFailover,
       "cLMcRmiGatewayFailoverInterval": cLMcRmiGatewayFailoverInterval,
       "ciscoLwappHaMIBConform": ciscoLwappHaMIBConform,
       "ciscoLwappHaMIBCompliances": ciscoLwappHaMIBCompliances,
       "ciscoLwappHaMIBCompliance": ciscoLwappHaMIBCompliance,
       "ciscoLwappHaMIBComplianceRev1": ciscoLwappHaMIBComplianceRev1,
       "ciscoLwappHaMIBGroups": ciscoLwappHaMIBGroups,
       "ciscoLwappHaGlobalConfigGroup": ciscoLwappHaGlobalConfigGroup,
       "ciscoLwappHaNetworkConfigGroup": ciscoLwappHaNetworkConfigGroup,
       "ciscoLwappHaStatisticsGroup": ciscoLwappHaStatisticsGroup,
       "ciscoLwappHaMIBNotificationVariableGroup": ciscoLwappHaMIBNotificationVariableGroup,
       "ciscoLwappHaMIBNotificationGroup": ciscoLwappHaMIBNotificationGroup,
       "ciscoLwappMcHaConfigGroup": ciscoLwappMcHaConfigGroup,
       "ciscoLwappMcRmiConfigGroup": ciscoLwappMcRmiConfigGroup}
)
