# SNMP MIB module (IANAPowerStateSet-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/IANAPowerStateSet-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 14:35:46 2025
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ianaPowerStateSet = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 228)
)
if mibBuilder.loadTexts:
    ianaPowerStateSet.setRevisions(
        ("2015-02-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PowerStateSet(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255,
              256,
              257,
              258,
              259,
              512,
              513,
              514,
              515,
              516,
              517,
              518,
              519,
              520,
              521,
              522,
              523,
              524,
              525,
              526,
              527,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1033,
              1034,
              1035,
              1036)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("unknown", 255),
          ("ieee1621", 256),
          ("ieee1621Off", 257),
          ("ieee1621Sleep", 258),
          ("ieee1621On", 259),
          ("dmtf", 512),
          ("dmtfOn", 513),
          ("dmtfSleepLight", 514),
          ("dmtfSleepDeep", 515),
          ("dmtfOffHard", 516),
          ("dmtfOffSoft", 517),
          ("dmtfHibernate", 518),
          ("dmtfPowerOffSoft", 519),
          ("dmtfPowerOffHard", 520),
          ("dmtfMasterBusReset", 521),
          ("dmtfDiagnosticInterrapt", 522),
          ("dmtfOffSoftGraceful", 523),
          ("dmtfOffHardGraceful", 524),
          ("dmtfMasterBusResetGraceful", 525),
          ("dmtfPowerCycleOffSoftGraceful", 526),
          ("dmtfPowerCycleHardGraceful", 527),
          ("eman", 1024),
          ("emanMechOff", 1025),
          ("emanSoftOff", 1026),
          ("emanHibernate", 1027),
          ("emanSleep", 1028),
          ("emanStandby", 1029),
          ("emanReady", 1030),
          ("emanLowMinus", 1031),
          ("emanLow", 1032),
          ("emanMediumMinus", 1033),
          ("emanMedium", 1034),
          ("emanHighMinus", 1035),
          ("emanHigh", 1036))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IANAPowerStateSet-MIB",
    **{"PowerStateSet": PowerStateSet,
       "ianaPowerStateSet": ianaPowerStateSet}
)
