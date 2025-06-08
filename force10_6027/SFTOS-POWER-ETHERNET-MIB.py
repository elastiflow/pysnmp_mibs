# SNMP MIB module (SFTOS-POWER-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/force10_6027/SFTOS-POWER-ETHERNET-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:18:01 2025
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

(sFTOS,) = mibBuilder.importSymbols(
    "FORCE10-REF-MIB",
    "sFTOS")

(pethPsePortEntry,) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethPsePortEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sFTOSpowerEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 15)
)
if mibBuilder.loadTexts:
    sFTOSpowerEthernetMIB.setRevisions(
        ("2005-01-17 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentPethObjects_ObjectIdentity = ObjectIdentity
agentPethObjects = _AgentPethObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 15, 1)
)
_AgentPethPsePortTable_Object = MibTable
agentPethPsePortTable = _AgentPethPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    agentPethPsePortTable.setStatus("current")
_AgentPethPsePortEntry_Object = MibTableRow
agentPethPsePortEntry = _AgentPethPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    agentPethPsePortEntry.setStatus("current")


class _AgentPethPowerLimit_Type(Gauge32):
    """Custom type agentPethPowerLimit based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_AgentPethPowerLimit_Type.__name__ = "Gauge32"
_AgentPethPowerLimit_Object = MibTableColumn
agentPethPowerLimit = _AgentPethPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 15, 1, 1, 1, 1),
    _AgentPethPowerLimit_Type()
)
agentPethPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPethPowerLimit.setStatus("current")
if mibBuilder.loadTexts:
    agentPethPowerLimit.setUnits("Watts")
_AgentPethOutputPower_Type = Gauge32
_AgentPethOutputPower_Object = MibTableColumn
agentPethOutputPower = _AgentPethOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 15, 1, 1, 1, 2),
    _AgentPethOutputPower_Type()
)
agentPethOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    agentPethOutputPower.setUnits("Milliwatts")
_AgentPethOutputCurrent_Type = Gauge32
_AgentPethOutputCurrent_Object = MibTableColumn
agentPethOutputCurrent = _AgentPethOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 15, 1, 1, 1, 3),
    _AgentPethOutputCurrent_Type()
)
agentPethOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethOutputCurrent.setStatus("current")
if mibBuilder.loadTexts:
    agentPethOutputCurrent.setUnits("Milliamps")
_AgentPethOutputVolts_Type = Gauge32
_AgentPethOutputVolts_Object = MibTableColumn
agentPethOutputVolts = _AgentPethOutputVolts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 1, 3, 1, 15, 1, 1, 1, 4),
    _AgentPethOutputVolts_Type()
)
agentPethOutputVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPethOutputVolts.setStatus("current")
if mibBuilder.loadTexts:
    agentPethOutputVolts.setUnits("Volts")
pethPsePortEntry.registerAugmentions(
    ("SFTOS-POWER-ETHERNET-MIB",
     "agentPethPsePortEntry")
)
agentPethPsePortEntry.setIndexNames(*pethPsePortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SFTOS-POWER-ETHERNET-MIB",
    **{"sFTOSpowerEthernetMIB": sFTOSpowerEthernetMIB,
       "agentPethObjects": agentPethObjects,
       "agentPethPsePortTable": agentPethPsePortTable,
       "agentPethPsePortEntry": agentPethPsePortEntry,
       "agentPethPowerLimit": agentPethPowerLimit,
       "agentPethOutputPower": agentPethOutputPower,
       "agentPethOutputCurrent": agentPethOutputCurrent,
       "agentPethOutputVolts": agentPethOutputVolts}
)
