# SNMP MIB module (CISCO-LWAPP-MOBILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-MOBILITY-MIB.mib
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

ciscoLwappMobilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576)
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityMIB.setRevisions(
        ("2020-10-05 00:00",
         "2019-11-11 00:00",
         "2019-04-25 00:00",
         "2018-05-28 00:00",
         "2018-04-24 00:00",
         "2017-04-27 00:00",
         "2014-04-01 00:00",
         "2010-08-23 00:00",
         "2006-07-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappMobilityMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityMIBNotifs = _CiscoLwappMobilityMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0)
)
_CiscoLwappMobilityMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityMIBObjects = _CiscoLwappMobilityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1)
)
_CLMobilityAnchorTable_Object = MibTable
cLMobilityAnchorTable = _CLMobilityAnchorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1)
)
if mibBuilder.loadTexts:
    cLMobilityAnchorTable.setStatus("current")
_CLMobilityAnchorEntry_Object = MibTableRow
cLMobilityAnchorEntry = _CLMobilityAnchorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1, 1)
)
cLMobilityAnchorEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorWlanProfileName"),
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorSwitchIPAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityAnchorEntry.setStatus("current")


class _CLMobilityAnchorWlanProfileName_Type(OctetString):
    """Custom type cLMobilityAnchorWlanProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLMobilityAnchorWlanProfileName_Type.__name__ = "OctetString"
_CLMobilityAnchorWlanProfileName_Object = MibTableColumn
cLMobilityAnchorWlanProfileName = _CLMobilityAnchorWlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1, 1, 1),
    _CLMobilityAnchorWlanProfileName_Type()
)
cLMobilityAnchorWlanProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityAnchorWlanProfileName.setStatus("current")
_CLMobilityAnchorSwitchIPAddress_Type = IpAddress
_CLMobilityAnchorSwitchIPAddress_Object = MibTableColumn
cLMobilityAnchorSwitchIPAddress = _CLMobilityAnchorSwitchIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1, 1, 2),
    _CLMobilityAnchorSwitchIPAddress_Type()
)
cLMobilityAnchorSwitchIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityAnchorSwitchIPAddress.setStatus("current")


class _CLMobilityAnchorStatus_Type(Bits):
    """Custom type cLMobilityAnchorStatus based on Bits"""
    namedValues = NamedValues(
        *(("controlpath", 0),
          ("datapath", 1))
    )

_CLMobilityAnchorStatus_Type.__name__ = "Bits"
_CLMobilityAnchorStatus_Object = MibTableColumn
cLMobilityAnchorStatus = _CLMobilityAnchorStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1, 1, 3),
    _CLMobilityAnchorStatus_Type()
)
cLMobilityAnchorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityAnchorStatus.setStatus("current")
_CLMobilityAnchorRowStatus_Type = RowStatus
_CLMobilityAnchorRowStatus_Object = MibTableColumn
cLMobilityAnchorRowStatus = _CLMobilityAnchorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 1, 1, 4),
    _CLMobilityAnchorRowStatus_Type()
)
cLMobilityAnchorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityAnchorRowStatus.setStatus("current")
_CLMobilityAnchorGlobalDot11Config_ObjectIdentity = ObjectIdentity
cLMobilityAnchorGlobalDot11Config = _CLMobilityAnchorGlobalDot11Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 2)
)


class _CLMobilityAnchorGroupKeepAliveNumber_Type(Integer32):
    """Custom type cLMobilityAnchorGroupKeepAliveNumber based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_CLMobilityAnchorGroupKeepAliveNumber_Type.__name__ = "Integer32"
_CLMobilityAnchorGroupKeepAliveNumber_Object = MibScalar
cLMobilityAnchorGroupKeepAliveNumber = _CLMobilityAnchorGroupKeepAliveNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 2, 1),
    _CLMobilityAnchorGroupKeepAliveNumber_Type()
)
cLMobilityAnchorGroupKeepAliveNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityAnchorGroupKeepAliveNumber.setStatus("current")


class _CLMobilityAnchorGroupKeepAliveInterval_Type(Integer32):
    """Custom type cLMobilityAnchorGroupKeepAliveInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CLMobilityAnchorGroupKeepAliveInterval_Type.__name__ = "Integer32"
_CLMobilityAnchorGroupKeepAliveInterval_Object = MibScalar
cLMobilityAnchorGroupKeepAliveInterval = _CLMobilityAnchorGroupKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 2, 2),
    _CLMobilityAnchorGroupKeepAliveInterval_Type()
)
cLMobilityAnchorGroupKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityAnchorGroupKeepAliveInterval.setStatus("current")
_CLMobilityAnchorSmtStatus_Type = TruthValue
_CLMobilityAnchorSmtStatus_Object = MibScalar
cLMobilityAnchorSmtStatus = _CLMobilityAnchorSmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 2, 3),
    _CLMobilityAnchorSmtStatus_Type()
)
cLMobilityAnchorSmtStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityAnchorSmtStatus.setStatus("current")
_CLMobilityAnchorCurrentSmt_Type = TruthValue
_CLMobilityAnchorCurrentSmt_Object = MibScalar
cLMobilityAnchorCurrentSmt = _CLMobilityAnchorCurrentSmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 2, 4),
    _CLMobilityAnchorCurrentSmt_Type()
)
cLMobilityAnchorCurrentSmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityAnchorCurrentSmt.setStatus("current")


class _CLMobilityAnchorDscpValue_Type(Integer32):
    """Custom type cLMobilityAnchorDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CLMobilityAnchorDscpValue_Type.__name__ = "Integer32"
_CLMobilityAnchorDscpValue_Object = MibScalar
cLMobilityAnchorDscpValue = _CLMobilityAnchorDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 2, 5),
    _CLMobilityAnchorDscpValue_Type()
)
cLMobilityAnchorDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityAnchorDscpValue.setStatus("current")
_CLMobilityTrapVariables_ObjectIdentity = ObjectIdentity
cLMobilityTrapVariables = _CLMobilityTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 3)
)


class _CLMobilityAnchorWlanId_Type(Integer32):
    """Custom type cLMobilityAnchorWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CLMobilityAnchorWlanId_Type.__name__ = "Integer32"
_CLMobilityAnchorWlanId_Object = MibScalar
cLMobilityAnchorWlanId = _CLMobilityAnchorWlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 3, 1),
    _CLMobilityAnchorWlanId_Type()
)
cLMobilityAnchorWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMobilityAnchorWlanId.setStatus("current")
_CLMobilityAnchorAddressType_Type = InetAddressType
_CLMobilityAnchorAddressType_Object = MibScalar
cLMobilityAnchorAddressType = _CLMobilityAnchorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 3, 2),
    _CLMobilityAnchorAddressType_Type()
)
cLMobilityAnchorAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMobilityAnchorAddressType.setStatus("current")
_CLMobilityAnchorAddress_Type = InetAddress
_CLMobilityAnchorAddress_Object = MibScalar
cLMobilityAnchorAddress = _CLMobilityAnchorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 3, 3),
    _CLMobilityAnchorAddress_Type()
)
cLMobilityAnchorAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cLMobilityAnchorAddress.setStatus("current")
_CLMobilityMulticastGroupConfig_ObjectIdentity = ObjectIdentity
cLMobilityMulticastGroupConfig = _CLMobilityMulticastGroupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4)
)
_CLMobilityMulticastMessagingEnable_Type = TruthValue
_CLMobilityMulticastMessagingEnable_Object = MibScalar
cLMobilityMulticastMessagingEnable = _CLMobilityMulticastMessagingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 1),
    _CLMobilityMulticastMessagingEnable_Type()
)
cLMobilityMulticastMessagingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMulticastMessagingEnable.setStatus("current")
_CLMobilityMulticastGroupTable_Object = MibTable
cLMobilityMulticastGroupTable = _CLMobilityMulticastGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cLMobilityMulticastGroupTable.setStatus("current")
_CLMobilityMulticastGroupEntry_Object = MibTableRow
cLMobilityMulticastGroupEntry = _CLMobilityMulticastGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 2, 1)
)
cLMobilityMulticastGroupEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMacAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityMulticastGroupEntry.setStatus("current")
_CLMobilityGroupMacAddress_Type = MacAddress
_CLMobilityGroupMacAddress_Object = MibTableColumn
cLMobilityGroupMacAddress = _CLMobilityGroupMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 2, 1, 1),
    _CLMobilityGroupMacAddress_Type()
)
cLMobilityGroupMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityGroupMacAddress.setStatus("current")
_CLMobilityMulticastGroupIPAddressType_Type = InetAddressType
_CLMobilityMulticastGroupIPAddressType_Object = MibTableColumn
cLMobilityMulticastGroupIPAddressType = _CLMobilityMulticastGroupIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 2, 1, 2),
    _CLMobilityMulticastGroupIPAddressType_Type()
)
cLMobilityMulticastGroupIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMulticastGroupIPAddressType.setStatus("current")
_CLMobilityMulticastGroupIPAddress_Type = InetAddress
_CLMobilityMulticastGroupIPAddress_Object = MibTableColumn
cLMobilityMulticastGroupIPAddress = _CLMobilityMulticastGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 4, 2, 1, 3),
    _CLMobilityMulticastGroupIPAddress_Type()
)
cLMobilityMulticastGroupIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMulticastGroupIPAddress.setStatus("current")
_CLMobilityGroupMembersTable_Object = MibTable
cLMobilityGroupMembersTable = _CLMobilityGroupMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5)
)
if mibBuilder.loadTexts:
    cLMobilityGroupMembersTable.setStatus("current")
_CLMobilityGroupMembersEntry_Object = MibTableRow
cLMobilityGroupMembersEntry = _CLMobilityGroupMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1)
)
cLMobilityGroupMembersEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMacAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityGroupMembersEntry.setStatus("current")
_CLMobilityGroupMemberIPAddressType_Type = InetAddressType
_CLMobilityGroupMemberIPAddressType_Object = MibTableColumn
cLMobilityGroupMemberIPAddressType = _CLMobilityGroupMemberIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 1),
    _CLMobilityGroupMemberIPAddressType_Type()
)
cLMobilityGroupMemberIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberIPAddressType.setStatus("deprecated")
_CLMobilityGroupMemberIPAddress_Type = InetAddress
_CLMobilityGroupMemberIPAddress_Object = MibTableColumn
cLMobilityGroupMemberIPAddress = _CLMobilityGroupMemberIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 2),
    _CLMobilityGroupMemberIPAddress_Type()
)
cLMobilityGroupMemberIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberIPAddress.setStatus("deprecated")


class _CLMobilityGroupMemberControlPathStatusUp_Type(TruthValue):
    """Custom type cLMobilityGroupMemberControlPathStatusUp based on TruthValue"""
    defaultValue = 2


_CLMobilityGroupMemberControlPathStatusUp_Type.__name__ = "TruthValue"
_CLMobilityGroupMemberControlPathStatusUp_Object = MibTableColumn
cLMobilityGroupMemberControlPathStatusUp = _CLMobilityGroupMemberControlPathStatusUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 3),
    _CLMobilityGroupMemberControlPathStatusUp_Type()
)
cLMobilityGroupMemberControlPathStatusUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberControlPathStatusUp.setStatus("current")


class _CLMobilityGroupMemberDataPathStatusUp_Type(TruthValue):
    """Custom type cLMobilityGroupMemberDataPathStatusUp based on TruthValue"""
    defaultValue = 2


_CLMobilityGroupMemberDataPathStatusUp_Type.__name__ = "TruthValue"
_CLMobilityGroupMemberDataPathStatusUp_Object = MibTableColumn
cLMobilityGroupMemberDataPathStatusUp = _CLMobilityGroupMemberDataPathStatusUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 4),
    _CLMobilityGroupMemberDataPathStatusUp_Type()
)
cLMobilityGroupMemberDataPathStatusUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberDataPathStatusUp.setStatus("current")


class _CLMobilityGroupMemberHashKey_Type(OctetString):
    """Custom type cLMobilityGroupMemberHashKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 40),
    )


_CLMobilityGroupMemberHashKey_Type.__name__ = "OctetString"
_CLMobilityGroupMemberHashKey_Object = MibTableColumn
cLMobilityGroupMemberHashKey = _CLMobilityGroupMemberHashKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 5),
    _CLMobilityGroupMemberHashKey_Type()
)
cLMobilityGroupMemberHashKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberHashKey.setStatus("current")
_CLMobilityGroupMemberAddressType_Type = InetAddressType
_CLMobilityGroupMemberAddressType_Object = MibTableColumn
cLMobilityGroupMemberAddressType = _CLMobilityGroupMemberAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 6),
    _CLMobilityGroupMemberAddressType_Type()
)
cLMobilityGroupMemberAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberAddressType.setStatus("current")
_CLMobilityGroupMemberAddress_Type = InetAddress
_CLMobilityGroupMemberAddress_Object = MibTableColumn
cLMobilityGroupMemberAddress = _CLMobilityGroupMemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 7),
    _CLMobilityGroupMemberAddress_Type()
)
cLMobilityGroupMemberAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberAddress.setStatus("current")
_CLMobilityGroupMemberGroupName_Type = SnmpAdminString
_CLMobilityGroupMemberGroupName_Object = MibTableColumn
cLMobilityGroupMemberGroupName = _CLMobilityGroupMemberGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 8),
    _CLMobilityGroupMemberGroupName_Type()
)
cLMobilityGroupMemberGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberGroupName.setStatus("current")
_CLMobilityGroupMemberRowStatus_Type = RowStatus
_CLMobilityGroupMemberRowStatus_Object = MibTableColumn
cLMobilityGroupMemberRowStatus = _CLMobilityGroupMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 9),
    _CLMobilityGroupMemberRowStatus_Type()
)
cLMobilityGroupMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberRowStatus.setStatus("current")


class _CLMobilityGroupMemberDataDtls_Type(TruthValue):
    """Custom type cLMobilityGroupMemberDataDtls based on TruthValue"""
    defaultValue = 1


_CLMobilityGroupMemberDataDtls_Type.__name__ = "TruthValue"
_CLMobilityGroupMemberDataDtls_Object = MibTableColumn
cLMobilityGroupMemberDataDtls = _CLMobilityGroupMemberDataDtls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 10),
    _CLMobilityGroupMemberDataDtls_Type()
)
cLMobilityGroupMemberDataDtls.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberDataDtls.setStatus("current")
_CLMobilityGroupMemberIPAddressTypeRev1_Type = InetAddressType
_CLMobilityGroupMemberIPAddressTypeRev1_Object = MibTableColumn
cLMobilityGroupMemberIPAddressTypeRev1 = _CLMobilityGroupMemberIPAddressTypeRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 11),
    _CLMobilityGroupMemberIPAddressTypeRev1_Type()
)
cLMobilityGroupMemberIPAddressTypeRev1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberIPAddressTypeRev1.setStatus("current")
_CLMobilityGroupMemberIPAddressRev1_Type = InetAddress
_CLMobilityGroupMemberIPAddressRev1_Object = MibTableColumn
cLMobilityGroupMemberIPAddressRev1 = _CLMobilityGroupMemberIPAddressRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 5, 1, 12),
    _CLMobilityGroupMemberIPAddressRev1_Type()
)
cLMobilityGroupMemberIPAddressRev1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityGroupMemberIPAddressRev1.setStatus("current")
_CLMobilityForeignWlcMapTable_Object = MibTable
cLMobilityForeignWlcMapTable = _CLMobilityForeignWlcMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 6)
)
if mibBuilder.loadTexts:
    cLMobilityForeignWlcMapTable.setStatus("current")
_CLMobilityForeignWlcMapEntry_Object = MibTableRow
cLMobilityForeignWlcMapEntry = _CLMobilityForeignWlcMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 6, 1)
)
cLMobilityForeignWlcMapEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorWlanProfileName"),
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityForeignWlcMapMacAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityForeignWlcMapEntry.setStatus("current")
_CLMobilityForeignWlcMapMacAddress_Type = MacAddress
_CLMobilityForeignWlcMapMacAddress_Object = MibTableColumn
cLMobilityForeignWlcMapMacAddress = _CLMobilityForeignWlcMapMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 6, 1, 1),
    _CLMobilityForeignWlcMapMacAddress_Type()
)
cLMobilityForeignWlcMapMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityForeignWlcMapMacAddress.setStatus("current")


class _CLMobilityForeignWlcMapIf_Type(SnmpAdminString):
    """Custom type cLMobilityForeignWlcMapIf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CLMobilityForeignWlcMapIf_Type.__name__ = "SnmpAdminString"
_CLMobilityForeignWlcMapIf_Object = MibTableColumn
cLMobilityForeignWlcMapIf = _CLMobilityForeignWlcMapIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 6, 1, 2),
    _CLMobilityForeignWlcMapIf_Type()
)
cLMobilityForeignWlcMapIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityForeignWlcMapIf.setStatus("current")
_CLMobilityForeignWlcMapRowStatus_Type = RowStatus
_CLMobilityForeignWlcMapRowStatus_Object = MibTableColumn
cLMobilityForeignWlcMapRowStatus = _CLMobilityForeignWlcMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 6, 1, 3),
    _CLMobilityForeignWlcMapRowStatus_Type()
)
cLMobilityForeignWlcMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLMobilityForeignWlcMapRowStatus.setStatus("current")
_CLMobilityStats_ObjectIdentity = ObjectIdentity
cLMobilityStats = _CLMobilityStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 7)
)
_CLMobilityIncomingCount_Type = Counter32
_CLMobilityIncomingCount_Object = MibScalar
cLMobilityIncomingCount = _CLMobilityIncomingCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 7, 1),
    _CLMobilityIncomingCount_Type()
)
cLMobilityIncomingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityIncomingCount.setStatus("current")
_CLMobilityOutgoingCount_Type = Counter32
_CLMobilityOutgoingCount_Object = MibScalar
cLMobilityOutgoingCount = _CLMobilityOutgoingCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 7, 2),
    _CLMobilityOutgoingCount_Type()
)
cLMobilityOutgoingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityOutgoingCount.setStatus("current")
_CiscoLwappMobilityMCGlobalObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityMCGlobalObjects = _CiscoLwappMobilityMCGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8)
)


class _CLMobilityMCMOEnableStatus_Type(TruthValue):
    """Custom type cLMobilityMCMOEnableStatus based on TruthValue"""
    defaultValue = 2


_CLMobilityMCMOEnableStatus_Type.__name__ = "TruthValue"
_CLMobilityMCMOEnableStatus_Object = MibScalar
cLMobilityMCMOEnableStatus = _CLMobilityMCMOEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 1),
    _CLMobilityMCMOEnableStatus_Type()
)
cLMobilityMCMOEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityMCMOEnableStatus.setStatus("current")


class _CLMobilityMCMOAdminEnableStatus_Type(TruthValue):
    """Custom type cLMobilityMCMOAdminEnableStatus based on TruthValue"""
    defaultValue = 2


_CLMobilityMCMOAdminEnableStatus_Type.__name__ = "TruthValue"
_CLMobilityMCMOAdminEnableStatus_Object = MibScalar
cLMobilityMCMOAdminEnableStatus = _CLMobilityMCMOAdminEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 2),
    _CLMobilityMCMOAdminEnableStatus_Type()
)
cLMobilityMCMOAdminEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCMOAdminEnableStatus.setStatus("current")


class _CLMobilityMCEnableStatus_Type(TruthValue):
    """Custom type cLMobilityMCEnableStatus based on TruthValue"""
    defaultValue = 2


_CLMobilityMCEnableStatus_Type.__name__ = "TruthValue"
_CLMobilityMCEnableStatus_Object = MibScalar
cLMobilityMCEnableStatus = _CLMobilityMCEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 3),
    _CLMobilityMCEnableStatus_Type()
)
cLMobilityMCEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityMCEnableStatus.setStatus("current")


class _CLMobilityMCAdminEnableStatus_Type(TruthValue):
    """Custom type cLMobilityMCAdminEnableStatus based on TruthValue"""
    defaultValue = 2


_CLMobilityMCAdminEnableStatus_Type.__name__ = "TruthValue"
_CLMobilityMCAdminEnableStatus_Object = MibScalar
cLMobilityMCAdminEnableStatus = _CLMobilityMCAdminEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 4),
    _CLMobilityMCAdminEnableStatus_Type()
)
cLMobilityMCAdminEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCAdminEnableStatus.setStatus("current")


class _CLMobilityMCMulticastMode_Type(TruthValue):
    """Custom type cLMobilityMCMulticastMode based on TruthValue"""
    defaultValue = 2


_CLMobilityMCMulticastMode_Type.__name__ = "TruthValue"
_CLMobilityMCMulticastMode_Object = MibScalar
cLMobilityMCMulticastMode = _CLMobilityMCMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 5),
    _CLMobilityMCMulticastMode_Type()
)
cLMobilityMCMulticastMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCMulticastMode.setStatus("current")


class _CLMobilityMCKeepAliveCount_Type(Unsigned32):
    """Custom type cLMobilityMCKeepAliveCount based on Unsigned32"""
    defaultValue = 3


_CLMobilityMCKeepAliveCount_Type.__name__ = "Unsigned32"
_CLMobilityMCKeepAliveCount_Object = MibScalar
cLMobilityMCKeepAliveCount = _CLMobilityMCKeepAliveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 6),
    _CLMobilityMCKeepAliveCount_Type()
)
cLMobilityMCKeepAliveCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCKeepAliveCount.setStatus("current")


class _CLMobilityMCKeepAliveInterval_Type(Unsigned32):
    """Custom type cLMobilityMCKeepAliveInterval based on Unsigned32"""
    defaultValue = 10


_CLMobilityMCKeepAliveInterval_Type.__name__ = "Unsigned32"
_CLMobilityMCKeepAliveInterval_Object = MibScalar
cLMobilityMCKeepAliveInterval = _CLMobilityMCKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 7),
    _CLMobilityMCKeepAliveInterval_Type()
)
cLMobilityMCKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCKeepAliveInterval.setStatus("current")


class _CLMobilityMCDscpValue_Type(Unsigned32):
    """Custom type cLMobilityMCDscpValue based on Unsigned32"""
    defaultValue = 0


_CLMobilityMCDscpValue_Type.__name__ = "Unsigned32"
_CLMobilityMCDscpValue_Object = MibScalar
cLMobilityMCDscpValue = _CLMobilityMCDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 8),
    _CLMobilityMCDscpValue_Type()
)
cLMobilityMCDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCDscpValue.setStatus("current")
_CLMobilityMCMOPublicAddressType_Type = InetAddressType
_CLMobilityMCMOPublicAddressType_Object = MibScalar
cLMobilityMCMOPublicAddressType = _CLMobilityMCMOPublicAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 9),
    _CLMobilityMCMOPublicAddressType_Type()
)
cLMobilityMCMOPublicAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCMOPublicAddressType.setStatus("current")
_CLMobilityMCMOPublicAddress_Type = InetAddress
_CLMobilityMCMOPublicAddress_Object = MibScalar
cLMobilityMCMOPublicAddress = _CLMobilityMCMOPublicAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 10),
    _CLMobilityMCMOPublicAddress_Type()
)
cLMobilityMCMOPublicAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCMOPublicAddress.setStatus("current")
_CLMobilityMCApCountLicensesInUse_Type = Unsigned32
_CLMobilityMCApCountLicensesInUse_Object = MibScalar
cLMobilityMCApCountLicensesInUse = _CLMobilityMCApCountLicensesInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 11),
    _CLMobilityMCApCountLicensesInUse_Type()
)
cLMobilityMCApCountLicensesInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityMCApCountLicensesInUse.setStatus("current")
_CLMobilityMCOwnGroupMulticastAddressType_Type = InetAddressType
_CLMobilityMCOwnGroupMulticastAddressType_Object = MibScalar
cLMobilityMCOwnGroupMulticastAddressType = _CLMobilityMCOwnGroupMulticastAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 12),
    _CLMobilityMCOwnGroupMulticastAddressType_Type()
)
cLMobilityMCOwnGroupMulticastAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCOwnGroupMulticastAddressType.setStatus("current")
_CLMobilityMCOwnGroupMulticastAddress_Type = InetAddress
_CLMobilityMCOwnGroupMulticastAddress_Object = MibScalar
cLMobilityMCOwnGroupMulticastAddress = _CLMobilityMCOwnGroupMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 13),
    _CLMobilityMCOwnGroupMulticastAddress_Type()
)
cLMobilityMCOwnGroupMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCOwnGroupMulticastAddress.setStatus("current")
_CLMobilityMCMobilityGroupName_Type = SnmpAdminString
_CLMobilityMCMobilityGroupName_Object = MibScalar
cLMobilityMCMobilityGroupName = _CLMobilityMCMobilityGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 14),
    _CLMobilityMCMobilityGroupName_Type()
)
cLMobilityMCMobilityGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCMobilityGroupName.setStatus("current")
_CLMobilityMCMONumberOfClients_Type = Unsigned32
_CLMobilityMCMONumberOfClients_Object = MibScalar
cLMobilityMCMONumberOfClients = _CLMobilityMCMONumberOfClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 15),
    _CLMobilityMCMONumberOfClients_Type()
)
cLMobilityMCMONumberOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityMCMONumberOfClients.setStatus("current")
_CLMobilityMCNumberOfMCs_Type = Unsigned32
_CLMobilityMCNumberOfMCs_Object = MibScalar
cLMobilityMCNumberOfMCs = _CLMobilityMCNumberOfMCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 16),
    _CLMobilityMCNumberOfMCs_Type()
)
cLMobilityMCNumberOfMCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityMCNumberOfMCs.setStatus("current")
_CLMobilityMCTotalNumberOfReportedAPs_Type = Unsigned32
_CLMobilityMCTotalNumberOfReportedAPs_Object = MibScalar
cLMobilityMCTotalNumberOfReportedAPs = _CLMobilityMCTotalNumberOfReportedAPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 17),
    _CLMobilityMCTotalNumberOfReportedAPs_Type()
)
cLMobilityMCTotalNumberOfReportedAPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityMCTotalNumberOfReportedAPs.setStatus("current")
_CLMobilityMCNumberOfReportedAPsInSubDomain_Type = Unsigned32
_CLMobilityMCNumberOfReportedAPsInSubDomain_Object = MibScalar
cLMobilityMCNumberOfReportedAPsInSubDomain = _CLMobilityMCNumberOfReportedAPsInSubDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 18),
    _CLMobilityMCNumberOfReportedAPsInSubDomain_Type()
)
cLMobilityMCNumberOfReportedAPsInSubDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityMCNumberOfReportedAPsInSubDomain.setStatus("current")
_CLMobilityMCMacAddress_Type = MacAddress
_CLMobilityMCMacAddress_Object = MibScalar
cLMobilityMCMacAddress = _CLMobilityMCMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 8, 19),
    _CLMobilityMCMacAddress_Type()
)
cLMobilityMCMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLMobilityMCMacAddress.setStatus("current")
_CLMobilityGroupMembersOperTable_Object = MibTable
cLMobilityGroupMembersOperTable = _CLMobilityGroupMembersOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 9)
)
if mibBuilder.loadTexts:
    cLMobilityGroupMembersOperTable.setStatus("current")
_CLMobilityGroupMembersOperEntry_Object = MibTableRow
cLMobilityGroupMembersOperEntry = _CLMobilityGroupMembersOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 9, 1)
)
cLMobilityGroupMembersOperEntry.setIndexNames(
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMembersOperNodeAddressType"),
    (0, "CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMembersOperNodeAddress"),
)
if mibBuilder.loadTexts:
    cLMobilityGroupMembersOperEntry.setStatus("current")
_CLMobilityGroupMembersOperNodeAddressType_Type = InetAddressType
_CLMobilityGroupMembersOperNodeAddressType_Object = MibTableColumn
cLMobilityGroupMembersOperNodeAddressType = _CLMobilityGroupMembersOperNodeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 9, 1, 1),
    _CLMobilityGroupMembersOperNodeAddressType_Type()
)
cLMobilityGroupMembersOperNodeAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityGroupMembersOperNodeAddressType.setStatus("current")


class _CLMobilityGroupMembersOperNodeAddress_Type(InetAddress):
    """Custom type cLMobilityGroupMembersOperNodeAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CLMobilityGroupMembersOperNodeAddress_Type.__name__ = "InetAddress"
_CLMobilityGroupMembersOperNodeAddress_Object = MibTableColumn
cLMobilityGroupMembersOperNodeAddress = _CLMobilityGroupMembersOperNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 9, 1, 2),
    _CLMobilityGroupMembersOperNodeAddress_Type()
)
cLMobilityGroupMembersOperNodeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLMobilityGroupMembersOperNodeAddress.setStatus("current")
_CLMobilityGroupMembersOperTunnelStatus_Type = Integer32
_CLMobilityGroupMembersOperTunnelStatus_Object = MibTableColumn
cLMobilityGroupMembersOperTunnelStatus = _CLMobilityGroupMembersOperTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 9, 1, 3),
    _CLMobilityGroupMembersOperTunnelStatus_Type()
)
cLMobilityGroupMembersOperTunnelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityGroupMembersOperTunnelStatus.setStatus("current")
_CLMobilityGroupMembersOperDataPathStatus_Type = TruthValue
_CLMobilityGroupMembersOperDataPathStatus_Object = MibTableColumn
cLMobilityGroupMembersOperDataPathStatus = _CLMobilityGroupMembersOperDataPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 9, 1, 4),
    _CLMobilityGroupMembersOperDataPathStatus_Type()
)
cLMobilityGroupMembersOperDataPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityGroupMembersOperDataPathStatus.setStatus("current")
_CLMobilityGroupMembersOperControlPathStatus_Type = TruthValue
_CLMobilityGroupMembersOperControlPathStatus_Object = MibTableColumn
cLMobilityGroupMembersOperControlPathStatus = _CLMobilityGroupMembersOperControlPathStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 1, 9, 1, 5),
    _CLMobilityGroupMembersOperControlPathStatus_Type()
)
cLMobilityGroupMembersOperControlPathStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLMobilityGroupMembersOperControlPathStatus.setStatus("current")
_CiscoLwappMobilityMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityMIBConform = _CiscoLwappMobilityMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2)
)
_CiscoLwappMobilityMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityMIBCompliances = _CiscoLwappMobilityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 1)
)
_CiscoLwappMobilityMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappMobilityMIBGroups = _CiscoLwappMobilityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2)
)

# Managed Objects groups

cLNplus1RedundancyRev01ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 1)
)
cLNplus1RedundancyRev01ConfigGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorGroupKeepAliveNumber"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorGroupKeepAliveInterval"))
)
if mibBuilder.loadTexts:
    cLNplus1RedundancyRev01ConfigGroup.setStatus("current")

cLNplus1RedundancyRev01StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 2)
)
cLNplus1RedundancyRev01StatusGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorRowStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorWlanId"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddress"))
)
if mibBuilder.loadTexts:
    cLNplus1RedundancyRev01StatusGroup.setStatus("current")

cLSymmetricTunnelingRev01ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 4)
)
cLSymmetricTunnelingRev01ConfigGroup.setObjects(
    ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorSmtStatus")
)
if mibBuilder.loadTexts:
    cLSymmetricTunnelingRev01ConfigGroup.setStatus("current")

cLSymmetricTunnelingRev01StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 5)
)
cLSymmetricTunnelingRev01StatusGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorCurrentSmt"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorDscpValue"))
)
if mibBuilder.loadTexts:
    cLSymmetricTunnelingRev01StatusGroup.setStatus("current")

cLMobilityGroupRev01ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 6)
)
cLMobilityGroupRev01ConfigGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMulticastMessagingEnable"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMulticastGroupIPAddress"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMulticastGroupIPAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberIPAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberIPAddress"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberControlPathStatusUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberDataPathStatusUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityForeignWlcMapIf"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityForeignWlcMapRowStatus"))
)
if mibBuilder.loadTexts:
    cLMobilityGroupRev01ConfigGroup.setStatus("deprecated")

cLMobilityGroupMemberRev02StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 7)
)
cLMobilityGroupMemberRev02StatusGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMulticastGroupIPAddress"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMulticastGroupIPAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberControlPathStatusUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberDataPathStatusUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityIncomingCount"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityOutgoingCount"))
)
if mibBuilder.loadTexts:
    cLMobilityGroupMemberRev02StatusGroup.setStatus("current")

cLMobilityGroupMemberRev02ConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 8)
)
cLMobilityGroupMemberRev02ConfigGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMulticastMessagingEnable"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMulticastGroupIPAddress"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMulticastGroupIPAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberControlPathStatusUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberDataPathStatusUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberHashKey"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberAddress"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberGroupName"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberRowStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityForeignWlcMapIf"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityForeignWlcMapRowStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberDataDtls"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberIPAddressTypeRev1"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberIPAddressRev1"))
)
if mibBuilder.loadTexts:
    cLMobilityGroupMemberRev02ConfigGroup.setStatus("current")

cLMobilityGroupMemberGlobalParametersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 9)
)
cLMobilityGroupMemberGlobalParametersGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCMOEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCMOAdminEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCAdminEnableStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCMulticastMode"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCKeepAliveCount"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCKeepAliveInterval"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCDscpValue"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCMOPublicAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCMOPublicAddress"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCApCountLicensesInUse"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCOwnGroupMulticastAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCOwnGroupMulticastAddress"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCMobilityGroupName"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCMONumberOfClients"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCNumberOfMCs"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCTotalNumberOfReportedAPs"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCNumberOfReportedAPsInSubDomain"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityMCMacAddress"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMembersOperControlPathStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMembersOperTunnelStatus"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMembersOperDataPathStatus"))
)
if mibBuilder.loadTexts:
    cLMobilityGroupMemberGlobalParametersGroup.setStatus("current")


# Notification objects

ciscoLwappMobilityAnchorControlPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 1)
)
ciscoLwappMobilityAnchorControlPathDown.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityAnchorControlPathDown.setStatus(
        "current"
    )

ciscoLwappMobilityAnchorControlPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 2)
)
ciscoLwappMobilityAnchorControlPathUp.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityAnchorControlPathUp.setStatus(
        "current"
    )

ciscoLwappMobilityAnchorDataPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 3)
)
ciscoLwappMobilityAnchorDataPathDown.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityAnchorDataPathDown.setStatus(
        "current"
    )

ciscoLwappMobilityAnchorDataPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 4)
)
ciscoLwappMobilityAnchorDataPathUp.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddressType"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityAnchorDataPathUp.setStatus(
        "current"
    )

ciscoLwappMobilityAllAnchorsOnWlanDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 5)
)
ciscoLwappMobilityAllAnchorsOnWlanDown.setObjects(
    ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorWlanId")
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityAllAnchorsOnWlanDown.setStatus(
        "deprecated"
    )

ciscoLwappMobilityOneAnchorOnWlanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 0, 6)
)
ciscoLwappMobilityOneAnchorOnWlanUp.setObjects(
    ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityAnchorWlanId")
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityOneAnchorOnWlanUp.setStatus(
        "deprecated"
    )


# Notifications groups

cLNplus1RedundancyRev01NotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 3)
)
cLNplus1RedundancyRev01NotifsGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorControlPathDown"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorControlPathUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorDataPathDown"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorDataPathUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAllAnchorsOnWlanDown"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityOneAnchorOnWlanUp"))
)
if mibBuilder.loadTexts:
    cLNplus1RedundancyRev01NotifsGroup.setStatus(
        "deprecated"
    )

cLNplus1RedundancyRev02NotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 2, 10)
)
cLNplus1RedundancyRev02NotifsGroup.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorControlPathDown"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorControlPathUp"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorDataPathDown"),
        ("CISCO-LWAPP-MOBILITY-MIB", "ciscoLwappMobilityAnchorDataPathUp"))
)
if mibBuilder.loadTexts:
    cLNplus1RedundancyRev02NotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappMobilityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 1, 1)
)
ciscoLwappMobilityMIBCompliance.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01StatusGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01NotifsGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLSymmetricTunnelingRev01ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLSymmetricTunnelingRev01StatusGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappMobilityMIBComplianceRev01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 1, 2)
)
ciscoLwappMobilityMIBComplianceRev01.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01StatusGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01NotifsGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLSymmetricTunnelingRev01ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLSymmetricTunnelingRev01StatusGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupRev01ConfigGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityMIBComplianceRev01.setStatus(
        "deprecated"
    )

ciscoLwappMobilityMIBComplianceRev02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 1, 3)
)
ciscoLwappMobilityMIBComplianceRev02.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01StatusGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01NotifsGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLSymmetricTunnelingRev01ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLSymmetricTunnelingRev01StatusGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberRev02ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberRev02StatusGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityMIBComplianceRev02.setStatus(
        "deprecated"
    )

ciscoLwappMobilityMIBComplianceRev03 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 1, 4)
)
ciscoLwappMobilityMIBComplianceRev03.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01StatusGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01NotifsGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLSymmetricTunnelingRev01ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLSymmetricTunnelingRev01StatusGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberRev02ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberRev02StatusGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberGlobalParametersGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityMIBComplianceRev03.setStatus(
        "deprecated"
    )

ciscoLwappMobilityMIBComplianceRev04 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 576, 2, 1, 5)
)
ciscoLwappMobilityMIBComplianceRev04.setObjects(
      *(("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev01StatusGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLNplus1RedundancyRev02NotifsGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLSymmetricTunnelingRev01ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLSymmetricTunnelingRev01StatusGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberRev02ConfigGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberRev02StatusGroup"),
        ("CISCO-LWAPP-MOBILITY-MIB", "cLMobilityGroupMemberGlobalParametersGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappMobilityMIBComplianceRev04.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-MOBILITY-MIB",
    **{"ciscoLwappMobilityMIB": ciscoLwappMobilityMIB,
       "ciscoLwappMobilityMIBNotifs": ciscoLwappMobilityMIBNotifs,
       "ciscoLwappMobilityAnchorControlPathDown": ciscoLwappMobilityAnchorControlPathDown,
       "ciscoLwappMobilityAnchorControlPathUp": ciscoLwappMobilityAnchorControlPathUp,
       "ciscoLwappMobilityAnchorDataPathDown": ciscoLwappMobilityAnchorDataPathDown,
       "ciscoLwappMobilityAnchorDataPathUp": ciscoLwappMobilityAnchorDataPathUp,
       "ciscoLwappMobilityAllAnchorsOnWlanDown": ciscoLwappMobilityAllAnchorsOnWlanDown,
       "ciscoLwappMobilityOneAnchorOnWlanUp": ciscoLwappMobilityOneAnchorOnWlanUp,
       "ciscoLwappMobilityMIBObjects": ciscoLwappMobilityMIBObjects,
       "cLMobilityAnchorTable": cLMobilityAnchorTable,
       "cLMobilityAnchorEntry": cLMobilityAnchorEntry,
       "cLMobilityAnchorWlanProfileName": cLMobilityAnchorWlanProfileName,
       "cLMobilityAnchorSwitchIPAddress": cLMobilityAnchorSwitchIPAddress,
       "cLMobilityAnchorStatus": cLMobilityAnchorStatus,
       "cLMobilityAnchorRowStatus": cLMobilityAnchorRowStatus,
       "cLMobilityAnchorGlobalDot11Config": cLMobilityAnchorGlobalDot11Config,
       "cLMobilityAnchorGroupKeepAliveNumber": cLMobilityAnchorGroupKeepAliveNumber,
       "cLMobilityAnchorGroupKeepAliveInterval": cLMobilityAnchorGroupKeepAliveInterval,
       "cLMobilityAnchorSmtStatus": cLMobilityAnchorSmtStatus,
       "cLMobilityAnchorCurrentSmt": cLMobilityAnchorCurrentSmt,
       "cLMobilityAnchorDscpValue": cLMobilityAnchorDscpValue,
       "cLMobilityTrapVariables": cLMobilityTrapVariables,
       "cLMobilityAnchorWlanId": cLMobilityAnchorWlanId,
       "cLMobilityAnchorAddressType": cLMobilityAnchorAddressType,
       "cLMobilityAnchorAddress": cLMobilityAnchorAddress,
       "cLMobilityMulticastGroupConfig": cLMobilityMulticastGroupConfig,
       "cLMobilityMulticastMessagingEnable": cLMobilityMulticastMessagingEnable,
       "cLMobilityMulticastGroupTable": cLMobilityMulticastGroupTable,
       "cLMobilityMulticastGroupEntry": cLMobilityMulticastGroupEntry,
       "cLMobilityGroupMacAddress": cLMobilityGroupMacAddress,
       "cLMobilityMulticastGroupIPAddressType": cLMobilityMulticastGroupIPAddressType,
       "cLMobilityMulticastGroupIPAddress": cLMobilityMulticastGroupIPAddress,
       "cLMobilityGroupMembersTable": cLMobilityGroupMembersTable,
       "cLMobilityGroupMembersEntry": cLMobilityGroupMembersEntry,
       "cLMobilityGroupMemberIPAddressType": cLMobilityGroupMemberIPAddressType,
       "cLMobilityGroupMemberIPAddress": cLMobilityGroupMemberIPAddress,
       "cLMobilityGroupMemberControlPathStatusUp": cLMobilityGroupMemberControlPathStatusUp,
       "cLMobilityGroupMemberDataPathStatusUp": cLMobilityGroupMemberDataPathStatusUp,
       "cLMobilityGroupMemberHashKey": cLMobilityGroupMemberHashKey,
       "cLMobilityGroupMemberAddressType": cLMobilityGroupMemberAddressType,
       "cLMobilityGroupMemberAddress": cLMobilityGroupMemberAddress,
       "cLMobilityGroupMemberGroupName": cLMobilityGroupMemberGroupName,
       "cLMobilityGroupMemberRowStatus": cLMobilityGroupMemberRowStatus,
       "cLMobilityGroupMemberDataDtls": cLMobilityGroupMemberDataDtls,
       "cLMobilityGroupMemberIPAddressTypeRev1": cLMobilityGroupMemberIPAddressTypeRev1,
       "cLMobilityGroupMemberIPAddressRev1": cLMobilityGroupMemberIPAddressRev1,
       "cLMobilityForeignWlcMapTable": cLMobilityForeignWlcMapTable,
       "cLMobilityForeignWlcMapEntry": cLMobilityForeignWlcMapEntry,
       "cLMobilityForeignWlcMapMacAddress": cLMobilityForeignWlcMapMacAddress,
       "cLMobilityForeignWlcMapIf": cLMobilityForeignWlcMapIf,
       "cLMobilityForeignWlcMapRowStatus": cLMobilityForeignWlcMapRowStatus,
       "cLMobilityStats": cLMobilityStats,
       "cLMobilityIncomingCount": cLMobilityIncomingCount,
       "cLMobilityOutgoingCount": cLMobilityOutgoingCount,
       "ciscoLwappMobilityMCGlobalObjects": ciscoLwappMobilityMCGlobalObjects,
       "cLMobilityMCMOEnableStatus": cLMobilityMCMOEnableStatus,
       "cLMobilityMCMOAdminEnableStatus": cLMobilityMCMOAdminEnableStatus,
       "cLMobilityMCEnableStatus": cLMobilityMCEnableStatus,
       "cLMobilityMCAdminEnableStatus": cLMobilityMCAdminEnableStatus,
       "cLMobilityMCMulticastMode": cLMobilityMCMulticastMode,
       "cLMobilityMCKeepAliveCount": cLMobilityMCKeepAliveCount,
       "cLMobilityMCKeepAliveInterval": cLMobilityMCKeepAliveInterval,
       "cLMobilityMCDscpValue": cLMobilityMCDscpValue,
       "cLMobilityMCMOPublicAddressType": cLMobilityMCMOPublicAddressType,
       "cLMobilityMCMOPublicAddress": cLMobilityMCMOPublicAddress,
       "cLMobilityMCApCountLicensesInUse": cLMobilityMCApCountLicensesInUse,
       "cLMobilityMCOwnGroupMulticastAddressType": cLMobilityMCOwnGroupMulticastAddressType,
       "cLMobilityMCOwnGroupMulticastAddress": cLMobilityMCOwnGroupMulticastAddress,
       "cLMobilityMCMobilityGroupName": cLMobilityMCMobilityGroupName,
       "cLMobilityMCMONumberOfClients": cLMobilityMCMONumberOfClients,
       "cLMobilityMCNumberOfMCs": cLMobilityMCNumberOfMCs,
       "cLMobilityMCTotalNumberOfReportedAPs": cLMobilityMCTotalNumberOfReportedAPs,
       "cLMobilityMCNumberOfReportedAPsInSubDomain": cLMobilityMCNumberOfReportedAPsInSubDomain,
       "cLMobilityMCMacAddress": cLMobilityMCMacAddress,
       "cLMobilityGroupMembersOperTable": cLMobilityGroupMembersOperTable,
       "cLMobilityGroupMembersOperEntry": cLMobilityGroupMembersOperEntry,
       "cLMobilityGroupMembersOperNodeAddressType": cLMobilityGroupMembersOperNodeAddressType,
       "cLMobilityGroupMembersOperNodeAddress": cLMobilityGroupMembersOperNodeAddress,
       "cLMobilityGroupMembersOperTunnelStatus": cLMobilityGroupMembersOperTunnelStatus,
       "cLMobilityGroupMembersOperDataPathStatus": cLMobilityGroupMembersOperDataPathStatus,
       "cLMobilityGroupMembersOperControlPathStatus": cLMobilityGroupMembersOperControlPathStatus,
       "ciscoLwappMobilityMIBConform": ciscoLwappMobilityMIBConform,
       "ciscoLwappMobilityMIBCompliances": ciscoLwappMobilityMIBCompliances,
       "ciscoLwappMobilityMIBCompliance": ciscoLwappMobilityMIBCompliance,
       "ciscoLwappMobilityMIBComplianceRev01": ciscoLwappMobilityMIBComplianceRev01,
       "ciscoLwappMobilityMIBComplianceRev02": ciscoLwappMobilityMIBComplianceRev02,
       "ciscoLwappMobilityMIBComplianceRev03": ciscoLwappMobilityMIBComplianceRev03,
       "ciscoLwappMobilityMIBComplianceRev04": ciscoLwappMobilityMIBComplianceRev04,
       "ciscoLwappMobilityMIBGroups": ciscoLwappMobilityMIBGroups,
       "cLNplus1RedundancyRev01ConfigGroup": cLNplus1RedundancyRev01ConfigGroup,
       "cLNplus1RedundancyRev01StatusGroup": cLNplus1RedundancyRev01StatusGroup,
       "cLNplus1RedundancyRev01NotifsGroup": cLNplus1RedundancyRev01NotifsGroup,
       "cLSymmetricTunnelingRev01ConfigGroup": cLSymmetricTunnelingRev01ConfigGroup,
       "cLSymmetricTunnelingRev01StatusGroup": cLSymmetricTunnelingRev01StatusGroup,
       "cLMobilityGroupRev01ConfigGroup": cLMobilityGroupRev01ConfigGroup,
       "cLMobilityGroupMemberRev02StatusGroup": cLMobilityGroupMemberRev02StatusGroup,
       "cLMobilityGroupMemberRev02ConfigGroup": cLMobilityGroupMemberRev02ConfigGroup,
       "cLMobilityGroupMemberGlobalParametersGroup": cLMobilityGroupMemberGlobalParametersGroup,
       "cLNplus1RedundancyRev02NotifsGroup": cLNplus1RedundancyRev02NotifsGroup}
)
