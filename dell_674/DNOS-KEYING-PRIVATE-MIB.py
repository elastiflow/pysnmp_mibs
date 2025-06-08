# SNMP MIB module (DNOS-KEYING-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DNOS-KEYING-PRIVATE-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:25:38 2025
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

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
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathKeyingPrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 24)
)
if mibBuilder.loadTexts:
    fastPathKeyingPrivate.setRevisions(
        ("2011-01-26 00:00",
         "2007-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentFeatureKeyingGroup_ObjectIdentity = ObjectIdentity
agentFeatureKeyingGroup = _AgentFeatureKeyingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 24, 1)
)
_AgentFeatureKeyingEnableKey_Type = DisplayString
_AgentFeatureKeyingEnableKey_Object = MibScalar
agentFeatureKeyingEnableKey = _AgentFeatureKeyingEnableKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 24, 1, 1),
    _AgentFeatureKeyingEnableKey_Type()
)
agentFeatureKeyingEnableKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFeatureKeyingEnableKey.setStatus("current")
_AgentFeatureKeyingDisableKey_Type = DisplayString
_AgentFeatureKeyingDisableKey_Object = MibScalar
agentFeatureKeyingDisableKey = _AgentFeatureKeyingDisableKey_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 24, 1, 2),
    _AgentFeatureKeyingDisableKey_Type()
)
agentFeatureKeyingDisableKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFeatureKeyingDisableKey.setStatus("current")
_AgentFeatureKeyingTable_Object = MibTable
agentFeatureKeyingTable = _AgentFeatureKeyingTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 24, 1, 3)
)
if mibBuilder.loadTexts:
    agentFeatureKeyingTable.setStatus("current")
_AgentFeatureKeyingEntry_Object = MibTableRow
agentFeatureKeyingEntry = _AgentFeatureKeyingEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 24, 1, 3, 1)
)
agentFeatureKeyingEntry.setIndexNames(
    (0, "DNOS-KEYING-PRIVATE-MIB", "agentFeatureKeyingIndex"),
)
if mibBuilder.loadTexts:
    agentFeatureKeyingEntry.setStatus("current")
_AgentFeatureKeyingIndex_Type = Unsigned32
_AgentFeatureKeyingIndex_Object = MibTableColumn
agentFeatureKeyingIndex = _AgentFeatureKeyingIndex_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 24, 1, 3, 1, 1),
    _AgentFeatureKeyingIndex_Type()
)
agentFeatureKeyingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentFeatureKeyingIndex.setStatus("current")
_AgentFeatureKeyingName_Type = DisplayString
_AgentFeatureKeyingName_Object = MibTableColumn
agentFeatureKeyingName = _AgentFeatureKeyingName_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 24, 1, 3, 1, 2),
    _AgentFeatureKeyingName_Type()
)
agentFeatureKeyingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFeatureKeyingName.setStatus("current")


class _AgentFeatureKeyingStatus_Type(Integer32):
    """Custom type agentFeatureKeyingStatus based on Integer32"""
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


_AgentFeatureKeyingStatus_Type.__name__ = "Integer32"
_AgentFeatureKeyingStatus_Object = MibTableColumn
agentFeatureKeyingStatus = _AgentFeatureKeyingStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 24, 1, 3, 1, 3),
    _AgentFeatureKeyingStatus_Type()
)
agentFeatureKeyingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFeatureKeyingStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-KEYING-PRIVATE-MIB",
    **{"fastPathKeyingPrivate": fastPathKeyingPrivate,
       "agentFeatureKeyingGroup": agentFeatureKeyingGroup,
       "agentFeatureKeyingEnableKey": agentFeatureKeyingEnableKey,
       "agentFeatureKeyingDisableKey": agentFeatureKeyingDisableKey,
       "agentFeatureKeyingTable": agentFeatureKeyingTable,
       "agentFeatureKeyingEntry": agentFeatureKeyingEntry,
       "agentFeatureKeyingIndex": agentFeatureKeyingIndex,
       "agentFeatureKeyingName": agentFeatureKeyingName,
       "agentFeatureKeyingStatus": agentFeatureKeyingStatus}
)
