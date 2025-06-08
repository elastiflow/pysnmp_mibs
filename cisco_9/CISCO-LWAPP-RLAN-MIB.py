# SNMP MIB module (CISCO-LWAPP-RLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-RLAN-MIB.mib
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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappRlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 856)
)
if mibBuilder.loadTexts:
    ciscoLwappRlanMIB.setRevisions(
        ("2019-06-21 00:00",
         "2019-04-23 00:00",
         "2018-07-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappRlanMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappRlanMIBNotifs = _CiscoLwappRlanMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 0)
)
_CiscoLwappRlanMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappRlanMIBObjects = _CiscoLwappRlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1)
)
_CiscoLwappRlanConfig_ObjectIdentity = ObjectIdentity
ciscoLwappRlanConfig = _CiscoLwappRlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1)
)
_CLRlanTable_Object = MibTable
cLRlanTable = _CLRlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cLRlanTable.setStatus("current")
_CLRlanEntry_Object = MibTableRow
cLRlanEntry = _CLRlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1)
)
cLRlanEntry.setIndexNames(
    (0, "CISCO-LWAPP-RLAN-MIB", "cLRlanIndex"),
)
if mibBuilder.loadTexts:
    cLRlanEntry.setStatus("current")


class _CLRlanIndex_Type(Unsigned32):
    """Custom type cLRlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CLRlanIndex_Type.__name__ = "Unsigned32"
_CLRlanIndex_Object = MibTableColumn
cLRlanIndex = _CLRlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 1),
    _CLRlanIndex_Type()
)
cLRlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRlanIndex.setStatus("current")
_CLRlanRowStatus_Type = RowStatus
_CLRlanRowStatus_Object = MibTableColumn
cLRlanRowStatus = _CLRlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 2),
    _CLRlanRowStatus_Type()
)
cLRlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRlanRowStatus.setStatus("current")


class _CLRlanProfileName_Type(SnmpAdminString):
    """Custom type cLRlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanProfileName_Type.__name__ = "SnmpAdminString"
_CLRlanProfileName_Object = MibTableColumn
cLRlanProfileName = _CLRlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 3),
    _CLRlanProfileName_Type()
)
cLRlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRlanProfileName.setStatus("current")


class _CLRlanMacFiltering_Type(SnmpAdminString):
    """Custom type cLRlanMacFiltering based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanMacFiltering_Type.__name__ = "SnmpAdminString"
_CLRlanMacFiltering_Object = MibTableColumn
cLRlanMacFiltering = _CLRlanMacFiltering_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 4),
    _CLRlanMacFiltering_Type()
)
cLRlanMacFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanMacFiltering.setStatus("current")


class _CLRlanAuthList_Type(SnmpAdminString):
    """Custom type cLRlanAuthList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanAuthList_Type.__name__ = "SnmpAdminString"
_CLRlanAuthList_Object = MibTableColumn
cLRlanAuthList = _CLRlanAuthList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 5),
    _CLRlanAuthList_Type()
)
cLRlanAuthList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanAuthList.setStatus("current")
_CLRlanSecurity8021X_Type = TruthValue
_CLRlanSecurity8021X_Object = MibTableColumn
cLRlanSecurity8021X = _CLRlanSecurity8021X_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 6),
    _CLRlanSecurity8021X_Type()
)
cLRlanSecurity8021X.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanSecurity8021X.setStatus("current")
_CLRlanSecurityWebAuth_Type = TruthValue
_CLRlanSecurityWebAuth_Object = MibTableColumn
cLRlanSecurityWebAuth = _CLRlanSecurityWebAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 7),
    _CLRlanSecurityWebAuth_Type()
)
cLRlanSecurityWebAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanSecurityWebAuth.setStatus("current")


class _CLRlanEapAuthProfileName_Type(SnmpAdminString):
    """Custom type cLRlanEapAuthProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanEapAuthProfileName_Type.__name__ = "SnmpAdminString"
_CLRlanEapAuthProfileName_Object = MibTableColumn
cLRlanEapAuthProfileName = _CLRlanEapAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 8),
    _CLRlanEapAuthProfileName_Type()
)
cLRlanEapAuthProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanEapAuthProfileName.setStatus("current")


class _CLRlanEapAuthStatus_Type(TruthValue):
    """Custom type cLRlanEapAuthStatus based on TruthValue"""
    defaultValue = 2


_CLRlanEapAuthStatus_Type.__name__ = "TruthValue"
_CLRlanEapAuthStatus_Object = MibTableColumn
cLRlanEapAuthStatus = _CLRlanEapAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 9),
    _CLRlanEapAuthStatus_Type()
)
cLRlanEapAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanEapAuthStatus.setStatus("current")


class _CLRlanWebAuthParameter_Type(SnmpAdminString):
    """Custom type cLRlanWebAuthParameter based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanWebAuthParameter_Type.__name__ = "SnmpAdminString"
_CLRlanWebAuthParameter_Object = MibTableColumn
cLRlanWebAuthParameter = _CLRlanWebAuthParameter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 10),
    _CLRlanWebAuthParameter_Type()
)
cLRlanWebAuthParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLRlanWebAuthParameter.setStatus("current")


class _CLRlanClientLimit_Type(Unsigned32):
    """Custom type cLRlanClientLimit based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CLRlanClientLimit_Type.__name__ = "Unsigned32"
_CLRlanClientLimit_Object = MibTableColumn
cLRlanClientLimit = _CLRlanClientLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 11),
    _CLRlanClientLimit_Type()
)
cLRlanClientLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanClientLimit.setStatus("current")


class _CLRlanStatus_Type(TruthValue):
    """Custom type cLRlanStatus based on TruthValue"""
    defaultValue = 2


_CLRlanStatus_Type.__name__ = "TruthValue"
_CLRlanStatus_Object = MibTableColumn
cLRlanStatus = _CLRlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 12),
    _CLRlanStatus_Type()
)
cLRlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanStatus.setStatus("current")


class _CLRlanWebAuthIpv4Acl_Type(SnmpAdminString):
    """Custom type cLRlanWebAuthIpv4Acl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanWebAuthIpv4Acl_Type.__name__ = "SnmpAdminString"
_CLRlanWebAuthIpv4Acl_Object = MibTableColumn
cLRlanWebAuthIpv4Acl = _CLRlanWebAuthIpv4Acl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 13),
    _CLRlanWebAuthIpv4Acl_Type()
)
cLRlanWebAuthIpv4Acl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanWebAuthIpv4Acl.setStatus("current")


class _CLRlanWebAuthIpv6Acl_Type(SnmpAdminString):
    """Custom type cLRlanWebAuthIpv6Acl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanWebAuthIpv6Acl_Type.__name__ = "SnmpAdminString"
_CLRlanWebAuthIpv6Acl_Object = MibTableColumn
cLRlanWebAuthIpv6Acl = _CLRlanWebAuthIpv6Acl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 14),
    _CLRlanWebAuthIpv6Acl_Type()
)
cLRlanWebAuthIpv6Acl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanWebAuthIpv6Acl.setStatus("current")


class _CLRlanSecurity8021XAuthList_Type(SnmpAdminString):
    """Custom type cLRlanSecurity8021XAuthList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanSecurity8021XAuthList_Type.__name__ = "SnmpAdminString"
_CLRlanSecurity8021XAuthList_Object = MibTableColumn
cLRlanSecurity8021XAuthList = _CLRlanSecurity8021XAuthList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 15),
    _CLRlanSecurity8021XAuthList_Type()
)
cLRlanSecurity8021XAuthList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanSecurity8021XAuthList.setStatus("current")


class _CLRlanMdnsMode_Type(Integer32):
    """Custom type cLRlanMdnsMode based on Integer32"""
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
        *(("bridge", 0),
          ("drop", 1),
          ("gateway", 2))
    )


_CLRlanMdnsMode_Type.__name__ = "Integer32"
_CLRlanMdnsMode_Object = MibTableColumn
cLRlanMdnsMode = _CLRlanMdnsMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 1, 1, 16),
    _CLRlanMdnsMode_Type()
)
cLRlanMdnsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanMdnsMode.setStatus("current")
_CLRlanPolicyTable_Object = MibTable
cLRlanPolicyTable = _CLRlanPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cLRlanPolicyTable.setStatus("current")
_CLRlanPolicyEntry_Object = MibTableRow
cLRlanPolicyEntry = _CLRlanPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1)
)
cLRlanPolicyEntry.setIndexNames(
    (0, "CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyProfileName"),
)
if mibBuilder.loadTexts:
    cLRlanPolicyEntry.setStatus("current")


class _CLRlanPolicyProfileName_Type(SnmpAdminString):
    """Custom type cLRlanPolicyProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanPolicyProfileName_Type.__name__ = "SnmpAdminString"
_CLRlanPolicyProfileName_Object = MibTableColumn
cLRlanPolicyProfileName = _CLRlanPolicyProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 1),
    _CLRlanPolicyProfileName_Type()
)
cLRlanPolicyProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLRlanPolicyProfileName.setStatus("current")
_CLRlanPolicyRowStatus_Type = RowStatus
_CLRlanPolicyRowStatus_Object = MibTableColumn
cLRlanPolicyRowStatus = _CLRlanPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 2),
    _CLRlanPolicyRowStatus_Type()
)
cLRlanPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLRlanPolicyRowStatus.setStatus("current")


class _CLRlanPolicyStatus_Type(TruthValue):
    """Custom type cLRlanPolicyStatus based on TruthValue"""
    defaultValue = 2


_CLRlanPolicyStatus_Type.__name__ = "TruthValue"
_CLRlanPolicyStatus_Object = MibTableColumn
cLRlanPolicyStatus = _CLRlanPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 3),
    _CLRlanPolicyStatus_Type()
)
cLRlanPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanPolicyStatus.setStatus("current")


class _CLRlanPolicyDesc_Type(SnmpAdminString):
    """Custom type cLRlanPolicyDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanPolicyDesc_Type.__name__ = "SnmpAdminString"
_CLRlanPolicyDesc_Object = MibTableColumn
cLRlanPolicyDesc = _CLRlanPolicyDesc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 4),
    _CLRlanPolicyDesc_Type()
)
cLRlanPolicyDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanPolicyDesc.setStatus("current")


class _CLRlanPolicyIpv4Acl_Type(SnmpAdminString):
    """Custom type cLRlanPolicyIpv4Acl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanPolicyIpv4Acl_Type.__name__ = "SnmpAdminString"
_CLRlanPolicyIpv4Acl_Object = MibTableColumn
cLRlanPolicyIpv4Acl = _CLRlanPolicyIpv4Acl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 5),
    _CLRlanPolicyIpv4Acl_Type()
)
cLRlanPolicyIpv4Acl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanPolicyIpv4Acl.setStatus("current")


class _CLRlanPolicyIpv6Acl_Type(SnmpAdminString):
    """Custom type cLRlanPolicyIpv6Acl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanPolicyIpv6Acl_Type.__name__ = "SnmpAdminString"
_CLRlanPolicyIpv6Acl_Object = MibTableColumn
cLRlanPolicyIpv6Acl = _CLRlanPolicyIpv6Acl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 6),
    _CLRlanPolicyIpv6Acl_Type()
)
cLRlanPolicyIpv6Acl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanPolicyIpv6Acl.setStatus("current")


class _CLRlanAAAOverride_Type(TruthValue):
    """Custom type cLRlanAAAOverride based on TruthValue"""
    defaultValue = 2


_CLRlanAAAOverride_Type.__name__ = "TruthValue"
_CLRlanAAAOverride_Object = MibTableColumn
cLRlanAAAOverride = _CLRlanAAAOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 7),
    _CLRlanAAAOverride_Type()
)
cLRlanAAAOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanAAAOverride.setStatus("current")


class _CLRlanCentralSwitching_Type(TruthValue):
    """Custom type cLRlanCentralSwitching based on TruthValue"""
    defaultValue = 1


_CLRlanCentralSwitching_Type.__name__ = "TruthValue"
_CLRlanCentralSwitching_Object = MibTableColumn
cLRlanCentralSwitching = _CLRlanCentralSwitching_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 8),
    _CLRlanCentralSwitching_Type()
)
cLRlanCentralSwitching.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanCentralSwitching.setStatus("current")


class _CLRlanInterface_Type(SnmpAdminString):
    """Custom type cLRlanInterface based on SnmpAdminString"""
    defaultValue = OctetString("1")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanInterface_Type.__name__ = "SnmpAdminString"
_CLRlanInterface_Object = MibTableColumn
cLRlanInterface = _CLRlanInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 9),
    _CLRlanInterface_Type()
)
cLRlanInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanInterface.setStatus("current")
_CLRlanPoeEnabled_Type = TruthValue
_CLRlanPoeEnabled_Object = MibTableColumn
cLRlanPoeEnabled = _CLRlanPoeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 10),
    _CLRlanPoeEnabled_Type()
)
cLRlanPoeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanPoeEnabled.setStatus("current")


class _CLRlanHostMode_Type(Integer32):
    """Custom type cLRlanHostMode based on Integer32"""
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
        *(("sinlgeHostMode", 0),
          ("multiHostMode", 1),
          ("multiDomainMode", 2))
    )


_CLRlanHostMode_Type.__name__ = "Integer32"
_CLRlanHostMode_Object = MibTableColumn
cLRlanHostMode = _CLRlanHostMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 11),
    _CLRlanHostMode_Type()
)
cLRlanHostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanHostMode.setStatus("current")


class _CLRlanViolationMode_Type(Integer32):
    """Custom type cLRlanViolationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protect", 0),
          ("replace", 1),
          ("shutdown", 2))
    )


_CLRlanViolationMode_Type.__name__ = "Integer32"
_CLRlanViolationMode_Object = MibTableColumn
cLRlanViolationMode = _CLRlanViolationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 12),
    _CLRlanViolationMode_Type()
)
cLRlanViolationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanViolationMode.setStatus("current")
_CLRlanVoiceVlanId_Type = Unsigned32
_CLRlanVoiceVlanId_Object = MibTableColumn
cLRlanVoiceVlanId = _CLRlanVoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 13),
    _CLRlanVoiceVlanId_Type()
)
cLRlanVoiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanVoiceVlanId.setStatus("current")
_CLRlanDataVlanId_Type = Unsigned32
_CLRlanDataVlanId_Object = MibTableColumn
cLRlanDataVlanId = _CLRlanDataVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 14),
    _CLRlanDataVlanId_Type()
)
cLRlanDataVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanDataVlanId.setStatus("current")


class _CLRlanBlacklistEnabled_Type(TruthValue):
    """Custom type cLRlanBlacklistEnabled based on TruthValue"""
    defaultValue = 1


_CLRlanBlacklistEnabled_Type.__name__ = "TruthValue"
_CLRlanBlacklistEnabled_Object = MibTableColumn
cLRlanBlacklistEnabled = _CLRlanBlacklistEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 15),
    _CLRlanBlacklistEnabled_Type()
)
cLRlanBlacklistEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanBlacklistEnabled.setStatus("current")


class _CLRlanBlacklistTimeout_Type(Unsigned32):
    """Custom type cLRlanBlacklistTimeout based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CLRlanBlacklistTimeout_Type.__name__ = "Unsigned32"
_CLRlanBlacklistTimeout_Object = MibTableColumn
cLRlanBlacklistTimeout = _CLRlanBlacklistTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 16),
    _CLRlanBlacklistTimeout_Type()
)
cLRlanBlacklistTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanBlacklistTimeout.setStatus("current")


class _CLRlanAAAPolicyName_Type(SnmpAdminString):
    """Custom type cLRlanAAAPolicyName based on SnmpAdminString"""
    defaultValue = OctetString("default-aaa-policy")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanAAAPolicyName_Type.__name__ = "SnmpAdminString"
_CLRlanAAAPolicyName_Object = MibTableColumn
cLRlanAAAPolicyName = _CLRlanAAAPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 17),
    _CLRlanAAAPolicyName_Type()
)
cLRlanAAAPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanAAAPolicyName.setStatus("current")


class _CLRlanSessionTimeout_Type(Unsigned32):
    """Custom type cLRlanSessionTimeout based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 86400),
    )


_CLRlanSessionTimeout_Type.__name__ = "Unsigned32"
_CLRlanSessionTimeout_Object = MibTableColumn
cLRlanSessionTimeout = _CLRlanSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 18),
    _CLRlanSessionTimeout_Type()
)
cLRlanSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanSessionTimeout.setStatus("current")
_CLRlanPreAuthEnabled_Type = TruthValue
_CLRlanPreAuthEnabled_Object = MibTableColumn
cLRlanPreAuthEnabled = _CLRlanPreAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 19),
    _CLRlanPreAuthEnabled_Type()
)
cLRlanPreAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanPreAuthEnabled.setStatus("current")
_CLRlanDhcpServerType_Type = InetAddressType
_CLRlanDhcpServerType_Object = MibTableColumn
cLRlanDhcpServerType = _CLRlanDhcpServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 20),
    _CLRlanDhcpServerType_Type()
)
cLRlanDhcpServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanDhcpServerType.setStatus("current")
_CLRlanDhcpServer_Type = InetAddress
_CLRlanDhcpServer_Object = MibTableColumn
cLRlanDhcpServer = _CLRlanDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 21),
    _CLRlanDhcpServer_Type()
)
cLRlanDhcpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanDhcpServer.setStatus("current")
_CLRlanRadiusHttpProfiling_Type = TruthValue
_CLRlanRadiusHttpProfiling_Object = MibTableColumn
cLRlanRadiusHttpProfiling = _CLRlanRadiusHttpProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 22),
    _CLRlanRadiusHttpProfiling_Type()
)
cLRlanRadiusHttpProfiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanRadiusHttpProfiling.setStatus("deprecated")
_CLRlanRadiusDhcpProfiling_Type = TruthValue
_CLRlanRadiusDhcpProfiling_Object = MibTableColumn
cLRlanRadiusDhcpProfiling = _CLRlanRadiusDhcpProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 23),
    _CLRlanRadiusDhcpProfiling_Type()
)
cLRlanRadiusDhcpProfiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanRadiusDhcpProfiling.setStatus("deprecated")
_CLRlanLocalHttpProfiling_Type = TruthValue
_CLRlanLocalHttpProfiling_Object = MibTableColumn
cLRlanLocalHttpProfiling = _CLRlanLocalHttpProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 24),
    _CLRlanLocalHttpProfiling_Type()
)
cLRlanLocalHttpProfiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanLocalHttpProfiling.setStatus("deprecated")
_CLRlanLocalDhcpProfiling_Type = TruthValue
_CLRlanLocalDhcpProfiling_Object = MibTableColumn
cLRlanLocalDhcpProfiling = _CLRlanLocalDhcpProfiling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 25),
    _CLRlanLocalDhcpProfiling_Type()
)
cLRlanLocalDhcpProfiling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanLocalDhcpProfiling.setStatus("deprecated")
_CLRlanIpv6IngressStatus_Type = TruthValue
_CLRlanIpv6IngressStatus_Object = MibTableColumn
cLRlanIpv6IngressStatus = _CLRlanIpv6IngressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 26),
    _CLRlanIpv6IngressStatus_Type()
)
cLRlanIpv6IngressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanIpv6IngressStatus.setStatus("current")
_CLRlanIpv6EgressStatus_Type = TruthValue
_CLRlanIpv6EgressStatus_Object = MibTableColumn
cLRlanIpv6EgressStatus = _CLRlanIpv6EgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 27),
    _CLRlanIpv6EgressStatus_Type()
)
cLRlanIpv6EgressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanIpv6EgressStatus.setStatus("current")
_CLRlanIpv4IngressStatus_Type = TruthValue
_CLRlanIpv4IngressStatus_Object = MibTableColumn
cLRlanIpv4IngressStatus = _CLRlanIpv4IngressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 28),
    _CLRlanIpv4IngressStatus_Type()
)
cLRlanIpv4IngressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanIpv4IngressStatus.setStatus("current")
_CLRlanIpv4EgressStatus_Type = TruthValue
_CLRlanIpv4EgressStatus_Object = MibTableColumn
cLRlanIpv4EgressStatus = _CLRlanIpv4EgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 29),
    _CLRlanIpv4EgressStatus_Type()
)
cLRlanIpv4EgressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanIpv4EgressStatus.setStatus("current")


class _CLRlanIpv6IngressName_Type(SnmpAdminString):
    """Custom type cLRlanIpv6IngressName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanIpv6IngressName_Type.__name__ = "SnmpAdminString"
_CLRlanIpv6IngressName_Object = MibTableColumn
cLRlanIpv6IngressName = _CLRlanIpv6IngressName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 30),
    _CLRlanIpv6IngressName_Type()
)
cLRlanIpv6IngressName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanIpv6IngressName.setStatus("current")


class _CLRlanIpv6EgressName_Type(SnmpAdminString):
    """Custom type cLRlanIpv6EgressName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanIpv6EgressName_Type.__name__ = "SnmpAdminString"
_CLRlanIpv6EgressName_Object = MibTableColumn
cLRlanIpv6EgressName = _CLRlanIpv6EgressName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 31),
    _CLRlanIpv6EgressName_Type()
)
cLRlanIpv6EgressName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanIpv6EgressName.setStatus("current")


class _CLRlanIpv4IngressName_Type(SnmpAdminString):
    """Custom type cLRlanIpv4IngressName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanIpv4IngressName_Type.__name__ = "SnmpAdminString"
_CLRlanIpv4IngressName_Object = MibTableColumn
cLRlanIpv4IngressName = _CLRlanIpv4IngressName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 32),
    _CLRlanIpv4IngressName_Type()
)
cLRlanIpv4IngressName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanIpv4IngressName.setStatus("current")


class _CLRlanIpv4EgressName_Type(SnmpAdminString):
    """Custom type cLRlanIpv4EgressName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanIpv4EgressName_Type.__name__ = "SnmpAdminString"
_CLRlanIpv4EgressName_Object = MibTableColumn
cLRlanIpv4EgressName = _CLRlanIpv4EgressName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 33),
    _CLRlanIpv4EgressName_Type()
)
cLRlanIpv4EgressName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanIpv4EgressName.setStatus("current")
_CLRlanSplitTunnelGatewayType_Type = InetAddressType
_CLRlanSplitTunnelGatewayType_Object = MibTableColumn
cLRlanSplitTunnelGatewayType = _CLRlanSplitTunnelGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 34),
    _CLRlanSplitTunnelGatewayType_Type()
)
cLRlanSplitTunnelGatewayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanSplitTunnelGatewayType.setStatus("current")
_CLRlanSplitTunnelGateway_Type = InetAddress
_CLRlanSplitTunnelGateway_Object = MibTableColumn
cLRlanSplitTunnelGateway = _CLRlanSplitTunnelGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 35),
    _CLRlanSplitTunnelGateway_Type()
)
cLRlanSplitTunnelGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanSplitTunnelGateway.setStatus("current")
_CLRlanSplitTunnelNetmaskType_Type = InetAddressType
_CLRlanSplitTunnelNetmaskType_Object = MibTableColumn
cLRlanSplitTunnelNetmaskType = _CLRlanSplitTunnelNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 36),
    _CLRlanSplitTunnelNetmaskType_Type()
)
cLRlanSplitTunnelNetmaskType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanSplitTunnelNetmaskType.setStatus("current")
_CLRlanSplitTunnelNetmask_Type = InetAddress
_CLRlanSplitTunnelNetmask_Object = MibTableColumn
cLRlanSplitTunnelNetmask = _CLRlanSplitTunnelNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 37),
    _CLRlanSplitTunnelNetmask_Type()
)
cLRlanSplitTunnelNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanSplitTunnelNetmask.setStatus("current")
_CLRlanSplitTunnel_Type = TruthValue
_CLRlanSplitTunnel_Object = MibTableColumn
cLRlanSplitTunnel = _CLRlanSplitTunnel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 38),
    _CLRlanSplitTunnel_Type()
)
cLRlanSplitTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanSplitTunnel.setStatus("current")


class _CLRlanAclName_Type(SnmpAdminString):
    """Custom type cLRlanAclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanAclName_Type.__name__ = "SnmpAdminString"
_CLRlanAclName_Object = MibTableColumn
cLRlanAclName = _CLRlanAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 39),
    _CLRlanAclName_Type()
)
cLRlanAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanAclName.setStatus("current")
_CLRlanSplitTunnelOverride_Type = TruthValue
_CLRlanSplitTunnelOverride_Object = MibTableColumn
cLRlanSplitTunnelOverride = _CLRlanSplitTunnelOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 40),
    _CLRlanSplitTunnelOverride_Type()
)
cLRlanSplitTunnelOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanSplitTunnelOverride.setStatus("current")


class _CLRlanAccountingList_Type(SnmpAdminString):
    """Custom type cLRlanAccountingList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLRlanAccountingList_Type.__name__ = "SnmpAdminString"
_CLRlanAccountingList_Object = MibTableColumn
cLRlanAccountingList = _CLRlanAccountingList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 41),
    _CLRlanAccountingList_Type()
)
cLRlanAccountingList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanAccountingList.setStatus("current")


class _CLRlanDhcpEnabled_Type(TruthValue):
    """Custom type cLRlanDhcpEnabled based on TruthValue"""
    defaultValue = 2


_CLRlanDhcpEnabled_Type.__name__ = "TruthValue"
_CLRlanDhcpEnabled_Object = MibTableColumn
cLRlanDhcpEnabled = _CLRlanDhcpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 42),
    _CLRlanDhcpEnabled_Type()
)
cLRlanDhcpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanDhcpEnabled.setStatus("current")


class _CLRlanCentralDhcp_Type(TruthValue):
    """Custom type cLRlanCentralDhcp based on TruthValue"""
    defaultValue = 1


_CLRlanCentralDhcp_Type.__name__ = "TruthValue"
_CLRlanCentralDhcp_Object = MibTableColumn
cLRlanCentralDhcp = _CLRlanCentralDhcp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 43),
    _CLRlanCentralDhcp_Type()
)
cLRlanCentralDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanCentralDhcp.setStatus("current")


class _CLRlanMdnsPolicy_Type(SnmpAdminString):
    """Custom type cLRlanMdnsPolicy based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CLRlanMdnsPolicy_Type.__name__ = "SnmpAdminString"
_CLRlanMdnsPolicy_Object = MibTableColumn
cLRlanMdnsPolicy = _CLRlanMdnsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 44),
    _CLRlanMdnsPolicy_Type()
)
cLRlanMdnsPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanMdnsPolicy.setStatus("current")
_CLRlanPowerLevelId_Type = Unsigned32
_CLRlanPowerLevelId_Object = MibTableColumn
cLRlanPowerLevelId = _CLRlanPowerLevelId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 1, 1, 2, 1, 45),
    _CLRlanPowerLevelId_Type()
)
cLRlanPowerLevelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLRlanPowerLevelId.setStatus("current")
_CiscoLwappRlanConform_ObjectIdentity = ObjectIdentity
ciscoLwappRlanConform = _CiscoLwappRlanConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2)
)
_CiscoLwappRlanCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappRlanCompliances = _CiscoLwappRlanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 1)
)
_CiscoLwappRlanGroups_ObjectIdentity = ObjectIdentity
ciscoLwappRlanGroups = _CiscoLwappRlanGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 2)
)

# Managed Objects groups

ciscoLwappRlanConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 2, 1)
)
ciscoLwappRlanConfigGroup1.setObjects(
      *(("CISCO-LWAPP-RLAN-MIB", "cLRlanRowStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanProfileName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanMacFiltering"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAuthList"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSecurity8021X"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSecurityWebAuth"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanEapAuthProfileName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanEapAuthStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanWebAuthParameter"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanClientLimit"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanWebAuthIpv4Acl"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanWebAuthIpv6Acl"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSecurity8021XAuthList"))
)
if mibBuilder.loadTexts:
    ciscoLwappRlanConfigGroup1.setStatus("current")

ciscoLwappRlanConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 2, 2)
)
ciscoLwappRlanConfigGroup2.setObjects(
      *(("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyRowStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyDesc"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyIpv4Acl"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyIpv6Acl"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAAAOverride"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanCentralSwitching"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanInterface"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPoeEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanHostMode"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanViolationMode"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanVoiceVlanId"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDataVlanId"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanBlacklistEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanBlacklistTimeout"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAAAPolicyName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSessionTimeout"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPreAuthEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDhcpServerType"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDhcpServer"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanRadiusHttpProfiling"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanRadiusDhcpProfiling"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanLocalHttpProfiling"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanLocalDhcpProfiling"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6IngressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6EgressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4IngressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4EgressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6IngressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6EgressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4IngressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4EgressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelGatewayType"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelGateway"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelNetmaskType"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelNetmask"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnel"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAclName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelOverride"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAccountingList"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDhcpEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanCentralDhcp"))
)
if mibBuilder.loadTexts:
    ciscoLwappRlanConfigGroup2.setStatus("deprecated")

ciscoLwappRlanConfigGroup2Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 2, 3)
)
ciscoLwappRlanConfigGroup2Sup1.setObjects(
      *(("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyRowStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyDesc"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyIpv4Acl"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyIpv6Acl"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAAAOverride"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanCentralSwitching"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanInterface"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPoeEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanHostMode"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanViolationMode"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanVoiceVlanId"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDataVlanId"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanBlacklistEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanBlacklistTimeout"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAAAPolicyName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSessionTimeout"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPreAuthEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDhcpServerType"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDhcpServer"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6IngressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6EgressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4IngressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4EgressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6IngressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6EgressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4IngressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4EgressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelGatewayType"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelGateway"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelNetmaskType"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelNetmask"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnel"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAclName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelOverride"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAccountingList"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDhcpEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanCentralDhcp"))
)
if mibBuilder.loadTexts:
    ciscoLwappRlanConfigGroup2Sup1.setStatus("deprecated")

ciscoLwappRlanConfigGroup2Sup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 2, 4)
)
ciscoLwappRlanConfigGroup2Sup2.setObjects(
      *(("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyRowStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyDesc"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyIpv4Acl"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPolicyIpv6Acl"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAAAOverride"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanCentralSwitching"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanInterface"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPoeEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanHostMode"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanViolationMode"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanVoiceVlanId"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDataVlanId"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanBlacklistEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanBlacklistTimeout"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAAAPolicyName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSessionTimeout"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanPreAuthEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDhcpServerType"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDhcpServer"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6IngressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6EgressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4IngressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4EgressStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6IngressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv6EgressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4IngressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanIpv4EgressName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelGatewayType"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelGateway"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelNetmaskType"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelNetmask"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnel"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAclName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSplitTunnelOverride"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAccountingList"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanDhcpEnabled"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanCentralDhcp"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanMdnsPolicy"))
)
if mibBuilder.loadTexts:
    ciscoLwappRlanConfigGroup2Sup2.setStatus("current")

ciscoLwappRlanConfigGroup1Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 2, 5)
)
ciscoLwappRlanConfigGroup1Sup1.setObjects(
      *(("CISCO-LWAPP-RLAN-MIB", "cLRlanRowStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanProfileName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanMacFiltering"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanAuthList"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSecurity8021X"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSecurityWebAuth"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanEapAuthProfileName"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanEapAuthStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanWebAuthParameter"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanClientLimit"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanStatus"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanWebAuthIpv4Acl"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanWebAuthIpv6Acl"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanSecurity8021XAuthList"),
        ("CISCO-LWAPP-RLAN-MIB", "cLRlanMdnsMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappRlanConfigGroup1Sup1.setStatus("current")

ciscoLwappRlanConfigGroup2Sup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 2, 6)
)
ciscoLwappRlanConfigGroup2Sup3.setObjects(
    ("CISCO-LWAPP-RLAN-MIB", "cLRlanPowerLevelId")
)
if mibBuilder.loadTexts:
    ciscoLwappRlanConfigGroup2Sup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappRlanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 1, 1)
)
ciscoLwappRlanCompliance.setObjects(
      *(("CISCO-LWAPP-RLAN-MIB", "ciscoLwappRlanConfigGroup1"),
        ("CISCO-LWAPP-RLAN-MIB", "ciscoLwappRlanConfigGroup2"))
)
if mibBuilder.loadTexts:
    ciscoLwappRlanCompliance.setStatus(
        "deprecated"
    )

ciscoLwappRlanComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 1, 2)
)
ciscoLwappRlanComplianceRev1.setObjects(
      *(("CISCO-LWAPP-RLAN-MIB", "ciscoLwappRlanConfigGroup1"),
        ("CISCO-LWAPP-RLAN-MIB", "ciscoLwappRlanConfigGroup2Sup1"))
)
if mibBuilder.loadTexts:
    ciscoLwappRlanComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappRlanComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 1, 3)
)
ciscoLwappRlanComplianceRev2.setObjects(
      *(("CISCO-LWAPP-RLAN-MIB", "ciscoLwappRlanConfigGroup1Sup1"),
        ("CISCO-LWAPP-RLAN-MIB", "ciscoLwappRlanConfigGroup2Sup2"))
)
if mibBuilder.loadTexts:
    ciscoLwappRlanComplianceRev2.setStatus(
        "deprecated"
    )

ciscoLwappRlanComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 856, 2, 1, 4)
)
ciscoLwappRlanComplianceRev3.setObjects(
      *(("CISCO-LWAPP-RLAN-MIB", "ciscoLwappRlanConfigGroup1Sup1"),
        ("CISCO-LWAPP-RLAN-MIB", "ciscoLwappRlanConfigGroup2Sup2"),
        ("CISCO-LWAPP-RLAN-MIB", "ciscoLwappRlanConfigGroup2Sup3"))
)
if mibBuilder.loadTexts:
    ciscoLwappRlanComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-RLAN-MIB",
    **{"ciscoLwappRlanMIB": ciscoLwappRlanMIB,
       "ciscoLwappRlanMIBNotifs": ciscoLwappRlanMIBNotifs,
       "ciscoLwappRlanMIBObjects": ciscoLwappRlanMIBObjects,
       "ciscoLwappRlanConfig": ciscoLwappRlanConfig,
       "cLRlanTable": cLRlanTable,
       "cLRlanEntry": cLRlanEntry,
       "cLRlanIndex": cLRlanIndex,
       "cLRlanRowStatus": cLRlanRowStatus,
       "cLRlanProfileName": cLRlanProfileName,
       "cLRlanMacFiltering": cLRlanMacFiltering,
       "cLRlanAuthList": cLRlanAuthList,
       "cLRlanSecurity8021X": cLRlanSecurity8021X,
       "cLRlanSecurityWebAuth": cLRlanSecurityWebAuth,
       "cLRlanEapAuthProfileName": cLRlanEapAuthProfileName,
       "cLRlanEapAuthStatus": cLRlanEapAuthStatus,
       "cLRlanWebAuthParameter": cLRlanWebAuthParameter,
       "cLRlanClientLimit": cLRlanClientLimit,
       "cLRlanStatus": cLRlanStatus,
       "cLRlanWebAuthIpv4Acl": cLRlanWebAuthIpv4Acl,
       "cLRlanWebAuthIpv6Acl": cLRlanWebAuthIpv6Acl,
       "cLRlanSecurity8021XAuthList": cLRlanSecurity8021XAuthList,
       "cLRlanMdnsMode": cLRlanMdnsMode,
       "cLRlanPolicyTable": cLRlanPolicyTable,
       "cLRlanPolicyEntry": cLRlanPolicyEntry,
       "cLRlanPolicyProfileName": cLRlanPolicyProfileName,
       "cLRlanPolicyRowStatus": cLRlanPolicyRowStatus,
       "cLRlanPolicyStatus": cLRlanPolicyStatus,
       "cLRlanPolicyDesc": cLRlanPolicyDesc,
       "cLRlanPolicyIpv4Acl": cLRlanPolicyIpv4Acl,
       "cLRlanPolicyIpv6Acl": cLRlanPolicyIpv6Acl,
       "cLRlanAAAOverride": cLRlanAAAOverride,
       "cLRlanCentralSwitching": cLRlanCentralSwitching,
       "cLRlanInterface": cLRlanInterface,
       "cLRlanPoeEnabled": cLRlanPoeEnabled,
       "cLRlanHostMode": cLRlanHostMode,
       "cLRlanViolationMode": cLRlanViolationMode,
       "cLRlanVoiceVlanId": cLRlanVoiceVlanId,
       "cLRlanDataVlanId": cLRlanDataVlanId,
       "cLRlanBlacklistEnabled": cLRlanBlacklistEnabled,
       "cLRlanBlacklistTimeout": cLRlanBlacklistTimeout,
       "cLRlanAAAPolicyName": cLRlanAAAPolicyName,
       "cLRlanSessionTimeout": cLRlanSessionTimeout,
       "cLRlanPreAuthEnabled": cLRlanPreAuthEnabled,
       "cLRlanDhcpServerType": cLRlanDhcpServerType,
       "cLRlanDhcpServer": cLRlanDhcpServer,
       "cLRlanRadiusHttpProfiling": cLRlanRadiusHttpProfiling,
       "cLRlanRadiusDhcpProfiling": cLRlanRadiusDhcpProfiling,
       "cLRlanLocalHttpProfiling": cLRlanLocalHttpProfiling,
       "cLRlanLocalDhcpProfiling": cLRlanLocalDhcpProfiling,
       "cLRlanIpv6IngressStatus": cLRlanIpv6IngressStatus,
       "cLRlanIpv6EgressStatus": cLRlanIpv6EgressStatus,
       "cLRlanIpv4IngressStatus": cLRlanIpv4IngressStatus,
       "cLRlanIpv4EgressStatus": cLRlanIpv4EgressStatus,
       "cLRlanIpv6IngressName": cLRlanIpv6IngressName,
       "cLRlanIpv6EgressName": cLRlanIpv6EgressName,
       "cLRlanIpv4IngressName": cLRlanIpv4IngressName,
       "cLRlanIpv4EgressName": cLRlanIpv4EgressName,
       "cLRlanSplitTunnelGatewayType": cLRlanSplitTunnelGatewayType,
       "cLRlanSplitTunnelGateway": cLRlanSplitTunnelGateway,
       "cLRlanSplitTunnelNetmaskType": cLRlanSplitTunnelNetmaskType,
       "cLRlanSplitTunnelNetmask": cLRlanSplitTunnelNetmask,
       "cLRlanSplitTunnel": cLRlanSplitTunnel,
       "cLRlanAclName": cLRlanAclName,
       "cLRlanSplitTunnelOverride": cLRlanSplitTunnelOverride,
       "cLRlanAccountingList": cLRlanAccountingList,
       "cLRlanDhcpEnabled": cLRlanDhcpEnabled,
       "cLRlanCentralDhcp": cLRlanCentralDhcp,
       "cLRlanMdnsPolicy": cLRlanMdnsPolicy,
       "cLRlanPowerLevelId": cLRlanPowerLevelId,
       "ciscoLwappRlanConform": ciscoLwappRlanConform,
       "ciscoLwappRlanCompliances": ciscoLwappRlanCompliances,
       "ciscoLwappRlanCompliance": ciscoLwappRlanCompliance,
       "ciscoLwappRlanComplianceRev1": ciscoLwappRlanComplianceRev1,
       "ciscoLwappRlanComplianceRev2": ciscoLwappRlanComplianceRev2,
       "ciscoLwappRlanComplianceRev3": ciscoLwappRlanComplianceRev3,
       "ciscoLwappRlanGroups": ciscoLwappRlanGroups,
       "ciscoLwappRlanConfigGroup1": ciscoLwappRlanConfigGroup1,
       "ciscoLwappRlanConfigGroup2": ciscoLwappRlanConfigGroup2,
       "ciscoLwappRlanConfigGroup2Sup1": ciscoLwappRlanConfigGroup2Sup1,
       "ciscoLwappRlanConfigGroup2Sup2": ciscoLwappRlanConfigGroup2Sup2,
       "ciscoLwappRlanConfigGroup1Sup1": ciscoLwappRlanConfigGroup1Sup1,
       "ciscoLwappRlanConfigGroup2Sup3": ciscoLwappRlanConfigGroup2Sup3}
)
