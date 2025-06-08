# SNMP MIB module (CISCO-SUBSCRIBER-SESSION-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-SUBSCRIBER-SESSION-TC-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 00:55:05 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoSubscriberSessionTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 785)
)
if mibBuilder.loadTexts:
    ciscoSubscriberSessionTcMIB.setRevisions(
        ("2007-09-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SubSessionType(TextualConvention, Integer32):
    status = "current"
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
        *(("all", 1),
          ("other", 2),
          ("pppSubscriber", 3),
          ("pppoeSubscriber", 4),
          ("l2tpSubscriber", 5),
          ("l2fSubscriber", 6),
          ("ipInterfaceSubscriber", 7),
          ("ipPktSubscriber", 8),
          ("ipDhcpv4Subscriber", 9),
          ("ipRadiusSubscriber", 10),
          ("l2MacSubscriber", 11),
          ("l2Dhcpv4Subscriber", 12),
          ("l2RadiusSubscriber", 13))
    )



class SubSessionTypes(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("pppSubscriber", 0),
          ("pppoeSubscriber", 1),
          ("l2tpSubscriber", 2),
          ("l2fSubscriber", 3),
          ("ipInterfaceSubscriber", 4),
          ("ipPktSubscriber", 5),
          ("ipDhcpv4Subscriber", 6),
          ("ipRadiusSubscriber", 7),
          ("l2MacSubscriber", 8),
          ("l2Dhcpv4Subscriber", 9),
          ("l2RadiusSubscriber", 10))
    )


class SubSessionState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("pending", 2),
          ("up", 3))
    )



class SubSessionRedundancyMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("other", 2),
          ("active", 3),
          ("standby", 4))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SUBSCRIBER-SESSION-TC-MIB",
    **{"SubSessionType": SubSessionType,
       "SubSessionTypes": SubSessionTypes,
       "SubSessionState": SubSessionState,
       "SubSessionRedundancyMode": SubSessionRedundancyMode,
       "ciscoSubscriberSessionTcMIB": ciscoSubscriberSessionTcMIB}
)
