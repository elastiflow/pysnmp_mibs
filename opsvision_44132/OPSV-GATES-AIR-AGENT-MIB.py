# SNMP MIB module (OPSV-GATES-AIR-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/opsvision_44132/OPSV-GATES-AIR-AGENT-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:48:35 2025
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

(opsv,) = mibBuilder.importSymbols(
    "OPSV-BASE-MIB",
    "opsv")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "DisplayString",
    "TextualConvention")

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
 Opaque,
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
    "Opaque",
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

opsvGAAgent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 44132, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OpsvGAAgentScalars_ObjectIdentity = ObjectIdentity
opsvGAAgentScalars = _OpsvGAAgentScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44132, 5, 1)
)


class _OpsvGAPrevState_Type(Integer32):
    """Custom type opsvGAPrevState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_OpsvGAPrevState_Type.__name__ = "Integer32"
_OpsvGAPrevState_Object = MibScalar
opsvGAPrevState = _OpsvGAPrevState_Object(
    (1, 3, 6, 1, 4, 1, 44132, 5, 1, 1),
    _OpsvGAPrevState_Type()
)
opsvGAPrevState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    opsvGAPrevState.setStatus("current")


class _OpsvGANewState_Type(Integer32):
    """Custom type opsvGANewState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_OpsvGANewState_Type.__name__ = "Integer32"
_OpsvGANewState_Object = MibScalar
opsvGANewState = _OpsvGANewState_Object(
    (1, 3, 6, 1, 4, 1, 44132, 5, 1, 2),
    _OpsvGANewState_Type()
)
opsvGANewState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    opsvGANewState.setStatus("current")
_OpsvGAAgentTables_ObjectIdentity = ObjectIdentity
opsvGAAgentTables = _OpsvGAAgentTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44132, 5, 2)
)
_OpsvGAAgentNotifications_ObjectIdentity = ObjectIdentity
opsvGAAgentNotifications = _OpsvGAAgentNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44132, 5, 3)
)
_OpsvGAAgentNotificationsPrefix_ObjectIdentity = ObjectIdentity
opsvGAAgentNotificationsPrefix = _OpsvGAAgentNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 44132, 5, 3, 0)
)

# Managed Objects groups


# Notification objects

opsvGatesAirStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 44132, 5, 3, 0, 1)
)
opsvGatesAirStateChangeNotification.setObjects(
      *(("OPSV-GATES-AIR-AGENT-MIB", "opsvGAPrevState"),
        ("OPSV-GATES-AIR-AGENT-MIB", "opsvGANewState"))
)
if mibBuilder.loadTexts:
    opsvGatesAirStateChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPSV-GATES-AIR-AGENT-MIB",
    **{"opsvGAAgent": opsvGAAgent,
       "opsvGAAgentScalars": opsvGAAgentScalars,
       "opsvGAPrevState": opsvGAPrevState,
       "opsvGANewState": opsvGANewState,
       "opsvGAAgentTables": opsvGAAgentTables,
       "opsvGAAgentNotifications": opsvGAAgentNotifications,
       "opsvGAAgentNotificationsPrefix": opsvGAAgentNotificationsPrefix,
       "opsvGatesAirStateChangeNotification": opsvGatesAirStateChangeNotification}
)
