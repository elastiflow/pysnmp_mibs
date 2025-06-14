# SNMP MIB module (DNOS-QOS-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DNOS-QOS-ACL-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:25:39 2025
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

(fastPathQOS,) = mibBuilder.importSymbols(
    "DNOS-QOS-MIB",
    "fastPathQOS")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

fastPathQOSACL = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fastPathQOSACL.setRevisions(
        ("2005-07-08 00:00",
         "2004-09-20 00:00",
         "2003-11-21 00:00",
         "2003-02-06 23:34")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EtypeValue(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )



class Ipv6AddressPrefix(TextualConvention, OctetString):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class AclBurstSize(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )



# MIB Managed Objects in the order of their OIDs

_AclNotifications_ObjectIdentity = ObjectIdentity
aclNotifications = _AclNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 0)
)
_AclTable_Object = MibTable
aclTable = _AclTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    aclTable.setStatus("current")
_AclEntry_Object = MibTableRow
aclEntry = _AclEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 1, 1)
)
aclEntry.setIndexNames(
    (0, "DNOS-QOS-ACL-MIB", "aclIndex"),
)
if mibBuilder.loadTexts:
    aclEntry.setStatus("current")


class _AclIndex_Type(Integer32):
    """Custom type aclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclIndex_Type.__name__ = "Integer32"
_AclIndex_Object = MibTableColumn
aclIndex = _AclIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 1, 1, 1),
    _AclIndex_Type()
)
aclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIndex.setStatus("current")


class _AclName_Type(DisplayString):
    """Custom type aclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclName_Type.__name__ = "DisplayString"
_AclName_Object = MibTableColumn
aclName = _AclName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 1, 1, 2),
    _AclName_Type()
)
aclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclName.setStatus("current")
_AclStatus_Type = RowStatus
_AclStatus_Object = MibTableColumn
aclStatus = _AclStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 1, 1, 3),
    _AclStatus_Type()
)
aclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclStatus.setStatus("current")
_AclRuleTable_Object = MibTable
aclRuleTable = _AclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    aclRuleTable.setStatus("current")
_AclRuleEntry_Object = MibTableRow
aclRuleEntry = _AclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1)
)
aclRuleEntry.setIndexNames(
    (0, "DNOS-QOS-ACL-MIB", "aclIndex"),
    (0, "DNOS-QOS-ACL-MIB", "aclRuleIndex"),
)
if mibBuilder.loadTexts:
    aclRuleEntry.setStatus("current")


class _AclRuleIndex_Type(Integer32):
    """Custom type aclRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclRuleIndex_Type.__name__ = "Integer32"
_AclRuleIndex_Object = MibTableColumn
aclRuleIndex = _AclRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 1),
    _AclRuleIndex_Type()
)
aclRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclRuleIndex.setStatus("current")


class _AclRuleAction_Type(Integer32):
    """Custom type aclRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_AclRuleAction_Type.__name__ = "Integer32"
_AclRuleAction_Object = MibTableColumn
aclRuleAction = _AclRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 2),
    _AclRuleAction_Type()
)
aclRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleAction.setStatus("current")


class _AclRuleProtocol_Type(Integer32):
    """Custom type aclRuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AclRuleProtocol_Type.__name__ = "Integer32"
_AclRuleProtocol_Object = MibTableColumn
aclRuleProtocol = _AclRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 3),
    _AclRuleProtocol_Type()
)
aclRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleProtocol.setStatus("current")
_AclRuleSrcIpAddress_Type = IpAddress
_AclRuleSrcIpAddress_Object = MibTableColumn
aclRuleSrcIpAddress = _AclRuleSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 4),
    _AclRuleSrcIpAddress_Type()
)
aclRuleSrcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcIpAddress.setStatus("current")
_AclRuleSrcIpMask_Type = IpAddress
_AclRuleSrcIpMask_Object = MibTableColumn
aclRuleSrcIpMask = _AclRuleSrcIpMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 5),
    _AclRuleSrcIpMask_Type()
)
aclRuleSrcIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcIpMask.setStatus("current")
_AclRuleSrcL4Port_Type = Integer32
_AclRuleSrcL4Port_Object = MibTableColumn
aclRuleSrcL4Port = _AclRuleSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 6),
    _AclRuleSrcL4Port_Type()
)
aclRuleSrcL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcL4Port.setStatus("current")
_AclRuleSrcL4PortRangeStart_Type = Integer32
_AclRuleSrcL4PortRangeStart_Object = MibTableColumn
aclRuleSrcL4PortRangeStart = _AclRuleSrcL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 7),
    _AclRuleSrcL4PortRangeStart_Type()
)
aclRuleSrcL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcL4PortRangeStart.setStatus("current")
_AclRuleSrcL4PortRangeEnd_Type = Integer32
_AclRuleSrcL4PortRangeEnd_Object = MibTableColumn
aclRuleSrcL4PortRangeEnd = _AclRuleSrcL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 8),
    _AclRuleSrcL4PortRangeEnd_Type()
)
aclRuleSrcL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcL4PortRangeEnd.setStatus("current")
_AclRuleDestIpAddress_Type = IpAddress
_AclRuleDestIpAddress_Object = MibTableColumn
aclRuleDestIpAddress = _AclRuleDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 9),
    _AclRuleDestIpAddress_Type()
)
aclRuleDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestIpAddress.setStatus("current")
_AclRuleDestIpMask_Type = IpAddress
_AclRuleDestIpMask_Object = MibTableColumn
aclRuleDestIpMask = _AclRuleDestIpMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 10),
    _AclRuleDestIpMask_Type()
)
aclRuleDestIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestIpMask.setStatus("current")
_AclRuleDestL4Port_Type = Integer32
_AclRuleDestL4Port_Object = MibTableColumn
aclRuleDestL4Port = _AclRuleDestL4Port_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 11),
    _AclRuleDestL4Port_Type()
)
aclRuleDestL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestL4Port.setStatus("current")
_AclRuleDestL4PortRangeStart_Type = Integer32
_AclRuleDestL4PortRangeStart_Object = MibTableColumn
aclRuleDestL4PortRangeStart = _AclRuleDestL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 12),
    _AclRuleDestL4PortRangeStart_Type()
)
aclRuleDestL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestL4PortRangeStart.setStatus("current")
_AclRuleDestL4PortRangeEnd_Type = Integer32
_AclRuleDestL4PortRangeEnd_Object = MibTableColumn
aclRuleDestL4PortRangeEnd = _AclRuleDestL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 13),
    _AclRuleDestL4PortRangeEnd_Type()
)
aclRuleDestL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDestL4PortRangeEnd.setStatus("current")
_AclRuleIPDSCP_Type = Integer32
_AclRuleIPDSCP_Object = MibTableColumn
aclRuleIPDSCP = _AclRuleIPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 14),
    _AclRuleIPDSCP_Type()
)
aclRuleIPDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIPDSCP.setStatus("current")
_AclRuleIpPrecedence_Type = Integer32
_AclRuleIpPrecedence_Object = MibTableColumn
aclRuleIpPrecedence = _AclRuleIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 15),
    _AclRuleIpPrecedence_Type()
)
aclRuleIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIpPrecedence.setStatus("current")
_AclRuleIpTosBits_Type = Integer32
_AclRuleIpTosBits_Object = MibTableColumn
aclRuleIpTosBits = _AclRuleIpTosBits_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 16),
    _AclRuleIpTosBits_Type()
)
aclRuleIpTosBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIpTosBits.setStatus("current")
_AclRuleIpTosMask_Type = Integer32
_AclRuleIpTosMask_Object = MibTableColumn
aclRuleIpTosMask = _AclRuleIpTosMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 17),
    _AclRuleIpTosMask_Type()
)
aclRuleIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIpTosMask.setStatus("current")
_AclRuleStatus_Type = RowStatus
_AclRuleStatus_Object = MibTableColumn
aclRuleStatus = _AclRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 18),
    _AclRuleStatus_Type()
)
aclRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleStatus.setStatus("current")
_AclRuleAssignQueueId_Type = Unsigned32
_AclRuleAssignQueueId_Object = MibTableColumn
aclRuleAssignQueueId = _AclRuleAssignQueueId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 19),
    _AclRuleAssignQueueId_Type()
)
aclRuleAssignQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleAssignQueueId.setStatus("current")


class _AclRuleRedirectIntf_Type(InterfaceIndexOrZero):
    """Custom type aclRuleRedirectIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_AclRuleRedirectIntf_Type.__name__ = "InterfaceIndexOrZero"
_AclRuleRedirectIntf_Object = MibTableColumn
aclRuleRedirectIntf = _AclRuleRedirectIntf_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 20),
    _AclRuleRedirectIntf_Type()
)
aclRuleRedirectIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleRedirectIntf.setStatus("current")
_AclRuleMatchEvery_Type = TruthValue
_AclRuleMatchEvery_Object = MibTableColumn
aclRuleMatchEvery = _AclRuleMatchEvery_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 21),
    _AclRuleMatchEvery_Type()
)
aclRuleMatchEvery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleMatchEvery.setStatus("current")


class _AclRuleMirrorIntf_Type(InterfaceIndexOrZero):
    """Custom type aclRuleMirrorIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_AclRuleMirrorIntf_Type.__name__ = "InterfaceIndexOrZero"
_AclRuleMirrorIntf_Object = MibTableColumn
aclRuleMirrorIntf = _AclRuleMirrorIntf_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 22),
    _AclRuleMirrorIntf_Type()
)
aclRuleMirrorIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleMirrorIntf.setStatus("current")
_AclRuleLogging_Type = TruthValue
_AclRuleLogging_Object = MibTableColumn
aclRuleLogging = _AclRuleLogging_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 23),
    _AclRuleLogging_Type()
)
aclRuleLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleLogging.setStatus("current")


class _AclRuleTimeRangeName_Type(DisplayString):
    """Custom type aclRuleTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclRuleTimeRangeName_Type.__name__ = "DisplayString"
_AclRuleTimeRangeName_Object = MibTableColumn
aclRuleTimeRangeName = _AclRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 24),
    _AclRuleTimeRangeName_Type()
)
aclRuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleTimeRangeName.setStatus("current")


class _AclRuleTimeRangeStatus_Type(Integer32):
    """Custom type aclRuleTimeRangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AclRuleTimeRangeStatus_Type.__name__ = "Integer32"
_AclRuleTimeRangeStatus_Object = MibTableColumn
aclRuleTimeRangeStatus = _AclRuleTimeRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 25),
    _AclRuleTimeRangeStatus_Type()
)
aclRuleTimeRangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclRuleTimeRangeStatus.setStatus("current")
_AclRuleRateLimitCrate_Type = Unsigned32
_AclRuleRateLimitCrate_Object = MibTableColumn
aclRuleRateLimitCrate = _AclRuleRateLimitCrate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 26),
    _AclRuleRateLimitCrate_Type()
)
aclRuleRateLimitCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleRateLimitCrate.setStatus("current")
_AclRuleRateLimitCburst_Type = AclBurstSize
_AclRuleRateLimitCburst_Object = MibTableColumn
aclRuleRateLimitCburst = _AclRuleRateLimitCburst_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 27),
    _AclRuleRateLimitCburst_Type()
)
aclRuleRateLimitCburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleRateLimitCburst.setStatus("current")


class _AclRuleIcmpType_Type(Integer32):
    """Custom type aclRuleIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclRuleIcmpType_Type.__name__ = "Integer32"
_AclRuleIcmpType_Object = MibTableColumn
aclRuleIcmpType = _AclRuleIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 29),
    _AclRuleIcmpType_Type()
)
aclRuleIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIcmpType.setStatus("current")


class _AclRuleIcmpCode_Type(Integer32):
    """Custom type aclRuleIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclRuleIcmpCode_Type.__name__ = "Integer32"
_AclRuleIcmpCode_Object = MibTableColumn
aclRuleIcmpCode = _AclRuleIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 30),
    _AclRuleIcmpCode_Type()
)
aclRuleIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIcmpCode.setStatus("current")


class _AclRuleIgmpType_Type(Integer32):
    """Custom type aclRuleIgmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclRuleIgmpType_Type.__name__ = "Integer32"
_AclRuleIgmpType_Object = MibTableColumn
aclRuleIgmpType = _AclRuleIgmpType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 31),
    _AclRuleIgmpType_Type()
)
aclRuleIgmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleIgmpType.setStatus("current")
_AclRuleEstablished_Type = TruthValue
_AclRuleEstablished_Object = MibTableColumn
aclRuleEstablished = _AclRuleEstablished_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 32),
    _AclRuleEstablished_Type()
)
aclRuleEstablished.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleEstablished.setStatus("current")
_AclRuleFragments_Type = TruthValue
_AclRuleFragments_Object = MibTableColumn
aclRuleFragments = _AclRuleFragments_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 4, 1, 33),
    _AclRuleFragments_Type()
)
aclRuleFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleFragments.setStatus("current")
_AclMacIndexNextFree_Type = Integer32
_AclMacIndexNextFree_Object = MibScalar
aclMacIndexNextFree = _AclMacIndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 5),
    _AclMacIndexNextFree_Type()
)
aclMacIndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMacIndexNextFree.setStatus("current")
_AclMacTable_Object = MibTable
aclMacTable = _AclMacTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 6)
)
if mibBuilder.loadTexts:
    aclMacTable.setStatus("current")
_AclMacEntry_Object = MibTableRow
aclMacEntry = _AclMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 6, 1)
)
aclMacEntry.setIndexNames(
    (0, "DNOS-QOS-ACL-MIB", "aclMacIndex"),
)
if mibBuilder.loadTexts:
    aclMacEntry.setStatus("current")


class _AclMacIndex_Type(Integer32):
    """Custom type aclMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclMacIndex_Type.__name__ = "Integer32"
_AclMacIndex_Object = MibTableColumn
aclMacIndex = _AclMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 6, 1, 1),
    _AclMacIndex_Type()
)
aclMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclMacIndex.setStatus("current")


class _AclMacName_Type(DisplayString):
    """Custom type aclMacName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclMacName_Type.__name__ = "DisplayString"
_AclMacName_Object = MibTableColumn
aclMacName = _AclMacName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 6, 1, 2),
    _AclMacName_Type()
)
aclMacName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacName.setStatus("current")
_AclMacStatus_Type = RowStatus
_AclMacStatus_Object = MibTableColumn
aclMacStatus = _AclMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 6, 1, 3),
    _AclMacStatus_Type()
)
aclMacStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacStatus.setStatus("current")
_AclMacRuleTable_Object = MibTable
aclMacRuleTable = _AclMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7)
)
if mibBuilder.loadTexts:
    aclMacRuleTable.setStatus("current")
_AclMacRuleEntry_Object = MibTableRow
aclMacRuleEntry = _AclMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1)
)
aclMacRuleEntry.setIndexNames(
    (0, "DNOS-QOS-ACL-MIB", "aclMacIndex"),
    (0, "DNOS-QOS-ACL-MIB", "aclMacRuleIndex"),
)
if mibBuilder.loadTexts:
    aclMacRuleEntry.setStatus("current")


class _AclMacRuleIndex_Type(Integer32):
    """Custom type aclMacRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclMacRuleIndex_Type.__name__ = "Integer32"
_AclMacRuleIndex_Object = MibTableColumn
aclMacRuleIndex = _AclMacRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 1),
    _AclMacRuleIndex_Type()
)
aclMacRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclMacRuleIndex.setStatus("current")


class _AclMacRuleAction_Type(Integer32):
    """Custom type aclMacRuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_AclMacRuleAction_Type.__name__ = "Integer32"
_AclMacRuleAction_Object = MibTableColumn
aclMacRuleAction = _AclMacRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 2),
    _AclMacRuleAction_Type()
)
aclMacRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleAction.setStatus("current")


class _AclMacRuleCos_Type(Unsigned32):
    """Custom type aclMacRuleCos based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclMacRuleCos_Type.__name__ = "Unsigned32"
_AclMacRuleCos_Object = MibTableColumn
aclMacRuleCos = _AclMacRuleCos_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 3),
    _AclMacRuleCos_Type()
)
aclMacRuleCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleCos.setStatus("current")


class _AclMacRuleCos2_Type(Unsigned32):
    """Custom type aclMacRuleCos2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclMacRuleCos2_Type.__name__ = "Unsigned32"
_AclMacRuleCos2_Object = MibTableColumn
aclMacRuleCos2 = _AclMacRuleCos2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 4),
    _AclMacRuleCos2_Type()
)
aclMacRuleCos2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleCos2.setStatus("current")
_AclMacRuleDestMacAddr_Type = MacAddress
_AclMacRuleDestMacAddr_Object = MibTableColumn
aclMacRuleDestMacAddr = _AclMacRuleDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 5),
    _AclMacRuleDestMacAddr_Type()
)
aclMacRuleDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleDestMacAddr.setStatus("current")
_AclMacRuleDestMacMask_Type = MacAddress
_AclMacRuleDestMacMask_Object = MibTableColumn
aclMacRuleDestMacMask = _AclMacRuleDestMacMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 6),
    _AclMacRuleDestMacMask_Type()
)
aclMacRuleDestMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleDestMacMask.setStatus("current")


class _AclMacRuleEtypeKey_Type(Integer32):
    """Custom type aclMacRuleEtypeKey based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("custom", 1),
          ("appletalk", 2),
          ("arp", 3),
          ("ibmsna", 4),
          ("ipv4", 5),
          ("ipv6", 6),
          ("ipx", 7),
          ("mplsmcast", 8),
          ("mplsucast", 9),
          ("netbios", 10),
          ("novell", 11),
          ("pppoe", 12),
          ("rarp", 13))
    )


_AclMacRuleEtypeKey_Type.__name__ = "Integer32"
_AclMacRuleEtypeKey_Object = MibTableColumn
aclMacRuleEtypeKey = _AclMacRuleEtypeKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 7),
    _AclMacRuleEtypeKey_Type()
)
aclMacRuleEtypeKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleEtypeKey.setStatus("current")
_AclMacRuleEtypeValue_Type = EtypeValue
_AclMacRuleEtypeValue_Object = MibTableColumn
aclMacRuleEtypeValue = _AclMacRuleEtypeValue_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 8),
    _AclMacRuleEtypeValue_Type()
)
aclMacRuleEtypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleEtypeValue.setStatus("current")
_AclMacRuleSrcMacAddr_Type = MacAddress
_AclMacRuleSrcMacAddr_Object = MibTableColumn
aclMacRuleSrcMacAddr = _AclMacRuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 9),
    _AclMacRuleSrcMacAddr_Type()
)
aclMacRuleSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleSrcMacAddr.setStatus("current")
_AclMacRuleSrcMacMask_Type = MacAddress
_AclMacRuleSrcMacMask_Object = MibTableColumn
aclMacRuleSrcMacMask = _AclMacRuleSrcMacMask_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 10),
    _AclMacRuleSrcMacMask_Type()
)
aclMacRuleSrcMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleSrcMacMask.setStatus("current")


class _AclMacRuleVlanId_Type(Unsigned32):
    """Custom type aclMacRuleVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AclMacRuleVlanId_Type.__name__ = "Unsigned32"
_AclMacRuleVlanId_Object = MibTableColumn
aclMacRuleVlanId = _AclMacRuleVlanId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 11),
    _AclMacRuleVlanId_Type()
)
aclMacRuleVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanId.setStatus("current")


class _AclMacRuleVlanIdRangeStart_Type(Unsigned32):
    """Custom type aclMacRuleVlanIdRangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AclMacRuleVlanIdRangeStart_Type.__name__ = "Unsigned32"
_AclMacRuleVlanIdRangeStart_Object = MibTableColumn
aclMacRuleVlanIdRangeStart = _AclMacRuleVlanIdRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 12),
    _AclMacRuleVlanIdRangeStart_Type()
)
aclMacRuleVlanIdRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanIdRangeStart.setStatus("current")


class _AclMacRuleVlanIdRangeEnd_Type(Unsigned32):
    """Custom type aclMacRuleVlanIdRangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AclMacRuleVlanIdRangeEnd_Type.__name__ = "Unsigned32"
_AclMacRuleVlanIdRangeEnd_Object = MibTableColumn
aclMacRuleVlanIdRangeEnd = _AclMacRuleVlanIdRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 13),
    _AclMacRuleVlanIdRangeEnd_Type()
)
aclMacRuleVlanIdRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanIdRangeEnd.setStatus("current")


class _AclMacRuleVlanId2_Type(Unsigned32):
    """Custom type aclMacRuleVlanId2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AclMacRuleVlanId2_Type.__name__ = "Unsigned32"
_AclMacRuleVlanId2_Object = MibTableColumn
aclMacRuleVlanId2 = _AclMacRuleVlanId2_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 14),
    _AclMacRuleVlanId2_Type()
)
aclMacRuleVlanId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanId2.setStatus("current")


class _AclMacRuleVlanId2RangeStart_Type(Unsigned32):
    """Custom type aclMacRuleVlanId2RangeStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AclMacRuleVlanId2RangeStart_Type.__name__ = "Unsigned32"
_AclMacRuleVlanId2RangeStart_Object = MibTableColumn
aclMacRuleVlanId2RangeStart = _AclMacRuleVlanId2RangeStart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 15),
    _AclMacRuleVlanId2RangeStart_Type()
)
aclMacRuleVlanId2RangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanId2RangeStart.setStatus("current")


class _AclMacRuleVlanId2RangeEnd_Type(Unsigned32):
    """Custom type aclMacRuleVlanId2RangeEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AclMacRuleVlanId2RangeEnd_Type.__name__ = "Unsigned32"
_AclMacRuleVlanId2RangeEnd_Object = MibTableColumn
aclMacRuleVlanId2RangeEnd = _AclMacRuleVlanId2RangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 16),
    _AclMacRuleVlanId2RangeEnd_Type()
)
aclMacRuleVlanId2RangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleVlanId2RangeEnd.setStatus("current")
_AclMacRuleStatus_Type = RowStatus
_AclMacRuleStatus_Object = MibTableColumn
aclMacRuleStatus = _AclMacRuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 17),
    _AclMacRuleStatus_Type()
)
aclMacRuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleStatus.setStatus("current")
_AclMacRuleAssignQueueId_Type = Unsigned32
_AclMacRuleAssignQueueId_Object = MibTableColumn
aclMacRuleAssignQueueId = _AclMacRuleAssignQueueId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 18),
    _AclMacRuleAssignQueueId_Type()
)
aclMacRuleAssignQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleAssignQueueId.setStatus("current")


class _AclMacRuleRedirectIntf_Type(InterfaceIndexOrZero):
    """Custom type aclMacRuleRedirectIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_AclMacRuleRedirectIntf_Type.__name__ = "InterfaceIndexOrZero"
_AclMacRuleRedirectIntf_Object = MibTableColumn
aclMacRuleRedirectIntf = _AclMacRuleRedirectIntf_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 19),
    _AclMacRuleRedirectIntf_Type()
)
aclMacRuleRedirectIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleRedirectIntf.setStatus("current")
_AclMacRuleMatchEvery_Type = TruthValue
_AclMacRuleMatchEvery_Object = MibTableColumn
aclMacRuleMatchEvery = _AclMacRuleMatchEvery_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 20),
    _AclMacRuleMatchEvery_Type()
)
aclMacRuleMatchEvery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleMatchEvery.setStatus("current")


class _AclMacRuleMirrorIntf_Type(InterfaceIndexOrZero):
    """Custom type aclMacRuleMirrorIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_AclMacRuleMirrorIntf_Type.__name__ = "InterfaceIndexOrZero"
_AclMacRuleMirrorIntf_Object = MibTableColumn
aclMacRuleMirrorIntf = _AclMacRuleMirrorIntf_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 21),
    _AclMacRuleMirrorIntf_Type()
)
aclMacRuleMirrorIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleMirrorIntf.setStatus("current")
_AclMacRuleLogging_Type = TruthValue
_AclMacRuleLogging_Object = MibTableColumn
aclMacRuleLogging = _AclMacRuleLogging_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 22),
    _AclMacRuleLogging_Type()
)
aclMacRuleLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleLogging.setStatus("current")


class _AclMacRuleTimeRangeName_Type(DisplayString):
    """Custom type aclMacRuleTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclMacRuleTimeRangeName_Type.__name__ = "DisplayString"
_AclMacRuleTimeRangeName_Object = MibTableColumn
aclMacRuleTimeRangeName = _AclMacRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 23),
    _AclMacRuleTimeRangeName_Type()
)
aclMacRuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacRuleTimeRangeName.setStatus("current")


class _AclMacRuleTimeRangeStatus_Type(Integer32):
    """Custom type aclMacRuleTimeRangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AclMacRuleTimeRangeStatus_Type.__name__ = "Integer32"
_AclMacRuleTimeRangeStatus_Object = MibTableColumn
aclMacRuleTimeRangeStatus = _AclMacRuleTimeRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 7, 1, 24),
    _AclMacRuleTimeRangeStatus_Type()
)
aclMacRuleTimeRangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMacRuleTimeRangeStatus.setStatus("current")
_AclIfTable_Object = MibTable
aclIfTable = _AclIfTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 8)
)
if mibBuilder.loadTexts:
    aclIfTable.setStatus("current")
_AclIfEntry_Object = MibTableRow
aclIfEntry = _AclIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 8, 1)
)
aclIfEntry.setIndexNames(
    (0, "DNOS-QOS-ACL-MIB", "aclIfIndex"),
    (0, "DNOS-QOS-ACL-MIB", "aclIfDirection"),
    (0, "DNOS-QOS-ACL-MIB", "aclIfSequence"),
    (0, "DNOS-QOS-ACL-MIB", "aclIfAclType"),
    (0, "DNOS-QOS-ACL-MIB", "aclIfAclId"),
)
if mibBuilder.loadTexts:
    aclIfEntry.setStatus("current")


class _AclIfIndex_Type(Integer32):
    """Custom type aclIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclIfIndex_Type.__name__ = "Integer32"
_AclIfIndex_Object = MibTableColumn
aclIfIndex = _AclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 8, 1, 1),
    _AclIfIndex_Type()
)
aclIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIfIndex.setStatus("current")


class _AclIfDirection_Type(Integer32):
    """Custom type aclIfDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_AclIfDirection_Type.__name__ = "Integer32"
_AclIfDirection_Object = MibTableColumn
aclIfDirection = _AclIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 8, 1, 2),
    _AclIfDirection_Type()
)
aclIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIfDirection.setStatus("current")


class _AclIfSequence_Type(Unsigned32):
    """Custom type aclIfSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AclIfSequence_Type.__name__ = "Unsigned32"
_AclIfSequence_Object = MibTableColumn
aclIfSequence = _AclIfSequence_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 8, 1, 3),
    _AclIfSequence_Type()
)
aclIfSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIfSequence.setStatus("current")


class _AclIfAclType_Type(Integer32):
    """Custom type aclIfAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2),
          ("ipv6", 3))
    )


_AclIfAclType_Type.__name__ = "Integer32"
_AclIfAclType_Object = MibTableColumn
aclIfAclType = _AclIfAclType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 8, 1, 4),
    _AclIfAclType_Type()
)
aclIfAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIfAclType.setStatus("current")


class _AclIfAclId_Type(Integer32):
    """Custom type aclIfAclId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclIfAclId_Type.__name__ = "Integer32"
_AclIfAclId_Object = MibTableColumn
aclIfAclId = _AclIfAclId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 8, 1, 5),
    _AclIfAclId_Type()
)
aclIfAclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIfAclId.setStatus("current")
_AclIfStatus_Type = RowStatus
_AclIfStatus_Object = MibTableColumn
aclIfStatus = _AclIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 8, 1, 6),
    _AclIfStatus_Type()
)
aclIfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIfStatus.setStatus("current")
_AclLoggingGroup_ObjectIdentity = ObjectIdentity
aclLoggingGroup = _AclLoggingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 9)
)


class _AclTrapRuleIndex_Type(Integer32):
    """Custom type aclTrapRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclTrapRuleIndex_Type.__name__ = "Integer32"
_AclTrapRuleIndex_Object = MibScalar
aclTrapRuleIndex = _AclTrapRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 9, 2),
    _AclTrapRuleIndex_Type()
)
aclTrapRuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aclTrapRuleIndex.setStatus("current")


class _AclTrapRuleAction_Type(Integer32):
    """Custom type aclTrapRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_AclTrapRuleAction_Type.__name__ = "Integer32"
_AclTrapRuleAction_Object = MibScalar
aclTrapRuleAction = _AclTrapRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 9, 3),
    _AclTrapRuleAction_Type()
)
aclTrapRuleAction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aclTrapRuleAction.setStatus("current")
_AclTrapRuleHitCount_Type = Counter64
_AclTrapRuleHitCount_Object = MibScalar
aclTrapRuleHitCount = _AclTrapRuleHitCount_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 9, 4),
    _AclTrapRuleHitCount_Type()
)
aclTrapRuleHitCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aclTrapRuleHitCount.setStatus("current")


class _AclTrapFlag_Type(Integer32):
    """Custom type aclTrapFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AclTrapFlag_Type.__name__ = "Integer32"
_AclTrapFlag_Object = MibScalar
aclTrapFlag = _AclTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 9, 5),
    _AclTrapFlag_Type()
)
aclTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclTrapFlag.setStatus("current")


class _AclTrapRuleTimeRangeName_Type(DisplayString):
    """Custom type aclTrapRuleTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclTrapRuleTimeRangeName_Type.__name__ = "DisplayString"
_AclTrapRuleTimeRangeName_Object = MibScalar
aclTrapRuleTimeRangeName = _AclTrapRuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 9, 6),
    _AclTrapRuleTimeRangeName_Type()
)
aclTrapRuleTimeRangeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aclTrapRuleTimeRangeName.setStatus("current")


class _AclTrapRuleTimeRangeNotification_Type(Integer32):
    """Custom type aclTrapRuleTimeRangeNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("deactivate", 2),
          ("delete", 3))
    )


_AclTrapRuleTimeRangeNotification_Type.__name__ = "Integer32"
_AclTrapRuleTimeRangeNotification_Object = MibScalar
aclTrapRuleTimeRangeNotification = _AclTrapRuleTimeRangeNotification_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 9, 7),
    _AclTrapRuleTimeRangeNotification_Type()
)
aclTrapRuleTimeRangeNotification.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aclTrapRuleTimeRangeNotification.setStatus("current")


class _AclTrapRuleInstallationStatus_Type(Integer32):
    """Custom type aclTrapRuleInstallationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("success", 2))
    )


_AclTrapRuleInstallationStatus_Type.__name__ = "Integer32"
_AclTrapRuleInstallationStatus_Object = MibScalar
aclTrapRuleInstallationStatus = _AclTrapRuleInstallationStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 9, 8),
    _AclTrapRuleInstallationStatus_Type()
)
aclTrapRuleInstallationStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aclTrapRuleInstallationStatus.setStatus("current")
_AclVlanTable_Object = MibTable
aclVlanTable = _AclVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 10)
)
if mibBuilder.loadTexts:
    aclVlanTable.setStatus("current")
_AclVlanEntry_Object = MibTableRow
aclVlanEntry = _AclVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 10, 1)
)
aclVlanEntry.setIndexNames(
    (0, "DNOS-QOS-ACL-MIB", "aclVlanIndex"),
    (0, "DNOS-QOS-ACL-MIB", "aclVlanDirection"),
    (0, "DNOS-QOS-ACL-MIB", "aclVlanSequence"),
    (0, "DNOS-QOS-ACL-MIB", "aclVlanAclType"),
    (0, "DNOS-QOS-ACL-MIB", "aclVlanAclId"),
)
if mibBuilder.loadTexts:
    aclVlanEntry.setStatus("current")


class _AclVlanIndex_Type(Integer32):
    """Custom type aclVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclVlanIndex_Type.__name__ = "Integer32"
_AclVlanIndex_Object = MibTableColumn
aclVlanIndex = _AclVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 10, 1, 1),
    _AclVlanIndex_Type()
)
aclVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclVlanIndex.setStatus("current")


class _AclVlanAclType_Type(Integer32):
    """Custom type aclVlanAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2),
          ("ipv6", 3))
    )


_AclVlanAclType_Type.__name__ = "Integer32"
_AclVlanAclType_Object = MibTableColumn
aclVlanAclType = _AclVlanAclType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 10, 1, 2),
    _AclVlanAclType_Type()
)
aclVlanAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclVlanAclType.setStatus("current")


class _AclVlanAclId_Type(Integer32):
    """Custom type aclVlanAclId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclVlanAclId_Type.__name__ = "Integer32"
_AclVlanAclId_Object = MibTableColumn
aclVlanAclId = _AclVlanAclId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 10, 1, 3),
    _AclVlanAclId_Type()
)
aclVlanAclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclVlanAclId.setStatus("current")


class _AclVlanDirection_Type(Integer32):
    """Custom type aclVlanDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_AclVlanDirection_Type.__name__ = "Integer32"
_AclVlanDirection_Object = MibTableColumn
aclVlanDirection = _AclVlanDirection_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 10, 1, 4),
    _AclVlanDirection_Type()
)
aclVlanDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclVlanDirection.setStatus("current")


class _AclVlanSequence_Type(Unsigned32):
    """Custom type aclVlanSequence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_AclVlanSequence_Type.__name__ = "Unsigned32"
_AclVlanSequence_Object = MibTableColumn
aclVlanSequence = _AclVlanSequence_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 10, 1, 5),
    _AclVlanSequence_Type()
)
aclVlanSequence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclVlanSequence.setStatus("current")
_AclVlanStatus_Type = RowStatus
_AclVlanStatus_Object = MibTableColumn
aclVlanStatus = _AclVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 10, 1, 6),
    _AclVlanStatus_Type()
)
aclVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclVlanStatus.setStatus("current")
_AclIpv6IndexNextFree_Type = Integer32
_AclIpv6IndexNextFree_Object = MibScalar
aclIpv6IndexNextFree = _AclIpv6IndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 11),
    _AclIpv6IndexNextFree_Type()
)
aclIpv6IndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclIpv6IndexNextFree.setStatus("current")
_AclIpv6Table_Object = MibTable
aclIpv6Table = _AclIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 12)
)
if mibBuilder.loadTexts:
    aclIpv6Table.setStatus("current")
_AclIpv6Entry_Object = MibTableRow
aclIpv6Entry = _AclIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 12, 1)
)
aclIpv6Entry.setIndexNames(
    (0, "DNOS-QOS-ACL-MIB", "aclIpv6Index"),
)
if mibBuilder.loadTexts:
    aclIpv6Entry.setStatus("current")


class _AclIpv6Index_Type(Integer32):
    """Custom type aclIpv6Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclIpv6Index_Type.__name__ = "Integer32"
_AclIpv6Index_Object = MibTableColumn
aclIpv6Index = _AclIpv6Index_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 12, 1, 1),
    _AclIpv6Index_Type()
)
aclIpv6Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIpv6Index.setStatus("current")


class _AclIpv6Name_Type(DisplayString):
    """Custom type aclIpv6Name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclIpv6Name_Type.__name__ = "DisplayString"
_AclIpv6Name_Object = MibTableColumn
aclIpv6Name = _AclIpv6Name_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 12, 1, 2),
    _AclIpv6Name_Type()
)
aclIpv6Name.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6Name.setStatus("current")
_AclIpv6Status_Type = RowStatus
_AclIpv6Status_Object = MibTableColumn
aclIpv6Status = _AclIpv6Status_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 12, 1, 3),
    _AclIpv6Status_Type()
)
aclIpv6Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6Status.setStatus("current")
_AclIpv6RuleTable_Object = MibTable
aclIpv6RuleTable = _AclIpv6RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13)
)
if mibBuilder.loadTexts:
    aclIpv6RuleTable.setStatus("current")
_AclIpv6RuleEntry_Object = MibTableRow
aclIpv6RuleEntry = _AclIpv6RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1)
)
aclIpv6RuleEntry.setIndexNames(
    (0, "DNOS-QOS-ACL-MIB", "aclIpv6Index"),
    (0, "DNOS-QOS-ACL-MIB", "aclIpv6RuleIndex"),
)
if mibBuilder.loadTexts:
    aclIpv6RuleEntry.setStatus("current")


class _AclIpv6RuleIndex_Type(Integer32):
    """Custom type aclIpv6RuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclIpv6RuleIndex_Type.__name__ = "Integer32"
_AclIpv6RuleIndex_Object = MibTableColumn
aclIpv6RuleIndex = _AclIpv6RuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 1),
    _AclIpv6RuleIndex_Type()
)
aclIpv6RuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIpv6RuleIndex.setStatus("current")


class _AclIpv6RuleAction_Type(Integer32):
    """Custom type aclIpv6RuleAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_AclIpv6RuleAction_Type.__name__ = "Integer32"
_AclIpv6RuleAction_Object = MibTableColumn
aclIpv6RuleAction = _AclIpv6RuleAction_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 2),
    _AclIpv6RuleAction_Type()
)
aclIpv6RuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleAction.setStatus("current")
_AclIpv6RuleLogging_Type = TruthValue
_AclIpv6RuleLogging_Object = MibTableColumn
aclIpv6RuleLogging = _AclIpv6RuleLogging_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 3),
    _AclIpv6RuleLogging_Type()
)
aclIpv6RuleLogging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleLogging.setStatus("current")
_AclIpv6RuleAssignQueueId_Type = Unsigned32
_AclIpv6RuleAssignQueueId_Object = MibTableColumn
aclIpv6RuleAssignQueueId = _AclIpv6RuleAssignQueueId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 4),
    _AclIpv6RuleAssignQueueId_Type()
)
aclIpv6RuleAssignQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleAssignQueueId.setStatus("current")


class _AclIpv6RuleRedirectIntf_Type(InterfaceIndexOrZero):
    """Custom type aclIpv6RuleRedirectIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_AclIpv6RuleRedirectIntf_Type.__name__ = "InterfaceIndexOrZero"
_AclIpv6RuleRedirectIntf_Object = MibTableColumn
aclIpv6RuleRedirectIntf = _AclIpv6RuleRedirectIntf_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 5),
    _AclIpv6RuleRedirectIntf_Type()
)
aclIpv6RuleRedirectIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleRedirectIntf.setStatus("current")


class _AclIpv6RuleMirrorIntf_Type(InterfaceIndexOrZero):
    """Custom type aclIpv6RuleMirrorIntf based on InterfaceIndexOrZero"""
    defaultValue = 0


_AclIpv6RuleMirrorIntf_Type.__name__ = "InterfaceIndexOrZero"
_AclIpv6RuleMirrorIntf_Object = MibTableColumn
aclIpv6RuleMirrorIntf = _AclIpv6RuleMirrorIntf_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 6),
    _AclIpv6RuleMirrorIntf_Type()
)
aclIpv6RuleMirrorIntf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleMirrorIntf.setStatus("current")
_AclIpv6RuleMatchEvery_Type = TruthValue
_AclIpv6RuleMatchEvery_Object = MibTableColumn
aclIpv6RuleMatchEvery = _AclIpv6RuleMatchEvery_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 7),
    _AclIpv6RuleMatchEvery_Type()
)
aclIpv6RuleMatchEvery.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleMatchEvery.setStatus("current")


class _AclIpv6RuleProtocol_Type(Integer32):
    """Custom type aclIpv6RuleProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AclIpv6RuleProtocol_Type.__name__ = "Integer32"
_AclIpv6RuleProtocol_Object = MibTableColumn
aclIpv6RuleProtocol = _AclIpv6RuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 8),
    _AclIpv6RuleProtocol_Type()
)
aclIpv6RuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleProtocol.setStatus("current")
_AclIpv6RuleSrcL4Port_Type = Integer32
_AclIpv6RuleSrcL4Port_Object = MibTableColumn
aclIpv6RuleSrcL4Port = _AclIpv6RuleSrcL4Port_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 9),
    _AclIpv6RuleSrcL4Port_Type()
)
aclIpv6RuleSrcL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleSrcL4Port.setStatus("current")
_AclIpv6RuleSrcL4PortRangeStart_Type = Integer32
_AclIpv6RuleSrcL4PortRangeStart_Object = MibTableColumn
aclIpv6RuleSrcL4PortRangeStart = _AclIpv6RuleSrcL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 10),
    _AclIpv6RuleSrcL4PortRangeStart_Type()
)
aclIpv6RuleSrcL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleSrcL4PortRangeStart.setStatus("current")
_AclIpv6RuleSrcL4PortRangeEnd_Type = Integer32
_AclIpv6RuleSrcL4PortRangeEnd_Object = MibTableColumn
aclIpv6RuleSrcL4PortRangeEnd = _AclIpv6RuleSrcL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 11),
    _AclIpv6RuleSrcL4PortRangeEnd_Type()
)
aclIpv6RuleSrcL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleSrcL4PortRangeEnd.setStatus("current")
_AclIpv6RuleDestL4Port_Type = Integer32
_AclIpv6RuleDestL4Port_Object = MibTableColumn
aclIpv6RuleDestL4Port = _AclIpv6RuleDestL4Port_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 12),
    _AclIpv6RuleDestL4Port_Type()
)
aclIpv6RuleDestL4Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleDestL4Port.setStatus("current")
_AclIpv6RuleDestL4PortRangeStart_Type = Integer32
_AclIpv6RuleDestL4PortRangeStart_Object = MibTableColumn
aclIpv6RuleDestL4PortRangeStart = _AclIpv6RuleDestL4PortRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 13),
    _AclIpv6RuleDestL4PortRangeStart_Type()
)
aclIpv6RuleDestL4PortRangeStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleDestL4PortRangeStart.setStatus("current")
_AclIpv6RuleDestL4PortRangeEnd_Type = Integer32
_AclIpv6RuleDestL4PortRangeEnd_Object = MibTableColumn
aclIpv6RuleDestL4PortRangeEnd = _AclIpv6RuleDestL4PortRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 14),
    _AclIpv6RuleDestL4PortRangeEnd_Type()
)
aclIpv6RuleDestL4PortRangeEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleDestL4PortRangeEnd.setStatus("current")
_AclIpv6RuleStatus_Type = RowStatus
_AclIpv6RuleStatus_Object = MibTableColumn
aclIpv6RuleStatus = _AclIpv6RuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 15),
    _AclIpv6RuleStatus_Type()
)
aclIpv6RuleStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleStatus.setStatus("current")


class _AclIpv6RuleFlowLabel_Type(Integer32):
    """Custom type aclIpv6RuleFlowLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_AclIpv6RuleFlowLabel_Type.__name__ = "Integer32"
_AclIpv6RuleFlowLabel_Object = MibTableColumn
aclIpv6RuleFlowLabel = _AclIpv6RuleFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 16),
    _AclIpv6RuleFlowLabel_Type()
)
aclIpv6RuleFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleFlowLabel.setStatus("current")
_AclIpv6RuleIPDSCP_Type = Integer32
_AclIpv6RuleIPDSCP_Object = MibTableColumn
aclIpv6RuleIPDSCP = _AclIpv6RuleIPDSCP_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 17),
    _AclIpv6RuleIPDSCP_Type()
)
aclIpv6RuleIPDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleIPDSCP.setStatus("current")
_AclRuleSrcIpv6Prefix_Type = Ipv6AddressPrefix
_AclRuleSrcIpv6Prefix_Object = MibTableColumn
aclRuleSrcIpv6Prefix = _AclRuleSrcIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 18),
    _AclRuleSrcIpv6Prefix_Type()
)
aclRuleSrcIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclRuleSrcIpv6Prefix.setStatus("current")


class _AclRuleSrcIpv6PrefixLength_Type(Integer32):
    """Custom type aclRuleSrcIpv6PrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AclRuleSrcIpv6PrefixLength_Type.__name__ = "Integer32"
_AclRuleSrcIpv6PrefixLength_Object = MibTableColumn
aclRuleSrcIpv6PrefixLength = _AclRuleSrcIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 19),
    _AclRuleSrcIpv6PrefixLength_Type()
)
aclRuleSrcIpv6PrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleSrcIpv6PrefixLength.setStatus("current")
_AclRuleDstIpv6Prefix_Type = Ipv6AddressPrefix
_AclRuleDstIpv6Prefix_Object = MibTableColumn
aclRuleDstIpv6Prefix = _AclRuleDstIpv6Prefix_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 20),
    _AclRuleDstIpv6Prefix_Type()
)
aclRuleDstIpv6Prefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclRuleDstIpv6Prefix.setStatus("current")


class _AclRuleDstIpv6PrefixLength_Type(Integer32):
    """Custom type aclRuleDstIpv6PrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AclRuleDstIpv6PrefixLength_Type.__name__ = "Integer32"
_AclRuleDstIpv6PrefixLength_Object = MibTableColumn
aclRuleDstIpv6PrefixLength = _AclRuleDstIpv6PrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 21),
    _AclRuleDstIpv6PrefixLength_Type()
)
aclRuleDstIpv6PrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRuleDstIpv6PrefixLength.setStatus("current")


class _AclIpv6RuleTimeRangeName_Type(DisplayString):
    """Custom type aclIpv6RuleTimeRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclIpv6RuleTimeRangeName_Type.__name__ = "DisplayString"
_AclIpv6RuleTimeRangeName_Object = MibTableColumn
aclIpv6RuleTimeRangeName = _AclIpv6RuleTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 22),
    _AclIpv6RuleTimeRangeName_Type()
)
aclIpv6RuleTimeRangeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleTimeRangeName.setStatus("current")


class _AclIpv6RuleTimeRangeStatus_Type(Integer32):
    """Custom type aclIpv6RuleTimeRangeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AclIpv6RuleTimeRangeStatus_Type.__name__ = "Integer32"
_AclIpv6RuleTimeRangeStatus_Object = MibTableColumn
aclIpv6RuleTimeRangeStatus = _AclIpv6RuleTimeRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 23),
    _AclIpv6RuleTimeRangeStatus_Type()
)
aclIpv6RuleTimeRangeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclIpv6RuleTimeRangeStatus.setStatus("current")
_AclIpv6RuleRateLimitCrate_Type = Unsigned32
_AclIpv6RuleRateLimitCrate_Object = MibTableColumn
aclIpv6RuleRateLimitCrate = _AclIpv6RuleRateLimitCrate_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 24),
    _AclIpv6RuleRateLimitCrate_Type()
)
aclIpv6RuleRateLimitCrate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleRateLimitCrate.setStatus("current")
_AclIpv6RuleRateLimitCburst_Type = AclBurstSize
_AclIpv6RuleRateLimitCburst_Object = MibTableColumn
aclIpv6RuleRateLimitCburst = _AclIpv6RuleRateLimitCburst_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 25),
    _AclIpv6RuleRateLimitCburst_Type()
)
aclIpv6RuleRateLimitCburst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleRateLimitCburst.setStatus("current")


class _AclIpv6RuleIcmpType_Type(Integer32):
    """Custom type aclIpv6RuleIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclIpv6RuleIcmpType_Type.__name__ = "Integer32"
_AclIpv6RuleIcmpType_Object = MibTableColumn
aclIpv6RuleIcmpType = _AclIpv6RuleIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 27),
    _AclIpv6RuleIcmpType_Type()
)
aclIpv6RuleIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleIcmpType.setStatus("current")


class _AclIpv6RuleIcmpCode_Type(Integer32):
    """Custom type aclIpv6RuleIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclIpv6RuleIcmpCode_Type.__name__ = "Integer32"
_AclIpv6RuleIcmpCode_Object = MibTableColumn
aclIpv6RuleIcmpCode = _AclIpv6RuleIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 28),
    _AclIpv6RuleIcmpCode_Type()
)
aclIpv6RuleIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleIcmpCode.setStatus("current")
_AclIpv6RuleRouting_Type = TruthValue
_AclIpv6RuleRouting_Object = MibTableColumn
aclIpv6RuleRouting = _AclIpv6RuleRouting_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 29),
    _AclIpv6RuleRouting_Type()
)
aclIpv6RuleRouting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleRouting.setStatus("current")
_AclIpv6RuleFragments_Type = TruthValue
_AclIpv6RuleFragments_Object = MibTableColumn
aclIpv6RuleFragments = _AclIpv6RuleFragments_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 30),
    _AclIpv6RuleFragments_Type()
)
aclIpv6RuleFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleFragments.setStatus("current")
_AclIpv6RuleEstablished_Type = TruthValue
_AclIpv6RuleEstablished_Object = MibTableColumn
aclIpv6RuleEstablished = _AclIpv6RuleEstablished_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 13, 1, 31),
    _AclIpv6RuleEstablished_Type()
)
aclIpv6RuleEstablished.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpv6RuleEstablished.setStatus("current")
_AclNamedIpv4IndexNextFree_Type = Integer32
_AclNamedIpv4IndexNextFree_Object = MibScalar
aclNamedIpv4IndexNextFree = _AclNamedIpv4IndexNextFree_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 14),
    _AclNamedIpv4IndexNextFree_Type()
)
aclNamedIpv4IndexNextFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedIpv4IndexNextFree.setStatus("current")

# Managed Objects groups


# Notification objects

aclTrapRuleLogEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 0, 1)
)
aclTrapRuleLogEvent.setObjects(
      *(("DNOS-QOS-ACL-MIB", "aclIfAclType"),
        ("DNOS-QOS-ACL-MIB", "aclIfAclId"),
        ("DNOS-QOS-ACL-MIB", "aclTrapRuleIndex"),
        ("DNOS-QOS-ACL-MIB", "aclTrapRuleAction"),
        ("DNOS-QOS-ACL-MIB", "aclTrapRuleHitCount"))
)
if mibBuilder.loadTexts:
    aclTrapRuleLogEvent.setStatus(
        "current"
    )

aclTrapRuleTimeRangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 3, 2, 0, 2)
)
aclTrapRuleTimeRangeEvent.setObjects(
      *(("DNOS-QOS-ACL-MIB", "aclIfAclType"),
        ("DNOS-QOS-ACL-MIB", "aclIfAclId"),
        ("DNOS-QOS-ACL-MIB", "aclTrapRuleIndex"),
        ("DNOS-QOS-ACL-MIB", "aclTrapRuleTimeRangeName"),
        ("DNOS-QOS-ACL-MIB", "aclTrapRuleTimeRangeNotification"),
        ("DNOS-QOS-ACL-MIB", "aclTrapRuleInstallationStatus"))
)
if mibBuilder.loadTexts:
    aclTrapRuleTimeRangeEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-QOS-ACL-MIB",
    **{"EtypeValue": EtypeValue,
       "Ipv6AddressPrefix": Ipv6AddressPrefix,
       "AclBurstSize": AclBurstSize,
       "fastPathQOSACL": fastPathQOSACL,
       "aclNotifications": aclNotifications,
       "aclTrapRuleLogEvent": aclTrapRuleLogEvent,
       "aclTrapRuleTimeRangeEvent": aclTrapRuleTimeRangeEvent,
       "aclTable": aclTable,
       "aclEntry": aclEntry,
       "aclIndex": aclIndex,
       "aclName": aclName,
       "aclStatus": aclStatus,
       "aclRuleTable": aclRuleTable,
       "aclRuleEntry": aclRuleEntry,
       "aclRuleIndex": aclRuleIndex,
       "aclRuleAction": aclRuleAction,
       "aclRuleProtocol": aclRuleProtocol,
       "aclRuleSrcIpAddress": aclRuleSrcIpAddress,
       "aclRuleSrcIpMask": aclRuleSrcIpMask,
       "aclRuleSrcL4Port": aclRuleSrcL4Port,
       "aclRuleSrcL4PortRangeStart": aclRuleSrcL4PortRangeStart,
       "aclRuleSrcL4PortRangeEnd": aclRuleSrcL4PortRangeEnd,
       "aclRuleDestIpAddress": aclRuleDestIpAddress,
       "aclRuleDestIpMask": aclRuleDestIpMask,
       "aclRuleDestL4Port": aclRuleDestL4Port,
       "aclRuleDestL4PortRangeStart": aclRuleDestL4PortRangeStart,
       "aclRuleDestL4PortRangeEnd": aclRuleDestL4PortRangeEnd,
       "aclRuleIPDSCP": aclRuleIPDSCP,
       "aclRuleIpPrecedence": aclRuleIpPrecedence,
       "aclRuleIpTosBits": aclRuleIpTosBits,
       "aclRuleIpTosMask": aclRuleIpTosMask,
       "aclRuleStatus": aclRuleStatus,
       "aclRuleAssignQueueId": aclRuleAssignQueueId,
       "aclRuleRedirectIntf": aclRuleRedirectIntf,
       "aclRuleMatchEvery": aclRuleMatchEvery,
       "aclRuleMirrorIntf": aclRuleMirrorIntf,
       "aclRuleLogging": aclRuleLogging,
       "aclRuleTimeRangeName": aclRuleTimeRangeName,
       "aclRuleTimeRangeStatus": aclRuleTimeRangeStatus,
       "aclRuleRateLimitCrate": aclRuleRateLimitCrate,
       "aclRuleRateLimitCburst": aclRuleRateLimitCburst,
       "aclRuleIcmpType": aclRuleIcmpType,
       "aclRuleIcmpCode": aclRuleIcmpCode,
       "aclRuleIgmpType": aclRuleIgmpType,
       "aclRuleEstablished": aclRuleEstablished,
       "aclRuleFragments": aclRuleFragments,
       "aclMacIndexNextFree": aclMacIndexNextFree,
       "aclMacTable": aclMacTable,
       "aclMacEntry": aclMacEntry,
       "aclMacIndex": aclMacIndex,
       "aclMacName": aclMacName,
       "aclMacStatus": aclMacStatus,
       "aclMacRuleTable": aclMacRuleTable,
       "aclMacRuleEntry": aclMacRuleEntry,
       "aclMacRuleIndex": aclMacRuleIndex,
       "aclMacRuleAction": aclMacRuleAction,
       "aclMacRuleCos": aclMacRuleCos,
       "aclMacRuleCos2": aclMacRuleCos2,
       "aclMacRuleDestMacAddr": aclMacRuleDestMacAddr,
       "aclMacRuleDestMacMask": aclMacRuleDestMacMask,
       "aclMacRuleEtypeKey": aclMacRuleEtypeKey,
       "aclMacRuleEtypeValue": aclMacRuleEtypeValue,
       "aclMacRuleSrcMacAddr": aclMacRuleSrcMacAddr,
       "aclMacRuleSrcMacMask": aclMacRuleSrcMacMask,
       "aclMacRuleVlanId": aclMacRuleVlanId,
       "aclMacRuleVlanIdRangeStart": aclMacRuleVlanIdRangeStart,
       "aclMacRuleVlanIdRangeEnd": aclMacRuleVlanIdRangeEnd,
       "aclMacRuleVlanId2": aclMacRuleVlanId2,
       "aclMacRuleVlanId2RangeStart": aclMacRuleVlanId2RangeStart,
       "aclMacRuleVlanId2RangeEnd": aclMacRuleVlanId2RangeEnd,
       "aclMacRuleStatus": aclMacRuleStatus,
       "aclMacRuleAssignQueueId": aclMacRuleAssignQueueId,
       "aclMacRuleRedirectIntf": aclMacRuleRedirectIntf,
       "aclMacRuleMatchEvery": aclMacRuleMatchEvery,
       "aclMacRuleMirrorIntf": aclMacRuleMirrorIntf,
       "aclMacRuleLogging": aclMacRuleLogging,
       "aclMacRuleTimeRangeName": aclMacRuleTimeRangeName,
       "aclMacRuleTimeRangeStatus": aclMacRuleTimeRangeStatus,
       "aclIfTable": aclIfTable,
       "aclIfEntry": aclIfEntry,
       "aclIfIndex": aclIfIndex,
       "aclIfDirection": aclIfDirection,
       "aclIfSequence": aclIfSequence,
       "aclIfAclType": aclIfAclType,
       "aclIfAclId": aclIfAclId,
       "aclIfStatus": aclIfStatus,
       "aclLoggingGroup": aclLoggingGroup,
       "aclTrapRuleIndex": aclTrapRuleIndex,
       "aclTrapRuleAction": aclTrapRuleAction,
       "aclTrapRuleHitCount": aclTrapRuleHitCount,
       "aclTrapFlag": aclTrapFlag,
       "aclTrapRuleTimeRangeName": aclTrapRuleTimeRangeName,
       "aclTrapRuleTimeRangeNotification": aclTrapRuleTimeRangeNotification,
       "aclTrapRuleInstallationStatus": aclTrapRuleInstallationStatus,
       "aclVlanTable": aclVlanTable,
       "aclVlanEntry": aclVlanEntry,
       "aclVlanIndex": aclVlanIndex,
       "aclVlanAclType": aclVlanAclType,
       "aclVlanAclId": aclVlanAclId,
       "aclVlanDirection": aclVlanDirection,
       "aclVlanSequence": aclVlanSequence,
       "aclVlanStatus": aclVlanStatus,
       "aclIpv6IndexNextFree": aclIpv6IndexNextFree,
       "aclIpv6Table": aclIpv6Table,
       "aclIpv6Entry": aclIpv6Entry,
       "aclIpv6Index": aclIpv6Index,
       "aclIpv6Name": aclIpv6Name,
       "aclIpv6Status": aclIpv6Status,
       "aclIpv6RuleTable": aclIpv6RuleTable,
       "aclIpv6RuleEntry": aclIpv6RuleEntry,
       "aclIpv6RuleIndex": aclIpv6RuleIndex,
       "aclIpv6RuleAction": aclIpv6RuleAction,
       "aclIpv6RuleLogging": aclIpv6RuleLogging,
       "aclIpv6RuleAssignQueueId": aclIpv6RuleAssignQueueId,
       "aclIpv6RuleRedirectIntf": aclIpv6RuleRedirectIntf,
       "aclIpv6RuleMirrorIntf": aclIpv6RuleMirrorIntf,
       "aclIpv6RuleMatchEvery": aclIpv6RuleMatchEvery,
       "aclIpv6RuleProtocol": aclIpv6RuleProtocol,
       "aclIpv6RuleSrcL4Port": aclIpv6RuleSrcL4Port,
       "aclIpv6RuleSrcL4PortRangeStart": aclIpv6RuleSrcL4PortRangeStart,
       "aclIpv6RuleSrcL4PortRangeEnd": aclIpv6RuleSrcL4PortRangeEnd,
       "aclIpv6RuleDestL4Port": aclIpv6RuleDestL4Port,
       "aclIpv6RuleDestL4PortRangeStart": aclIpv6RuleDestL4PortRangeStart,
       "aclIpv6RuleDestL4PortRangeEnd": aclIpv6RuleDestL4PortRangeEnd,
       "aclIpv6RuleStatus": aclIpv6RuleStatus,
       "aclIpv6RuleFlowLabel": aclIpv6RuleFlowLabel,
       "aclIpv6RuleIPDSCP": aclIpv6RuleIPDSCP,
       "aclRuleSrcIpv6Prefix": aclRuleSrcIpv6Prefix,
       "aclRuleSrcIpv6PrefixLength": aclRuleSrcIpv6PrefixLength,
       "aclRuleDstIpv6Prefix": aclRuleDstIpv6Prefix,
       "aclRuleDstIpv6PrefixLength": aclRuleDstIpv6PrefixLength,
       "aclIpv6RuleTimeRangeName": aclIpv6RuleTimeRangeName,
       "aclIpv6RuleTimeRangeStatus": aclIpv6RuleTimeRangeStatus,
       "aclIpv6RuleRateLimitCrate": aclIpv6RuleRateLimitCrate,
       "aclIpv6RuleRateLimitCburst": aclIpv6RuleRateLimitCburst,
       "aclIpv6RuleIcmpType": aclIpv6RuleIcmpType,
       "aclIpv6RuleIcmpCode": aclIpv6RuleIcmpCode,
       "aclIpv6RuleRouting": aclIpv6RuleRouting,
       "aclIpv6RuleFragments": aclIpv6RuleFragments,
       "aclIpv6RuleEstablished": aclIpv6RuleEstablished,
       "aclNamedIpv4IndexNextFree": aclNamedIpv4IndexNextFree}
)
