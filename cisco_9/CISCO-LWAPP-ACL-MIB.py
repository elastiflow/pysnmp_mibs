# SNMP MIB module (CISCO-LWAPP-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-LWAPP-ACL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:47:34 2025
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

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

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

ciscoLwappAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577)
)
if mibBuilder.loadTexts:
    ciscoLwappAclMIB.setRevisions(
        ("2017-04-24 00:00",
         "2010-03-04 00:00",
         "2006-08-29 00:00",
         "2006-07-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappAclMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappAclMIBNotifs = _CiscoLwappAclMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 0)
)
_CiscoLwappAclMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappAclMIBObjects = _CiscoLwappAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1)
)
_CiscoLwappCpuAcl_ObjectIdentity = ObjectIdentity
ciscoLwappCpuAcl = _CiscoLwappCpuAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1)
)
_ClaCpuAclTable_Object = MibTable
claCpuAclTable = _ClaCpuAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1, 1)
)
if mibBuilder.loadTexts:
    claCpuAclTable.setStatus("current")
_ClaCpuAclEntry_Object = MibTableRow
claCpuAclEntry = _ClaCpuAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1, 1, 1)
)
claCpuAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-ACL-MIB", "claCpuAclIndex"),
)
if mibBuilder.loadTexts:
    claCpuAclEntry.setStatus("current")
_ClaCpuAclIndex_Type = Unsigned32
_ClaCpuAclIndex_Object = MibTableColumn
claCpuAclIndex = _ClaCpuAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1, 1, 1, 1),
    _ClaCpuAclIndex_Type()
)
claCpuAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claCpuAclIndex.setStatus("current")


class _ClaCpuAclName_Type(SnmpAdminString):
    """Custom type claCpuAclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ClaCpuAclName_Type.__name__ = "SnmpAdminString"
_ClaCpuAclName_Object = MibTableColumn
claCpuAclName = _ClaCpuAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1, 1, 1, 2),
    _ClaCpuAclName_Type()
)
claCpuAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claCpuAclName.setStatus("current")


class _ClaCpuAclPacketApplicability_Type(Integer32):
    """Custom type claCpuAclPacketApplicability based on Integer32"""
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
        *(("none", 1),
          ("wired", 2),
          ("wireless", 3),
          ("both", 4))
    )


_ClaCpuAclPacketApplicability_Type.__name__ = "Integer32"
_ClaCpuAclPacketApplicability_Object = MibTableColumn
claCpuAclPacketApplicability = _ClaCpuAclPacketApplicability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 1, 1, 1, 3),
    _ClaCpuAclPacketApplicability_Type()
)
claCpuAclPacketApplicability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claCpuAclPacketApplicability.setStatus("current")
_CiscoLwappControllerAcl_ObjectIdentity = ObjectIdentity
ciscoLwappControllerAcl = _CiscoLwappControllerAcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2)
)
_ClaAclTable_Object = MibTable
claAclTable = _ClaAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 1)
)
if mibBuilder.loadTexts:
    claAclTable.setStatus("current")
_ClaAclEntry_Object = MibTableRow
claAclEntry = _ClaAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 1, 1)
)
claAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-ACL-MIB", "claAclName"),
)
if mibBuilder.loadTexts:
    claAclEntry.setStatus("current")


class _ClaAclName_Type(OctetString):
    """Custom type claAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClaAclName_Type.__name__ = "OctetString"
_ClaAclName_Object = MibTableColumn
claAclName = _ClaAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 1, 1, 1),
    _ClaAclName_Type()
)
claAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claAclName.setStatus("current")


class _ClaAclCounterClear_Type(TruthValue):
    """Custom type claAclCounterClear based on TruthValue"""
    defaultValue = 2


_ClaAclCounterClear_Type.__name__ = "TruthValue"
_ClaAclCounterClear_Object = MibTableColumn
claAclCounterClear = _ClaAclCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 1, 1, 2),
    _ClaAclCounterClear_Type()
)
claAclCounterClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claAclCounterClear.setStatus("current")
_ClaAclRuleTable_Object = MibTable
claAclRuleTable = _ClaAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 2)
)
if mibBuilder.loadTexts:
    claAclRuleTable.setStatus("current")
_ClaAclRuleEntry_Object = MibTableRow
claAclRuleEntry = _ClaAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 2, 1)
)
claAclRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-ACL-MIB", "claAclName"),
    (0, "CISCO-LWAPP-ACL-MIB", "claAclRuleIndex"),
)
if mibBuilder.loadTexts:
    claAclRuleEntry.setStatus("current")


class _ClaAclRuleIndex_Type(Unsigned32):
    """Custom type claAclRuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ClaAclRuleIndex_Type.__name__ = "Unsigned32"
_ClaAclRuleIndex_Object = MibTableColumn
claAclRuleIndex = _ClaAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 2, 1, 2),
    _ClaAclRuleIndex_Type()
)
claAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claAclRuleIndex.setStatus("current")
_ClaAclRuleHits_Type = Counter32
_ClaAclRuleHits_Object = MibTableColumn
claAclRuleHits = _ClaAclRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 2, 1, 3),
    _ClaAclRuleHits_Type()
)
claAclRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claAclRuleHits.setStatus("current")
_ClaAclUrlTable_Object = MibTable
claAclUrlTable = _ClaAclUrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 3)
)
if mibBuilder.loadTexts:
    claAclUrlTable.setStatus("current")
_ClaAclUrlEntry_Object = MibTableRow
claAclUrlEntry = _ClaAclUrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 3, 1)
)
claAclUrlEntry.setIndexNames(
    (0, "CISCO-LWAPP-ACL-MIB", "claAclName"),
    (0, "CISCO-LWAPP-ACL-MIB", "claAclUrlIndex"),
)
if mibBuilder.loadTexts:
    claAclUrlEntry.setStatus("current")


class _ClaAclUrlIndex_Type(Unsigned32):
    """Custom type claAclUrlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ClaAclUrlIndex_Type.__name__ = "Unsigned32"
_ClaAclUrlIndex_Object = MibTableColumn
claAclUrlIndex = _ClaAclUrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 3, 1, 1),
    _ClaAclUrlIndex_Type()
)
claAclUrlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claAclUrlIndex.setStatus("current")
_ClaAclUrlName_Type = CiscoURLString
_ClaAclUrlName_Object = MibTableColumn
claAclUrlName = _ClaAclUrlName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 3, 1, 2),
    _ClaAclUrlName_Type()
)
claAclUrlName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claAclUrlName.setStatus("current")
_ClaAclUrlRowStatus_Type = RowStatus
_ClaAclUrlRowStatus_Object = MibTableColumn
claAclUrlRowStatus = _ClaAclUrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 3, 1, 3),
    _ClaAclUrlRowStatus_Type()
)
claAclUrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claAclUrlRowStatus.setStatus("current")
_ClaUrlAclTable_Object = MibTable
claUrlAclTable = _ClaUrlAclTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 4)
)
if mibBuilder.loadTexts:
    claUrlAclTable.setStatus("current")
_ClaUrlAclEntry_Object = MibTableRow
claUrlAclEntry = _ClaUrlAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 4, 1)
)
claUrlAclEntry.setIndexNames(
    (0, "CISCO-LWAPP-ACL-MIB", "claUrlAclName"),
)
if mibBuilder.loadTexts:
    claUrlAclEntry.setStatus("current")


class _ClaUrlAclName_Type(OctetString):
    """Custom type claUrlAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ClaUrlAclName_Type.__name__ = "OctetString"
_ClaUrlAclName_Object = MibTableColumn
claUrlAclName = _ClaUrlAclName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 4, 1, 1),
    _ClaUrlAclName_Type()
)
claUrlAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claUrlAclName.setStatus("current")


class _ClaUrlAclApplyMode_Type(Integer32):
    """Custom type claUrlAclApplyMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notapplied", 1),
          ("applied", 2))
    )


_ClaUrlAclApplyMode_Type.__name__ = "Integer32"
_ClaUrlAclApplyMode_Object = MibTableColumn
claUrlAclApplyMode = _ClaUrlAclApplyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 4, 1, 2),
    _ClaUrlAclApplyMode_Type()
)
claUrlAclApplyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claUrlAclApplyMode.setStatus("current")


class _ClaUrlAclCounterClear_Type(TruthValue):
    """Custom type claUrlAclCounterClear based on TruthValue"""
    defaultValue = 2


_ClaUrlAclCounterClear_Type.__name__ = "TruthValue"
_ClaUrlAclCounterClear_Object = MibTableColumn
claUrlAclCounterClear = _ClaUrlAclCounterClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 4, 1, 3),
    _ClaUrlAclCounterClear_Type()
)
claUrlAclCounterClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claUrlAclCounterClear.setStatus("current")
_ClaUrlAclRowStatus_Type = RowStatus
_ClaUrlAclRowStatus_Object = MibTableColumn
claUrlAclRowStatus = _ClaUrlAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 4, 1, 4),
    _ClaUrlAclRowStatus_Type()
)
claUrlAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claUrlAclRowStatus.setStatus("current")


class _ClaUrlAclListType_Type(Integer32):
    """Custom type claUrlAclListType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("whitelist", 1),
          ("blacklist", 2))
    )


_ClaUrlAclListType_Type.__name__ = "Integer32"
_ClaUrlAclListType_Object = MibTableColumn
claUrlAclListType = _ClaUrlAclListType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 4, 1, 5),
    _ClaUrlAclListType_Type()
)
claUrlAclListType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claUrlAclListType.setStatus("current")
_ClaUrlAclRuleTable_Object = MibTable
claUrlAclRuleTable = _ClaUrlAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 5)
)
if mibBuilder.loadTexts:
    claUrlAclRuleTable.setStatus("current")
_ClaUrlAclRuleEntry_Object = MibTableRow
claUrlAclRuleEntry = _ClaUrlAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 5, 1)
)
claUrlAclRuleEntry.setIndexNames(
    (0, "CISCO-LWAPP-ACL-MIB", "claUrlAclName"),
    (0, "CISCO-LWAPP-ACL-MIB", "claUrlAclRuleIndex"),
)
if mibBuilder.loadTexts:
    claUrlAclRuleEntry.setStatus("current")
_ClaUrlAclRuleIndex_Type = Unsigned32
_ClaUrlAclRuleIndex_Object = MibTableColumn
claUrlAclRuleIndex = _ClaUrlAclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 5, 1, 1),
    _ClaUrlAclRuleIndex_Type()
)
claUrlAclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    claUrlAclRuleIndex.setStatus("current")


class _ClaUrlAclRuleUrl_Type(OctetString):
    """Custom type claUrlAclRuleUrl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ClaUrlAclRuleUrl_Type.__name__ = "OctetString"
_ClaUrlAclRuleUrl_Object = MibTableColumn
claUrlAclRuleUrl = _ClaUrlAclRuleUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 5, 1, 2),
    _ClaUrlAclRuleUrl_Type()
)
claUrlAclRuleUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claUrlAclRuleUrl.setStatus("current")


class _ClaUrlAclRuleAction_Type(Integer32):
    """Custom type claUrlAclRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_ClaUrlAclRuleAction_Type.__name__ = "Integer32"
_ClaUrlAclRuleAction_Object = MibTableColumn
claUrlAclRuleAction = _ClaUrlAclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 5, 1, 3),
    _ClaUrlAclRuleAction_Type()
)
claUrlAclRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claUrlAclRuleAction.setStatus("current")
_ClaUrlAclRuleHits_Type = Counter32
_ClaUrlAclRuleHits_Object = MibTableColumn
claUrlAclRuleHits = _ClaUrlAclRuleHits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 5, 1, 4),
    _ClaUrlAclRuleHits_Type()
)
claUrlAclRuleHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    claUrlAclRuleHits.setStatus("current")
_ClaUrlAclRuleRowStatus_Type = RowStatus
_ClaUrlAclRuleRowStatus_Object = MibTableColumn
claUrlAclRuleRowStatus = _ClaUrlAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 2, 5, 1, 5),
    _ClaUrlAclRuleRowStatus_Type()
)
claUrlAclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    claUrlAclRuleRowStatus.setStatus("current")
_CiscoLwappControllerAclGeneral_ObjectIdentity = ObjectIdentity
ciscoLwappControllerAclGeneral = _CiscoLwappControllerAclGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 3)
)


class _ClaAclCounterEnable_Type(TruthValue):
    """Custom type claAclCounterEnable based on TruthValue"""
    defaultValue = 2


_ClaAclCounterEnable_Type.__name__ = "TruthValue"
_ClaAclCounterEnable_Object = MibScalar
claAclCounterEnable = _ClaAclCounterEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 3, 1),
    _ClaAclCounterEnable_Type()
)
claAclCounterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claAclCounterEnable.setStatus("current")
_ClaUrlAclExternalServerIpType_Type = InetAddressType
_ClaUrlAclExternalServerIpType_Object = MibScalar
claUrlAclExternalServerIpType = _ClaUrlAclExternalServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 3, 2),
    _ClaUrlAclExternalServerIpType_Type()
)
claUrlAclExternalServerIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claUrlAclExternalServerIpType.setStatus("current")
_ClaUrlAclExternalServerIp_Type = InetAddress
_ClaUrlAclExternalServerIp_Object = MibScalar
claUrlAclExternalServerIp = _ClaUrlAclExternalServerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 1, 3, 3),
    _ClaUrlAclExternalServerIp_Type()
)
claUrlAclExternalServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    claUrlAclExternalServerIp.setStatus("current")
_CiscoLwappAclMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappAclMIBConform = _CiscoLwappAclMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2)
)
_CiscoLwappAclMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappAclMIBCompliances = _CiscoLwappAclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 1)
)
_CiscoLwappAclMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappAclMIBGroups = _CiscoLwappAclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 2)
)

# Managed Objects groups

ciscoLwappCpuAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 2, 1)
)
ciscoLwappCpuAclGroup.setObjects(
      *(("CISCO-LWAPP-ACL-MIB", "claCpuAclName"),
        ("CISCO-LWAPP-ACL-MIB", "claCpuAclPacketApplicability"))
)
if mibBuilder.loadTexts:
    ciscoLwappCpuAclGroup.setStatus("current")

ciscoLwappAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 2, 2)
)
ciscoLwappAclGroup.setObjects(
      *(("CISCO-LWAPP-ACL-MIB", "claAclCounterEnable"),
        ("CISCO-LWAPP-ACL-MIB", "claAclCounterClear"),
        ("CISCO-LWAPP-ACL-MIB", "claAclRuleHits"),
        ("CISCO-LWAPP-ACL-MIB", "claAclCounterEnable"),
        ("CISCO-LWAPP-ACL-MIB", "claAclCounterClear"),
        ("CISCO-LWAPP-ACL-MIB", "claAclRuleHits"),
        ("CISCO-LWAPP-ACL-MIB", "claUrlAclExternalServerIpType"),
        ("CISCO-LWAPP-ACL-MIB", "claUrlAclExternalServerIp"),
        ("CISCO-LWAPP-ACL-MIB", "claAclUrlName"),
        ("CISCO-LWAPP-ACL-MIB", "claAclUrlRowStatus"),
        ("CISCO-LWAPP-ACL-MIB", "claUrlAclApplyMode"),
        ("CISCO-LWAPP-ACL-MIB", "claUrlAclCounterClear"),
        ("CISCO-LWAPP-ACL-MIB", "claUrlAclRowStatus"),
        ("CISCO-LWAPP-ACL-MIB", "claUrlAclListType"),
        ("CISCO-LWAPP-ACL-MIB", "claUrlAclRuleUrl"),
        ("CISCO-LWAPP-ACL-MIB", "claUrlAclRuleAction"),
        ("CISCO-LWAPP-ACL-MIB", "claUrlAclRuleHits"),
        ("CISCO-LWAPP-ACL-MIB", "claUrlAclRuleRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappAclGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoLwappAclMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 1, 1)
)
ciscoLwappAclMIBCompliance.setObjects(
    ("CISCO-LWAPP-ACL-MIB", "ciscoLwappCpuAclGroup")
)
if mibBuilder.loadTexts:
    ciscoLwappAclMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappAclMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 577, 2, 1, 2)
)
ciscoLwappAclMIBComplianceRev1.setObjects(
      *(("CISCO-LWAPP-ACL-MIB", "ciscoLwappCpuAclGroup"),
        ("CISCO-LWAPP-ACL-MIB", "ciscoLwappAclGroup"))
)
if mibBuilder.loadTexts:
    ciscoLwappAclMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-ACL-MIB",
    **{"ciscoLwappAclMIB": ciscoLwappAclMIB,
       "ciscoLwappAclMIBNotifs": ciscoLwappAclMIBNotifs,
       "ciscoLwappAclMIBObjects": ciscoLwappAclMIBObjects,
       "ciscoLwappCpuAcl": ciscoLwappCpuAcl,
       "claCpuAclTable": claCpuAclTable,
       "claCpuAclEntry": claCpuAclEntry,
       "claCpuAclIndex": claCpuAclIndex,
       "claCpuAclName": claCpuAclName,
       "claCpuAclPacketApplicability": claCpuAclPacketApplicability,
       "ciscoLwappControllerAcl": ciscoLwappControllerAcl,
       "claAclTable": claAclTable,
       "claAclEntry": claAclEntry,
       "claAclName": claAclName,
       "claAclCounterClear": claAclCounterClear,
       "claAclRuleTable": claAclRuleTable,
       "claAclRuleEntry": claAclRuleEntry,
       "claAclRuleIndex": claAclRuleIndex,
       "claAclRuleHits": claAclRuleHits,
       "claAclUrlTable": claAclUrlTable,
       "claAclUrlEntry": claAclUrlEntry,
       "claAclUrlIndex": claAclUrlIndex,
       "claAclUrlName": claAclUrlName,
       "claAclUrlRowStatus": claAclUrlRowStatus,
       "claUrlAclTable": claUrlAclTable,
       "claUrlAclEntry": claUrlAclEntry,
       "claUrlAclName": claUrlAclName,
       "claUrlAclApplyMode": claUrlAclApplyMode,
       "claUrlAclCounterClear": claUrlAclCounterClear,
       "claUrlAclRowStatus": claUrlAclRowStatus,
       "claUrlAclListType": claUrlAclListType,
       "claUrlAclRuleTable": claUrlAclRuleTable,
       "claUrlAclRuleEntry": claUrlAclRuleEntry,
       "claUrlAclRuleIndex": claUrlAclRuleIndex,
       "claUrlAclRuleUrl": claUrlAclRuleUrl,
       "claUrlAclRuleAction": claUrlAclRuleAction,
       "claUrlAclRuleHits": claUrlAclRuleHits,
       "claUrlAclRuleRowStatus": claUrlAclRuleRowStatus,
       "ciscoLwappControllerAclGeneral": ciscoLwappControllerAclGeneral,
       "claAclCounterEnable": claAclCounterEnable,
       "claUrlAclExternalServerIpType": claUrlAclExternalServerIpType,
       "claUrlAclExternalServerIp": claUrlAclExternalServerIp,
       "ciscoLwappAclMIBConform": ciscoLwappAclMIBConform,
       "ciscoLwappAclMIBCompliances": ciscoLwappAclMIBCompliances,
       "ciscoLwappAclMIBCompliance": ciscoLwappAclMIBCompliance,
       "ciscoLwappAclMIBComplianceRev1": ciscoLwappAclMIBComplianceRev1,
       "ciscoLwappAclMIBGroups": ciscoLwappAclMIBGroups,
       "ciscoLwappCpuAclGroup": ciscoLwappCpuAclGroup,
       "ciscoLwappAclGroup": ciscoLwappAclGroup}
)
