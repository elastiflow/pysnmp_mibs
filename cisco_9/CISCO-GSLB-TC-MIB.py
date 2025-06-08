# SNMP MIB module (CISCO-GSLB-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-GSLB-TC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:28:31 2025
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

ciscoGslbTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 583)
)
if mibBuilder.loadTexts:
    ciscoGslbTcMIB.setRevisions(
        ("2007-02-23 00:00",
         "2006-09-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoGslbNodeServices(TextualConvention, Integer32):
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
        *(("primary", 1),
          ("standby", 2),
          ("secondary", 3))
    )



class CiscoGslbPeerStatus(TextualConvention, Integer32):
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
        *(("inactive", 1),
          ("offline", 2),
          ("online", 3))
    )



class CiscoGslbAnswerType(TextualConvention, Integer32):
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
        *(("other", 1),
          ("vip", 2),
          ("ns", 3),
          ("cra", 4))
    )



class CiscoGslbKeepaliveTargetType(TextualConvention, Integer32):
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
        *(("other", 1),
          ("vip", 2),
          ("ns", 3),
          ("cra", 4),
          ("shared", 5))
    )



class CiscoGslbKeepaliveMethod(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("none", 2),
          ("icmp", 3),
          ("tcp", 4),
          ("httphead", 5),
          ("kalap", 6),
          ("ns", 7),
          ("cra", 8),
          ("scriptedKal", 9))
    )



class CiscoGslbKeepaliveConfigState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("suspend", 2))
    )



class CiscoGslbKeepaliveRate(TextualConvention, Integer32):
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
          ("standard", 2),
          ("fast", 3))
    )



class CiscoGslbTerminationMethod(TextualConvention, Integer32):
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
          ("reset", 2),
          ("graceful", 3))
    )



class CiscoGslbKeepaliveStatus(TextualConvention, Integer32):
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
        *(("other", 1),
          ("offline", 2),
          ("online", 3),
          ("suspended", 4),
          ("init", 5))
    )



class CiscoGslbAnswerStatus(TextualConvention, Integer32):
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
        *(("other", 1),
          ("offline", 2),
          ("online", 3),
          ("suspended", 4),
          ("init", 5))
    )



class CiscoGslbAnswerAdminState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("suspended", 1),
          ("active", 2))
    )



class CiscoGslbKalapType(TextualConvention, Integer32):
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
          ("kalapByVip", 2),
          ("kalapByTag", 3))
    )



class CiscoGslbBalanceMethod(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("orderedList", 2),
          ("roundRobin", 3),
          ("weightedRR", 4),
          ("leastLoaded", 5),
          ("hashed", 6),
          ("boomerang", 7))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GSLB-TC-MIB",
    **{"CiscoGslbNodeServices": CiscoGslbNodeServices,
       "CiscoGslbPeerStatus": CiscoGslbPeerStatus,
       "CiscoGslbAnswerType": CiscoGslbAnswerType,
       "CiscoGslbKeepaliveTargetType": CiscoGslbKeepaliveTargetType,
       "CiscoGslbKeepaliveMethod": CiscoGslbKeepaliveMethod,
       "CiscoGslbKeepaliveConfigState": CiscoGslbKeepaliveConfigState,
       "CiscoGslbKeepaliveRate": CiscoGslbKeepaliveRate,
       "CiscoGslbTerminationMethod": CiscoGslbTerminationMethod,
       "CiscoGslbKeepaliveStatus": CiscoGslbKeepaliveStatus,
       "CiscoGslbAnswerStatus": CiscoGslbAnswerStatus,
       "CiscoGslbAnswerAdminState": CiscoGslbAnswerAdminState,
       "CiscoGslbKalapType": CiscoGslbKalapType,
       "CiscoGslbBalanceMethod": CiscoGslbBalanceMethod,
       "ciscoGslbTcMIB": ciscoGslbTcMIB}
)
