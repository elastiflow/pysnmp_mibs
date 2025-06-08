# SNMP MIB module (CL-PKTC-EUE-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cablelabs_4491/CL-PKTC-EUE-TC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:37:34 2025
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

(pktcEUEMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcEUEMibs")

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

pktcEUETCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2)
)
if mibBuilder.loadTexts:
    pktcEUETCMIB.setRevisions(
        ("2009-12-14 00:00",
         "2008-07-10 00:00",
         "2007-11-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PktcEUETCID(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1023),
    )



class PktcEUETCIDType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("gruu", 2),
          ("publicIdentity", 3),
          ("privateIdentity", 4),
          ("publicPrivatePair", 5),
          ("username", 6),
          ("macaddress", 7),
          ("packetcableIdentity", 8))
    )



class PktcEUETCAdminStatus(TextualConvention, Integer32):
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
          ("inactive", 2))
    )



class PktcEUETCOperStatus(TextualConvention, Integer32):
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
        *(("active", 1),
          ("inactive", 2),
          ("notPresent", 3),
          ("unknown", 4))
    )



class PktcEUETCStatusInfo(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class PktcEUETCUsrElementIndexType(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class PktcEUETCAppOrgIdentifier(TextualConvention, Unsigned32):
    status = "current"


class PktcEUETCAppIdentifier(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )



class PktcEUETCUsrAppIndexType(TextualConvention, Unsigned32):
    status = "current"


class PktcEUETCCredsType(TextualConvention, Integer32):
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
          ("none", 2),
          ("password", 3),
          ("preSharedKey", 4),
          ("certificate", 5))
    )



class PktcEUETCCreds(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8192),
    )



# MIB Managed Objects in the order of their OIDs

_PktcEUETCNotifications_ObjectIdentity = ObjectIdentity
pktcEUETCNotifications = _PktcEUETCNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 0)
)
_PktcEUETCObjects_ObjectIdentity = ObjectIdentity
pktcEUETCObjects = _PktcEUETCObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1)
)
_PktcEUETCUsageObjs_ObjectIdentity = ObjectIdentity
pktcEUETCUsageObjs = _PktcEUETCUsageObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 1, 1)
)
_PktcEUETCConformance_ObjectIdentity = ObjectIdentity
pktcEUETCConformance = _PktcEUETCConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2)
)
_PktcEUETCCompliances_ObjectIdentity = ObjectIdentity
pktcEUETCCompliances = _PktcEUETCCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 1)
)
_PktcEUETCGroups_ObjectIdentity = ObjectIdentity
pktcEUETCGroups = _PktcEUETCGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 10, 2, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CL-PKTC-EUE-TC-MIB",
    **{"PktcEUETCID": PktcEUETCID,
       "PktcEUETCIDType": PktcEUETCIDType,
       "PktcEUETCAdminStatus": PktcEUETCAdminStatus,
       "PktcEUETCOperStatus": PktcEUETCOperStatus,
       "PktcEUETCStatusInfo": PktcEUETCStatusInfo,
       "PktcEUETCUsrElementIndexType": PktcEUETCUsrElementIndexType,
       "PktcEUETCAppOrgIdentifier": PktcEUETCAppOrgIdentifier,
       "PktcEUETCAppIdentifier": PktcEUETCAppIdentifier,
       "PktcEUETCUsrAppIndexType": PktcEUETCUsrAppIndexType,
       "PktcEUETCCredsType": PktcEUETCCredsType,
       "PktcEUETCCreds": PktcEUETCCreds,
       "pktcEUETCMIB": pktcEUETCMIB,
       "pktcEUETCNotifications": pktcEUETCNotifications,
       "pktcEUETCObjects": pktcEUETCObjects,
       "pktcEUETCUsageObjs": pktcEUETCUsageObjs,
       "pktcEUETCConformance": pktcEUETCConformance,
       "pktcEUETCCompliances": pktcEUETCCompliances,
       "pktcEUETCGroups": pktcEUETCGroups}
)
