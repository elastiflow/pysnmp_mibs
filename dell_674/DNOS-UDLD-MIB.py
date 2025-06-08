# SNMP MIB module (DNOS-UDLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DNOS-UDLD-MIB.mib
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fastPathUdld = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54)
)
if mibBuilder.loadTexts:
    fastPathUdld.setRevisions(
        ("2008-02-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentUdldMIBObjects_ObjectIdentity = ObjectIdentity
agentUdldMIBObjects = _AgentUdldMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1)
)
_AgentUdldGlobal_ObjectIdentity = ObjectIdentity
agentUdldGlobal = _AgentUdldGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1, 1)
)


class _AgentUdldGlobalMode_Type(Integer32):
    """Custom type agentUdldGlobalMode based on Integer32"""
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


_AgentUdldGlobalMode_Type.__name__ = "Integer32"
_AgentUdldGlobalMode_Object = MibScalar
agentUdldGlobalMode = _AgentUdldGlobalMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1, 1, 1),
    _AgentUdldGlobalMode_Type()
)
agentUdldGlobalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUdldGlobalMode.setStatus("current")


class _AgentUdldMessageInterval_Type(Integer32):
    """Custom type agentUdldMessageInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 90),
    )


_AgentUdldMessageInterval_Type.__name__ = "Integer32"
_AgentUdldMessageInterval_Object = MibScalar
agentUdldMessageInterval = _AgentUdldMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1, 1, 2),
    _AgentUdldMessageInterval_Type()
)
agentUdldMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUdldMessageInterval.setStatus("current")
if mibBuilder.loadTexts:
    agentUdldMessageInterval.setUnits("seconds")


class _AgentUdldTimeoutInterval_Type(Integer32):
    """Custom type agentUdldTimeoutInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_AgentUdldTimeoutInterval_Type.__name__ = "Integer32"
_AgentUdldTimeoutInterval_Object = MibScalar
agentUdldTimeoutInterval = _AgentUdldTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1, 1, 3),
    _AgentUdldTimeoutInterval_Type()
)
agentUdldTimeoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUdldTimeoutInterval.setStatus("current")
if mibBuilder.loadTexts:
    agentUdldTimeoutInterval.setUnits("seconds")


class _AgentUdldReset_Type(Integer32):
    """Custom type agentUdldReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normalOperation", 0),
          ("reset", 1))
    )


_AgentUdldReset_Type.__name__ = "Integer32"
_AgentUdldReset_Object = MibScalar
agentUdldReset = _AgentUdldReset_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1, 1, 4),
    _AgentUdldReset_Type()
)
agentUdldReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUdldReset.setStatus("current")
_AgentUdldInterface_ObjectIdentity = ObjectIdentity
agentUdldInterface = _AgentUdldInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1, 2)
)
_AgentUdldInterfaceTable_Object = MibTable
agentUdldInterfaceTable = _AgentUdldInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1, 2, 1)
)
if mibBuilder.loadTexts:
    agentUdldInterfaceTable.setStatus("current")
_AgentUdldInterfaceEntry_Object = MibTableRow
agentUdldInterfaceEntry = _AgentUdldInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1, 2, 1, 1)
)
agentUdldInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentUdldInterfaceEntry.setStatus("current")


class _AgentUdldInterfaceOperStatus_Type(Integer32):
    """Custom type agentUdldInterfaceOperStatus based on Integer32"""
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
        *(("shutdown", 1),
          ("undetermined", 2),
          ("biDirectional", 3),
          ("notApplicable", 4),
          ("undetermined-LinkDown", 5))
    )


_AgentUdldInterfaceOperStatus_Type.__name__ = "Integer32"
_AgentUdldInterfaceOperStatus_Object = MibTableColumn
agentUdldInterfaceOperStatus = _AgentUdldInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1, 2, 1, 1, 1),
    _AgentUdldInterfaceOperStatus_Type()
)
agentUdldInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentUdldInterfaceOperStatus.setStatus("current")


class _AgentUdldInterfaceAdminMode_Type(Integer32):
    """Custom type agentUdldInterfaceAdminMode based on Integer32"""
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


_AgentUdldInterfaceAdminMode_Type.__name__ = "Integer32"
_AgentUdldInterfaceAdminMode_Object = MibTableColumn
agentUdldInterfaceAdminMode = _AgentUdldInterfaceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1, 2, 1, 1, 2),
    _AgentUdldInterfaceAdminMode_Type()
)
agentUdldInterfaceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUdldInterfaceAdminMode.setStatus("current")
_AgentUdldInterfaceAggresiveMode_Type = TruthValue
_AgentUdldInterfaceAggresiveMode_Object = MibTableColumn
agentUdldInterfaceAggresiveMode = _AgentUdldInterfaceAggresiveMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 54, 1, 2, 1, 1, 3),
    _AgentUdldInterfaceAggresiveMode_Type()
)
agentUdldInterfaceAggresiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUdldInterfaceAggresiveMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-UDLD-MIB",
    **{"fastPathUdld": fastPathUdld,
       "agentUdldMIBObjects": agentUdldMIBObjects,
       "agentUdldGlobal": agentUdldGlobal,
       "agentUdldGlobalMode": agentUdldGlobalMode,
       "agentUdldMessageInterval": agentUdldMessageInterval,
       "agentUdldTimeoutInterval": agentUdldTimeoutInterval,
       "agentUdldReset": agentUdldReset,
       "agentUdldInterface": agentUdldInterface,
       "agentUdldInterfaceTable": agentUdldInterfaceTable,
       "agentUdldInterfaceEntry": agentUdldInterfaceEntry,
       "agentUdldInterfaceOperStatus": agentUdldInterfaceOperStatus,
       "agentUdldInterfaceAdminMode": agentUdldInterfaceAdminMode,
       "agentUdldInterfaceAggresiveMode": agentUdldInterfaceAggresiveMode}
)
