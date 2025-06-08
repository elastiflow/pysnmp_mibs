# SNMP MIB module (CEM-IPOA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-IPOA-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

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

cemIpoaModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 20)
)
if mibBuilder.loadTexts:
    cemIpoaModule.setRevisions(
        ("2002-04-03 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CemIpoaEncapsType(TextualConvention, Integer32):
    status = "current"
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
        *(("llcSnapRouted", 1),
          ("vcMuxedRouted", 2),
          ("llcSnapBridged", 3),
          ("vcMuxedBridged", 4),
          ("other", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CemIpoaMIB_ObjectIdentity = ObjectIdentity
cemIpoaMIB = _CemIpoaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1)
)
if mibBuilder.loadTexts:
    cemIpoaMIB.setStatus("current")
_CemIpoaTables_ObjectIdentity = ObjectIdentity
cemIpoaTables = _CemIpoaTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1)
)
if mibBuilder.loadTexts:
    cemIpoaTables.setStatus("current")
_CemIpoaIfTable_Object = MibTable
cemIpoaIfTable = _CemIpoaIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cemIpoaIfTable.setStatus("current")
_CemIpoaIfEntry_Object = MibTableRow
cemIpoaIfEntry = _CemIpoaIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 1, 1)
)
cemIpoaIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cemIpoaIfEntry.setStatus("current")
_CemIpoaIfEncapsType_Type = CemIpoaEncapsType
_CemIpoaIfEncapsType_Object = MibTableColumn
cemIpoaIfEncapsType = _CemIpoaIfEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 1, 1, 1),
    _CemIpoaIfEncapsType_Type()
)
cemIpoaIfEncapsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cemIpoaIfEncapsType.setStatus("current")
_CemIpoaIfRowStatus_Type = RowStatus
_CemIpoaIfRowStatus_Object = MibTableColumn
cemIpoaIfRowStatus = _CemIpoaIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 1, 1, 2),
    _CemIpoaIfRowStatus_Type()
)
cemIpoaIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cemIpoaIfRowStatus.setStatus("current")


class _CemIpoaIfCacheEntryAge_Type(Integer32):
    """Custom type cemIpoaIfCacheEntryAge based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1200),
    )


_CemIpoaIfCacheEntryAge_Type.__name__ = "Integer32"
_CemIpoaIfCacheEntryAge_Object = MibTableColumn
cemIpoaIfCacheEntryAge = _CemIpoaIfCacheEntryAge_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 1, 1, 3),
    _CemIpoaIfCacheEntryAge_Type()
)
cemIpoaIfCacheEntryAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cemIpoaIfCacheEntryAge.setStatus("current")
if mibBuilder.loadTexts:
    cemIpoaIfCacheEntryAge.setUnits("seconds")
_CemIpoaBindingsTable_Object = MibTable
cemIpoaBindingsTable = _CemIpoaBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cemIpoaBindingsTable.setStatus("current")
_CemIpoaBindingsEntry_Object = MibTableRow
cemIpoaBindingsEntry = _CemIpoaBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 2, 1)
)
cemIpoaBindingsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CEM-IPOA-MIB", "cemIpoaBindingsAtmIfIndex"),
    (0, "CEM-IPOA-MIB", "cemIpoaBindingsVclVpi"),
    (0, "CEM-IPOA-MIB", "cemIpoaBindingsVclVci"),
)
if mibBuilder.loadTexts:
    cemIpoaBindingsEntry.setStatus("current")


class _CemIpoaBindingsAtmIfIndex_Type(Integer32):
    """Custom type cemIpoaBindingsAtmIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CemIpoaBindingsAtmIfIndex_Type.__name__ = "Integer32"
_CemIpoaBindingsAtmIfIndex_Object = MibTableColumn
cemIpoaBindingsAtmIfIndex = _CemIpoaBindingsAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 2, 1, 1),
    _CemIpoaBindingsAtmIfIndex_Type()
)
cemIpoaBindingsAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cemIpoaBindingsAtmIfIndex.setStatus("current")
_CemIpoaBindingsVclVpi_Type = AtmVpIdentifier
_CemIpoaBindingsVclVpi_Object = MibTableColumn
cemIpoaBindingsVclVpi = _CemIpoaBindingsVclVpi_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 2, 1, 2),
    _CemIpoaBindingsVclVpi_Type()
)
cemIpoaBindingsVclVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cemIpoaBindingsVclVpi.setStatus("current")
_CemIpoaBindingsVclVci_Type = AtmVcIdentifier
_CemIpoaBindingsVclVci_Object = MibTableColumn
cemIpoaBindingsVclVci = _CemIpoaBindingsVclVci_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 2, 1, 3),
    _CemIpoaBindingsVclVci_Type()
)
cemIpoaBindingsVclVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cemIpoaBindingsVclVci.setStatus("current")
_CemIpoaBindingsRowStatus_Type = RowStatus
_CemIpoaBindingsRowStatus_Object = MibTableColumn
cemIpoaBindingsRowStatus = _CemIpoaBindingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 2, 1, 4),
    _CemIpoaBindingsRowStatus_Type()
)
cemIpoaBindingsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cemIpoaBindingsRowStatus.setStatus("current")
_CemIpoaBindingsIpAddress_Type = IpAddress
_CemIpoaBindingsIpAddress_Object = MibTableColumn
cemIpoaBindingsIpAddress = _CemIpoaBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 2, 1, 5),
    _CemIpoaBindingsIpAddress_Type()
)
cemIpoaBindingsIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cemIpoaBindingsIpAddress.setStatus("current")
_CemIpoaIfInArpStatsTable_Object = MibTable
cemIpoaIfInArpStatsTable = _CemIpoaIfInArpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cemIpoaIfInArpStatsTable.setStatus("current")
_CemIpoaIfInArpStatsEntry_Object = MibTableRow
cemIpoaIfInArpStatsEntry = _CemIpoaIfInArpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 3, 1)
)
cemIpoaIfInArpStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cemIpoaIfInArpStatsEntry.setStatus("current")
_CemIpoaIfInArpInReqs_Type = Counter32
_CemIpoaIfInArpInReqs_Object = MibTableColumn
cemIpoaIfInArpInReqs = _CemIpoaIfInArpInReqs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 3, 1, 1),
    _CemIpoaIfInArpInReqs_Type()
)
cemIpoaIfInArpInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemIpoaIfInArpInReqs.setStatus("current")
_CemIpoaIfInArpOutReqs_Type = Counter32
_CemIpoaIfInArpOutReqs_Object = MibTableColumn
cemIpoaIfInArpOutReqs = _CemIpoaIfInArpOutReqs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 3, 1, 2),
    _CemIpoaIfInArpOutReqs_Type()
)
cemIpoaIfInArpOutReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemIpoaIfInArpOutReqs.setStatus("current")
_CemIpoaIfInArpInReplies_Type = Counter32
_CemIpoaIfInArpInReplies_Object = MibTableColumn
cemIpoaIfInArpInReplies = _CemIpoaIfInArpInReplies_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 3, 1, 3),
    _CemIpoaIfInArpInReplies_Type()
)
cemIpoaIfInArpInReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemIpoaIfInArpInReplies.setStatus("current")
_CemIpoaIfInArpOutReplies_Type = Counter32
_CemIpoaIfInArpOutReplies_Object = MibTableColumn
cemIpoaIfInArpOutReplies = _CemIpoaIfInArpOutReplies_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 3, 1, 4),
    _CemIpoaIfInArpOutReplies_Type()
)
cemIpoaIfInArpOutReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemIpoaIfInArpOutReplies.setStatus("current")
_CemIpoaIfInArpInvalidInReqs_Type = Counter32
_CemIpoaIfInArpInvalidInReqs_Object = MibTableColumn
cemIpoaIfInArpInvalidInReqs = _CemIpoaIfInArpInvalidInReqs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 3, 1, 5),
    _CemIpoaIfInArpInvalidInReqs_Type()
)
cemIpoaIfInArpInvalidInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemIpoaIfInArpInvalidInReqs.setStatus("current")
_CemIpoaIfInArpInvalidOutReqs_Type = Counter32
_CemIpoaIfInArpInvalidOutReqs_Object = MibTableColumn
cemIpoaIfInArpInvalidOutReqs = _CemIpoaIfInArpInvalidOutReqs_Object(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 1, 3, 1, 6),
    _CemIpoaIfInArpInvalidOutReqs_Type()
)
cemIpoaIfInArpInvalidOutReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cemIpoaIfInArpInvalidOutReqs.setStatus("current")
_CemIpoaGroups_ObjectIdentity = ObjectIdentity
cemIpoaGroups = _CemIpoaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 2)
)
if mibBuilder.loadTexts:
    cemIpoaGroups.setStatus("current")
_CemIpoaConformance_ObjectIdentity = ObjectIdentity
cemIpoaConformance = _CemIpoaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 3)
)
if mibBuilder.loadTexts:
    cemIpoaConformance.setStatus("current")

# Managed Objects groups

cemIpoaIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 2, 1)
)
cemIpoaIfGroup.setObjects(
      *(("CEM-IPOA-MIB", "cemIpoaIfEncapsType"),
        ("CEM-IPOA-MIB", "cemIpoaIfRowStatus"),
        ("CEM-IPOA-MIB", "cemIpoaIfCacheEntryAge"))
)
if mibBuilder.loadTexts:
    cemIpoaIfGroup.setStatus("current")

cemIpoaBindingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 2, 2)
)
cemIpoaBindingsGroup.setObjects(
      *(("CEM-IPOA-MIB", "cemIpoaBindingsRowStatus"),
        ("CEM-IPOA-MIB", "cemIpoaBindingsIpAddress"))
)
if mibBuilder.loadTexts:
    cemIpoaBindingsGroup.setStatus("current")

cemIpoaIfInArpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 2, 3)
)
cemIpoaIfInArpStatsGroup.setObjects(
      *(("CEM-IPOA-MIB", "cemIpoaIfInArpInReqs"),
        ("CEM-IPOA-MIB", "cemIpoaIfInArpOutReqs"),
        ("CEM-IPOA-MIB", "cemIpoaIfInArpInReplies"),
        ("CEM-IPOA-MIB", "cemIpoaIfInArpOutReplies"),
        ("CEM-IPOA-MIB", "cemIpoaIfInArpInvalidInReqs"),
        ("CEM-IPOA-MIB", "cemIpoaIfInArpInvalidOutReqs"))
)
if mibBuilder.loadTexts:
    cemIpoaIfInArpStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cemIpoaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6352, 20, 1, 3, 1)
)
cemIpoaCompliance.setObjects(
      *(("CEM-IPOA-MIB", "cemIpoaIfGroup"),
        ("CEM-IPOA-MIB", "cemIpoaBindingsGroup"),
        ("CEM-IPOA-MIB", "cemIpoaIfInArpStatsGroup"))
)
if mibBuilder.loadTexts:
    cemIpoaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-IPOA-MIB",
    **{"CemIpoaEncapsType": CemIpoaEncapsType,
       "cemIpoaModule": cemIpoaModule,
       "cemIpoaMIB": cemIpoaMIB,
       "cemIpoaTables": cemIpoaTables,
       "cemIpoaIfTable": cemIpoaIfTable,
       "cemIpoaIfEntry": cemIpoaIfEntry,
       "cemIpoaIfEncapsType": cemIpoaIfEncapsType,
       "cemIpoaIfRowStatus": cemIpoaIfRowStatus,
       "cemIpoaIfCacheEntryAge": cemIpoaIfCacheEntryAge,
       "cemIpoaBindingsTable": cemIpoaBindingsTable,
       "cemIpoaBindingsEntry": cemIpoaBindingsEntry,
       "cemIpoaBindingsAtmIfIndex": cemIpoaBindingsAtmIfIndex,
       "cemIpoaBindingsVclVpi": cemIpoaBindingsVclVpi,
       "cemIpoaBindingsVclVci": cemIpoaBindingsVclVci,
       "cemIpoaBindingsRowStatus": cemIpoaBindingsRowStatus,
       "cemIpoaBindingsIpAddress": cemIpoaBindingsIpAddress,
       "cemIpoaIfInArpStatsTable": cemIpoaIfInArpStatsTable,
       "cemIpoaIfInArpStatsEntry": cemIpoaIfInArpStatsEntry,
       "cemIpoaIfInArpInReqs": cemIpoaIfInArpInReqs,
       "cemIpoaIfInArpOutReqs": cemIpoaIfInArpOutReqs,
       "cemIpoaIfInArpInReplies": cemIpoaIfInArpInReplies,
       "cemIpoaIfInArpOutReplies": cemIpoaIfInArpOutReplies,
       "cemIpoaIfInArpInvalidInReqs": cemIpoaIfInArpInvalidInReqs,
       "cemIpoaIfInArpInvalidOutReqs": cemIpoaIfInArpInvalidOutReqs,
       "cemIpoaGroups": cemIpoaGroups,
       "cemIpoaIfGroup": cemIpoaIfGroup,
       "cemIpoaBindingsGroup": cemIpoaBindingsGroup,
       "cemIpoaIfInArpStatsGroup": cemIpoaIfInArpStatsGroup,
       "cemIpoaConformance": cemIpoaConformance,
       "cemIpoaCompliance": cemIpoaCompliance}
)
