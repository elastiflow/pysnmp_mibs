# SNMP MIB module (MASTERAGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_2352/MASTERAGENT-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:10:57 2025
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

(agentxSessionDescr,) = mibBuilder.importSymbols(
    "AGENTX-MIB",
    "agentxSessionDescr")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

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

masteragentxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 104)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Masteragent_ObjectIdentity = ObjectIdentity
masteragent = _Masteragent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 104, 1)
)


class _AgentxSessionCloseReason_Type(Unsigned32):
    """Custom type agentxSessionCloseReason based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AgentxSessionCloseReason_Type.__name__ = "Unsigned32"
_AgentxSessionCloseReason_Object = MibScalar
agentxSessionCloseReason = _AgentxSessionCloseReason_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 104, 2),
    _AgentxSessionCloseReason_Type()
)
agentxSessionCloseReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentxSessionCloseReason.setStatus("current")

# Managed Objects groups


# Notification objects

rbnSubAgentLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 104, 1, 2)
)
rbnSubAgentLost.setObjects(
      *(("AGENTX-MIB", "agentxSessionDescr"),
        ("MASTERAGENT-MIB", "agentxSessionCloseReason"))
)
if mibBuilder.loadTexts:
    rbnSubAgentLost.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MASTERAGENT-MIB",
    **{"masteragentxMIB": masteragentxMIB,
       "masteragent": masteragent,
       "rbnSubAgentLost": rbnSubAgentLost,
       "agentxSessionCloseReason": agentxSessionCloseReason}
)
