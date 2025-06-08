# SNMP MIB module (JUNIPER-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/juniper_2636/JUNIPER-NAT-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 31 15:30:07 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
    "InetAddressType")

(jnxSvcsMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxSvcsMibRoot")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxNatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1)
)
if mibBuilder.loadTexts:
    jnxNatMIB.setRevisions(
        ("2010-07-12 20:22",
         "2020-08-27 20:22")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxNatNotifications_ObjectIdentity = ObjectIdentity
jnxNatNotifications = _JnxNatNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 0)
)
_JnxNatObjects_ObjectIdentity = ObjectIdentity
jnxNatObjects = _JnxNatObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1)
)
_JnxSrcNatStatsTable_Object = MibTable
jnxSrcNatStatsTable = _JnxSrcNatStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxSrcNatStatsTable.setStatus("current")
_JnxSrcNatStatsEntry_Object = MibTableRow
jnxSrcNatStatsEntry = _JnxSrcNatStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1)
)
jnxSrcNatStatsEntry.setIndexNames(
    (0, "JUNIPER-NAT-MIB", "jnxNatSrcPoolName"),
)
if mibBuilder.loadTexts:
    jnxSrcNatStatsEntry.setStatus("current")


class _JnxNatSrcPoolName_Type(DisplayString):
    """Custom type jnxNatSrcPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxNatSrcPoolName_Type.__name__ = "DisplayString"
_JnxNatSrcPoolName_Object = MibTableColumn
jnxNatSrcPoolName = _JnxNatSrcPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 1),
    _JnxNatSrcPoolName_Type()
)
jnxNatSrcPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxNatSrcPoolName.setStatus("current")


class _JnxNatSrcXlatedAddrType_Type(Integer32):
    """Custom type jnxNatSrcXlatedAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_JnxNatSrcXlatedAddrType_Type.__name__ = "Integer32"
_JnxNatSrcXlatedAddrType_Object = MibTableColumn
jnxNatSrcXlatedAddrType = _JnxNatSrcXlatedAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 2),
    _JnxNatSrcXlatedAddrType_Type()
)
jnxNatSrcXlatedAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcXlatedAddrType.setStatus("current")


class _JnxNatSrcPoolType_Type(Integer32):
    """Custom type jnxNatSrcPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic-napt", 2),
          ("dynamic-nat", 3),
          ("basic-nat44", 11),
          ("dynamic-nat44", 12),
          ("napt-44", 13),
          ("dnat-44", 14),
          ("stateful-nat64", 15),
          ("stateless-nat64", 16),
          ("basic-nat-pt", 17),
          ("napt-pt", 18),
          ("basic-nat66", 19),
          ("stateless-nat66", 20),
          ("napt-66", 21),
          ("twice-napt-44", 22),
          ("twice-basic-nat-44", 23),
          ("twice-dynamic-nat-44", 24),
          ("det-napt44", 25),
          ("sd-napt44", 26))
    )


_JnxNatSrcPoolType_Type.__name__ = "Integer32"
_JnxNatSrcPoolType_Object = MibTableColumn
jnxNatSrcPoolType = _JnxNatSrcPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 3),
    _JnxNatSrcPoolType_Type()
)
jnxNatSrcPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcPoolType.setStatus("current")
_JnxNatSrcNumPortAvail_Type = Unsigned32
_JnxNatSrcNumPortAvail_Object = MibTableColumn
jnxNatSrcNumPortAvail = _JnxNatSrcNumPortAvail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 4),
    _JnxNatSrcNumPortAvail_Type()
)
jnxNatSrcNumPortAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcNumPortAvail.setStatus("current")
_JnxNatSrcNumPortInuse_Type = Unsigned32
_JnxNatSrcNumPortInuse_Object = MibTableColumn
jnxNatSrcNumPortInuse = _JnxNatSrcNumPortInuse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 5),
    _JnxNatSrcNumPortInuse_Type()
)
jnxNatSrcNumPortInuse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcNumPortInuse.setStatus("current")
_JnxNatSrcNumAddressAvail_Type = Unsigned32
_JnxNatSrcNumAddressAvail_Object = MibTableColumn
jnxNatSrcNumAddressAvail = _JnxNatSrcNumAddressAvail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 6),
    _JnxNatSrcNumAddressAvail_Type()
)
jnxNatSrcNumAddressAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcNumAddressAvail.setStatus("current")
_JnxNatSrcNumAddressInUse_Type = Unsigned32
_JnxNatSrcNumAddressInUse_Object = MibTableColumn
jnxNatSrcNumAddressInUse = _JnxNatSrcNumAddressInUse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 7),
    _JnxNatSrcNumAddressInUse_Type()
)
jnxNatSrcNumAddressInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcNumAddressInUse.setStatus("current")
_JnxNatSrcNumSessions_Type = Unsigned32
_JnxNatSrcNumSessions_Object = MibTableColumn
jnxNatSrcNumSessions = _JnxNatSrcNumSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 8),
    _JnxNatSrcNumSessions_Type()
)
jnxNatSrcNumSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcNumSessions.setStatus("current")
_JnxNatSrcNumAddressMapped_Type = Unsigned32
_JnxNatSrcNumAddressMapped_Object = MibTableColumn
jnxNatSrcNumAddressMapped = _JnxNatSrcNumAddressMapped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 1, 1, 9),
    _JnxNatSrcNumAddressMapped_Type()
)
jnxNatSrcNumAddressMapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatSrcNumAddressMapped.setStatus("current")
_JnxNatRuleTable_Object = MibTable
jnxNatRuleTable = _JnxNatRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxNatRuleTable.setStatus("current")
_JnxNatRuleEntry_Object = MibTableRow
jnxNatRuleEntry = _JnxNatRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1)
)
jnxNatRuleEntry.setIndexNames(
    (0, "JUNIPER-NAT-MIB", "jnxNatRuleName"),
)
if mibBuilder.loadTexts:
    jnxNatRuleEntry.setStatus("current")


class _JnxNatRuleName_Type(DisplayString):
    """Custom type jnxNatRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_JnxNatRuleName_Type.__name__ = "DisplayString"
_JnxNatRuleName_Object = MibTableColumn
jnxNatRuleName = _JnxNatRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1, 1),
    _JnxNatRuleName_Type()
)
jnxNatRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxNatRuleName.setStatus("current")


class _JnxNatRuleType_Type(Integer32):
    """Custom type jnxNatRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("static-source", 1),
          ("static-destination", 2),
          ("dynamic-source", 3),
          ("napt", 4),
          ("basic-nat44", 11),
          ("dynamic-nat44", 12),
          ("napt-44", 13),
          ("dnat-44", 14),
          ("stateful-nat64", 15),
          ("stateless-nat64", 16),
          ("basic-nat-pt", 17),
          ("napt-pt", 18),
          ("basic-nat66", 19),
          ("stateless-nat66", 20),
          ("napt-66", 21),
          ("twice-napt-44", 22),
          ("twice-basic-nat-44", 23),
          ("twice-dynamic-nat-44", 24),
          ("det-napt44", 25),
          ("sd-napt44", 26))
    )


_JnxNatRuleType_Type.__name__ = "Integer32"
_JnxNatRuleType_Object = MibTableColumn
jnxNatRuleType = _JnxNatRuleType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1, 2),
    _JnxNatRuleType_Type()
)
jnxNatRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatRuleType.setStatus("current")
_JnxNatRuleTransHits_Type = Unsigned32
_JnxNatRuleTransHits_Object = MibTableColumn
jnxNatRuleTransHits = _JnxNatRuleTransHits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 2, 1, 3),
    _JnxNatRuleTransHits_Type()
)
jnxNatRuleTransHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatRuleTransHits.setStatus("current")
_JnxNatPoolTable_Object = MibTable
jnxNatPoolTable = _JnxNatPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxNatPoolTable.setStatus("current")
_JnxNatPoolEntry_Object = MibTableRow
jnxNatPoolEntry = _JnxNatPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1)
)
jnxNatPoolEntry.setIndexNames(
    (0, "JUNIPER-NAT-MIB", "jnxNatPoolName"),
)
if mibBuilder.loadTexts:
    jnxNatPoolEntry.setStatus("current")


class _JnxNatPoolName_Type(DisplayString):
    """Custom type jnxNatPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxNatPoolName_Type.__name__ = "DisplayString"
_JnxNatPoolName_Object = MibTableColumn
jnxNatPoolName = _JnxNatPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1, 1),
    _JnxNatPoolName_Type()
)
jnxNatPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxNatPoolName.setStatus("current")


class _JnxNatPoolType_Type(Integer32):
    """Custom type jnxNatPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("static-source", 1),
          ("static-destination", 2),
          ("dynamic-source", 3),
          ("napt", 4),
          ("basic-nat44", 11),
          ("dynamic-nat44", 12),
          ("napt-44", 13),
          ("dnat-44", 14),
          ("stateful-nat64", 15),
          ("stateless-nat64", 16),
          ("basic-nat-pt", 17),
          ("napt-pt", 18),
          ("basic-nat66", 19),
          ("stateless-nat66", 20),
          ("napt-66", 21),
          ("twice-napt-44", 22),
          ("twice-basic-nat-44", 23),
          ("twice-dynamic-nat-44", 24),
          ("det-napt44", 25),
          ("sd-napt44", 26))
    )


_JnxNatPoolType_Type.__name__ = "Integer32"
_JnxNatPoolType_Object = MibTableColumn
jnxNatPoolType = _JnxNatPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1, 2),
    _JnxNatPoolType_Type()
)
jnxNatPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatPoolType.setStatus("current")
_JnxNatPoolTransHits_Type = Unsigned32
_JnxNatPoolTransHits_Object = MibTableColumn
jnxNatPoolTransHits = _JnxNatPoolTransHits_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 3, 1, 3),
    _JnxNatPoolTransHits_Type()
)
jnxNatPoolTransHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatPoolTransHits.setStatus("current")
_JnxNatPbaStatsTable_Object = MibTable
jnxNatPbaStatsTable = _JnxNatPbaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 4)
)
if mibBuilder.loadTexts:
    jnxNatPbaStatsTable.setStatus("current")
_JnxNatPbaStatsEntry_Object = MibTableRow
jnxNatPbaStatsEntry = _JnxNatPbaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 4, 1)
)
jnxNatPbaStatsEntry.setIndexNames(
    (0, "JUNIPER-NAT-MIB", "jnxNatPbaPoolName"),
)
if mibBuilder.loadTexts:
    jnxNatPbaStatsEntry.setStatus("current")


class _JnxNatPbaPoolName_Type(DisplayString):
    """Custom type jnxNatPbaPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JnxNatPbaPoolName_Type.__name__ = "DisplayString"
_JnxNatPbaPoolName_Object = MibTableColumn
jnxNatPbaPoolName = _JnxNatPbaPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 4, 1, 1),
    _JnxNatPbaPoolName_Type()
)
jnxNatPbaPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatPbaPoolName.setStatus("current")
_JnxNatPbaOutOfPortError_Type = Unsigned32
_JnxNatPbaOutOfPortError_Object = MibTableColumn
jnxNatPbaOutOfPortError = _JnxNatPbaOutOfPortError_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 4, 1, 2),
    _JnxNatPbaOutOfPortError_Type()
)
jnxNatPbaOutOfPortError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatPbaOutOfPortError.setStatus("current")
_JnxNatPbaMaxNumberOfPortBlocksUsed_Type = Unsigned32
_JnxNatPbaMaxNumberOfPortBlocksUsed_Object = MibTableColumn
jnxNatPbaMaxNumberOfPortBlocksUsed = _JnxNatPbaMaxNumberOfPortBlocksUsed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 4, 1, 3),
    _JnxNatPbaMaxNumberOfPortBlocksUsed_Type()
)
jnxNatPbaMaxNumberOfPortBlocksUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatPbaMaxNumberOfPortBlocksUsed.setStatus("current")
_JnxNatPbaCurrentNumberOfPortBlocksInUse_Type = Unsigned32
_JnxNatPbaCurrentNumberOfPortBlocksInUse_Object = MibTableColumn
jnxNatPbaCurrentNumberOfPortBlocksInUse = _JnxNatPbaCurrentNumberOfPortBlocksInUse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 4, 1, 4),
    _JnxNatPbaCurrentNumberOfPortBlocksInUse_Type()
)
jnxNatPbaCurrentNumberOfPortBlocksInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatPbaCurrentNumberOfPortBlocksInUse.setStatus("current")
_JnxNatPbaPortBlockAllocErrors_Type = Unsigned32
_JnxNatPbaPortBlockAllocErrors_Object = MibTableColumn
jnxNatPbaPortBlockAllocErrors = _JnxNatPbaPortBlockAllocErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 4, 1, 5),
    _JnxNatPbaPortBlockAllocErrors_Type()
)
jnxNatPbaPortBlockAllocErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatPbaPortBlockAllocErrors.setStatus("current")
_JnxNatPbaPortBlockMemAllocErrors_Type = Unsigned32
_JnxNatPbaPortBlockMemAllocErrors_Object = MibTableColumn
jnxNatPbaPortBlockMemAllocErrors = _JnxNatPbaPortBlockMemAllocErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 4, 1, 6),
    _JnxNatPbaPortBlockMemAllocErrors_Type()
)
jnxNatPbaPortBlockMemAllocErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatPbaPortBlockMemAllocErrors.setStatus("current")
_JnxNatPbaPortBlockLimitExeededErrors_Type = Unsigned32
_JnxNatPbaPortBlockLimitExeededErrors_Object = MibTableColumn
jnxNatPbaPortBlockLimitExeededErrors = _JnxNatPbaPortBlockLimitExeededErrors_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 1, 4, 1, 7),
    _JnxNatPbaPortBlockLimitExeededErrors_Type()
)
jnxNatPbaPortBlockLimitExeededErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxNatPbaPortBlockLimitExeededErrors.setStatus("current")
_JnxNatTrapVars_ObjectIdentity = ObjectIdentity
jnxNatTrapVars = _JnxNatTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 2)
)


class _JnxNatAddrPoolUtil_Type(Integer32):
    """Custom type jnxNatAddrPoolUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JnxNatAddrPoolUtil_Type.__name__ = "Integer32"
_JnxNatAddrPoolUtil_Object = MibScalar
jnxNatAddrPoolUtil = _JnxNatAddrPoolUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 2, 1),
    _JnxNatAddrPoolUtil_Type()
)
jnxNatAddrPoolUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxNatAddrPoolUtil.setStatus("current")


class _JnxNatTrapSrcPoolName_Type(DisplayString):
    """Custom type jnxNatTrapSrcPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxNatTrapSrcPoolName_Type.__name__ = "DisplayString"
_JnxNatTrapSrcPoolName_Object = MibScalar
jnxNatTrapSrcPoolName = _JnxNatTrapSrcPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 2, 2),
    _JnxNatTrapSrcPoolName_Type()
)
jnxNatTrapSrcPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxNatTrapSrcPoolName.setStatus("current")

# Managed Objects groups


# Notification objects

jnxNatAddrPoolThresholdStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 59, 1, 0, 1)
)
jnxNatAddrPoolThresholdStatus.setObjects(
      *(("JUNIPER-NAT-MIB", "jnxNatTrapSrcPoolName"),
        ("JUNIPER-NAT-MIB", "jnxNatAddrPoolUtil"))
)
if mibBuilder.loadTexts:
    jnxNatAddrPoolThresholdStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-NAT-MIB",
    **{"jnxNatMIB": jnxNatMIB,
       "jnxNatNotifications": jnxNatNotifications,
       "jnxNatAddrPoolThresholdStatus": jnxNatAddrPoolThresholdStatus,
       "jnxNatObjects": jnxNatObjects,
       "jnxSrcNatStatsTable": jnxSrcNatStatsTable,
       "jnxSrcNatStatsEntry": jnxSrcNatStatsEntry,
       "jnxNatSrcPoolName": jnxNatSrcPoolName,
       "jnxNatSrcXlatedAddrType": jnxNatSrcXlatedAddrType,
       "jnxNatSrcPoolType": jnxNatSrcPoolType,
       "jnxNatSrcNumPortAvail": jnxNatSrcNumPortAvail,
       "jnxNatSrcNumPortInuse": jnxNatSrcNumPortInuse,
       "jnxNatSrcNumAddressAvail": jnxNatSrcNumAddressAvail,
       "jnxNatSrcNumAddressInUse": jnxNatSrcNumAddressInUse,
       "jnxNatSrcNumSessions": jnxNatSrcNumSessions,
       "jnxNatSrcNumAddressMapped": jnxNatSrcNumAddressMapped,
       "jnxNatRuleTable": jnxNatRuleTable,
       "jnxNatRuleEntry": jnxNatRuleEntry,
       "jnxNatRuleName": jnxNatRuleName,
       "jnxNatRuleType": jnxNatRuleType,
       "jnxNatRuleTransHits": jnxNatRuleTransHits,
       "jnxNatPoolTable": jnxNatPoolTable,
       "jnxNatPoolEntry": jnxNatPoolEntry,
       "jnxNatPoolName": jnxNatPoolName,
       "jnxNatPoolType": jnxNatPoolType,
       "jnxNatPoolTransHits": jnxNatPoolTransHits,
       "jnxNatPbaStatsTable": jnxNatPbaStatsTable,
       "jnxNatPbaStatsEntry": jnxNatPbaStatsEntry,
       "jnxNatPbaPoolName": jnxNatPbaPoolName,
       "jnxNatPbaOutOfPortError": jnxNatPbaOutOfPortError,
       "jnxNatPbaMaxNumberOfPortBlocksUsed": jnxNatPbaMaxNumberOfPortBlocksUsed,
       "jnxNatPbaCurrentNumberOfPortBlocksInUse": jnxNatPbaCurrentNumberOfPortBlocksInUse,
       "jnxNatPbaPortBlockAllocErrors": jnxNatPbaPortBlockAllocErrors,
       "jnxNatPbaPortBlockMemAllocErrors": jnxNatPbaPortBlockMemAllocErrors,
       "jnxNatPbaPortBlockLimitExeededErrors": jnxNatPbaPortBlockLimitExeededErrors,
       "jnxNatTrapVars": jnxNatTrapVars,
       "jnxNatAddrPoolUtil": jnxNatAddrPoolUtil,
       "jnxNatTrapSrcPoolName": jnxNatTrapSrcPoolName}
)
