# SNMP MIB module (DNOS-OUTBOUNDTELNET-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/dell_674/DNOS-OUTBOUNDTELNET-PRIVATE-MIB.mib
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

fastPathOutboundTelnetPrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19)
)
if mibBuilder.loadTexts:
    fastPathOutboundTelnetPrivate.setRevisions(
        ("2011-01-26 00:00",
         "2007-05-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentOutboundTelnetGroup_ObjectIdentity = ObjectIdentity
agentOutboundTelnetGroup = _AgentOutboundTelnetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1)
)


class _AgentOutboundTelnetAdminMode_Type(Integer32):
    """Custom type agentOutboundTelnetAdminMode based on Integer32"""
    defaultValue = 1

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


_AgentOutboundTelnetAdminMode_Type.__name__ = "Integer32"
_AgentOutboundTelnetAdminMode_Object = MibScalar
agentOutboundTelnetAdminMode = _AgentOutboundTelnetAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 1),
    _AgentOutboundTelnetAdminMode_Type()
)
agentOutboundTelnetAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutboundTelnetAdminMode.setStatus("current")


class _AgentOutboundTelnetMaxNoOfSessions_Type(Integer32):
    """Custom type agentOutboundTelnetMaxNoOfSessions based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AgentOutboundTelnetMaxNoOfSessions_Type.__name__ = "Integer32"
_AgentOutboundTelnetMaxNoOfSessions_Object = MibScalar
agentOutboundTelnetMaxNoOfSessions = _AgentOutboundTelnetMaxNoOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 2),
    _AgentOutboundTelnetMaxNoOfSessions_Type()
)
agentOutboundTelnetMaxNoOfSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutboundTelnetMaxNoOfSessions.setStatus("current")


class _AgentOutboundTelnetTimeout_Type(Integer32):
    """Custom type agentOutboundTelnetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentOutboundTelnetTimeout_Type.__name__ = "Integer32"
_AgentOutboundTelnetTimeout_Object = MibScalar
agentOutboundTelnetTimeout = _AgentOutboundTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 3),
    _AgentOutboundTelnetTimeout_Type()
)
agentOutboundTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutboundTelnetTimeout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-OUTBOUNDTELNET-PRIVATE-MIB",
    **{"fastPathOutboundTelnetPrivate": fastPathOutboundTelnetPrivate,
       "agentOutboundTelnetGroup": agentOutboundTelnetGroup,
       "agentOutboundTelnetAdminMode": agentOutboundTelnetAdminMode,
       "agentOutboundTelnetMaxNoOfSessions": agentOutboundTelnetMaxNoOfSessions,
       "agentOutboundTelnetTimeout": agentOutboundTelnetTimeout}
)
