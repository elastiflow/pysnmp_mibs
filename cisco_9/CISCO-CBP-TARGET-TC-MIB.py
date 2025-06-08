# SNMP MIB module (CISCO-CBP-TARGET-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-CBP-TARGET-TC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:49:42 2025
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

ciscoCbpTargetTCMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 511)
)
if mibBuilder.loadTexts:
    ciscoCbpTargetTCMIB.setRevisions(
        ("2006-03-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CcbptTargetType(TextualConvention, Integer32):
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
        *(("genIf", 1),
          ("atmPvc", 2),
          ("frDlci", 3),
          ("entity", 4),
          ("fwZone", 5),
          ("fwZonePair", 6),
          ("aaaSession", 7))
    )



class CcbptTargetDirection(TextualConvention, Integer32):
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
        *(("undirected", 1),
          ("input", 2),
          ("output", 3),
          ("inOut", 4))
    )



class CcbptTargetId(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CcbptTargetIdIf(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4



class CcbptTargetIdAtmPvc(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d:2d:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixedLength = 8



class CcbptTargetIdFrDlci(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d:2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixedLength = 6



class CcbptTargetIdEntity(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4



class CcbptTargetIdNameString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class CcbptTargetIdAaaSession(TextualConvention, OctetString):
    status = "current"
    displayHint = "4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixedLength = 4



class CcbptPolicySourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ciscoCbQos", 1),
          ("ciscoCbpBase", 2))
    )



class CcbptPolicyIdentifier(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )



class CcbptPolicyIdentifierOrZero(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CBP-TARGET-TC-MIB",
    **{"CcbptTargetType": CcbptTargetType,
       "CcbptTargetDirection": CcbptTargetDirection,
       "CcbptTargetId": CcbptTargetId,
       "CcbptTargetIdIf": CcbptTargetIdIf,
       "CcbptTargetIdAtmPvc": CcbptTargetIdAtmPvc,
       "CcbptTargetIdFrDlci": CcbptTargetIdFrDlci,
       "CcbptTargetIdEntity": CcbptTargetIdEntity,
       "CcbptTargetIdNameString": CcbptTargetIdNameString,
       "CcbptTargetIdAaaSession": CcbptTargetIdAaaSession,
       "CcbptPolicySourceType": CcbptPolicySourceType,
       "CcbptPolicyIdentifier": CcbptPolicyIdentifier,
       "CcbptPolicyIdentifierOrZero": CcbptPolicyIdentifierOrZero,
       "ciscoCbpTargetTCMIB": ciscoCbpTargetTCMIB}
)
