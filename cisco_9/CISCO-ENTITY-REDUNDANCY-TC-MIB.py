# SNMP MIB module (CISCO-ENTITY-REDUNDANCY-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-ENTITY-REDUNDANCY-TC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:13:16 2025
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

ciscoEntityRedunTcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 494)
)
if mibBuilder.loadTexts:
    ciscoEntityRedunTcMIB.setRevisions(
        ("2005-10-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CeRedunType(TextualConvention, Integer32):
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
          ("yCable", 2),
          ("aps", 3),
          ("featureCard", 4),
          ("externalSwitch", 5),
          ("slotPair", 6),
          ("cmts", 7))
    )



class CeRedunScope(TextualConvention, Integer32):
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
          ("local", 2),
          ("remoteChassis", 3),
          ("remoteSystem", 4))
    )



class CeRedunArch(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("oneToOne", 2),
          ("onePlusOne", 3),
          ("oneToN", 4),
          ("mToN", 5),
          ("loadSharing", 6))
    )



class CeRedunSwitchCommand(TextualConvention, Integer32):
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
        *(("noCmdInEffect", 1),
          ("clear", 2),
          ("manualSwitchAway", 3),
          ("forcedSwitchAway", 4),
          ("lockoutProtection", 5))
    )



class CeRedunMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )



class CeRedunMbrStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("protectionLockedOut", 0),
          ("degraded", 1),
          ("failure", 2),
          ("standby", 3),
          ("protectionProvided", 4),
          ("forcedStandby", 5),
          ("manualStandby", 6))
    )


class CeRedunStateCategories(TextualConvention, Integer32):
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("inactive", 3),
          ("failed", 4),
          ("initializing", 5),
          ("negotiation", 6),
          ("activeOther", 7),
          ("activeImageInitialize", 8),
          ("activeConfigInitialize", 9),
          ("activeRunStateInitialize", 10),
          ("activeFromStandbyTransition", 11),
          ("activeReconciliation", 12),
          ("activeWait", 13),
          ("active", 14),
          ("standbyOther", 15),
          ("standbyImageInitialize", 16),
          ("standbyConfigInitialize", 17),
          ("standbyRunStateInitialize", 18),
          ("standbyReconciliation", 19),
          ("standbyWait", 20),
          ("standbyColdFinal", 21),
          ("standbyWarmFinal", 22),
          ("standbyHotFinal", 23),
          ("standbySwitchingToActive", 24))
    )



class CeRedunReasonCategories(TextualConvention, Integer32):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unsupported", 2),
          ("notKnown", 3),
          ("userManual", 4),
          ("userForced", 5),
          ("userLockout", 6),
          ("activeMbrFailed", 7),
          ("activeMbrRemoved", 8),
          ("activeMbrDisabled", 9),
          ("revertiveSwitchover", 10),
          ("remoteRequest", 11))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-REDUNDANCY-TC-MIB",
    **{"CeRedunType": CeRedunType,
       "CeRedunScope": CeRedunScope,
       "CeRedunArch": CeRedunArch,
       "CeRedunSwitchCommand": CeRedunSwitchCommand,
       "CeRedunMode": CeRedunMode,
       "CeRedunMbrStatus": CeRedunMbrStatus,
       "CeRedunStateCategories": CeRedunStateCategories,
       "CeRedunReasonCategories": CeRedunReasonCategories,
       "ciscoEntityRedunTcMIB": ciscoEntityRedunTcMIB}
)
