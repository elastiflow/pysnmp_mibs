# SNMP MIB module (ACMEPACKET-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/acmepacket_9148/ACMEPACKET-SMI.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:10:25 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

acmepacket = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148)
)
if mibBuilder.loadTexts:
    acmepacket.setRevisions(
        ("2012-02-02 18:00",
         "2004-02-26 18:00",
         "2001-09-05 00:00",
         "2014-06-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcmepacketProducts_ObjectIdentity = ObjectIdentity
acmepacketProducts = _AcmepacketProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 1)
)
if mibBuilder.loadTexts:
    acmepacketProducts.setStatus("current")
_AcmepacketAgentCapability_ObjectIdentity = ObjectIdentity
acmepacketAgentCapability = _AcmepacketAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2)
)
if mibBuilder.loadTexts:
    acmepacketAgentCapability.setStatus("current")
_AcmepacketMgmt_ObjectIdentity = ObjectIdentity
acmepacketMgmt = _AcmepacketMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3)
)
if mibBuilder.loadTexts:
    acmepacketMgmt.setStatus("current")
_AcmepacketConfig_ObjectIdentity = ObjectIdentity
acmepacketConfig = _AcmepacketConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 4)
)
if mibBuilder.loadTexts:
    acmepacketConfig.setStatus("current")
_AcmepacketExperiment_ObjectIdentity = ObjectIdentity
acmepacketExperiment = _AcmepacketExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 5)
)
if mibBuilder.loadTexts:
    acmepacketExperiment.setStatus("current")
_AcmepacketModules_ObjectIdentity = ObjectIdentity
acmepacketModules = _AcmepacketModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 6)
)
if mibBuilder.loadTexts:
    acmepacketModules.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACMEPACKET-SMI",
    **{"acmepacket": acmepacket,
       "acmepacketProducts": acmepacketProducts,
       "acmepacketAgentCapability": acmepacketAgentCapability,
       "acmepacketMgmt": acmepacketMgmt,
       "acmepacketConfig": acmepacketConfig,
       "acmepacketExperiment": acmepacketExperiment,
       "acmepacketModules": acmepacketModules}
)
