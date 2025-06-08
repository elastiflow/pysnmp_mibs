# SNMP MIB module (BELAIR-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ericsson_15768/BELAIR-TC.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 16:08:43 2025
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

(belairModules,) = mibBuilder.importSymbols(
    "BELAIR-SMI",
    "belairModules")

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

belairTcModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15768, 1, 2)
)
if mibBuilder.loadTexts:
    belairTcModule.setRevisions(
        ("2008-11-26 15:00",
         "2008-10-02 13:05",
         "2008-08-30 17:15",
         "2006-01-12 13:40",
         "2005-11-25 10:00",
         "2005-09-12 11:00",
         "2005-03-07 15:15",
         "2004-11-01 14:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BelAirSoftwareBank(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )



class BelAirRowStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )



class BelAirAlarmId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              12,
              15,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              46,
              49,
              50,
              51,
              52,
              53,
              56,
              57,
              58,
              59,
              61,
              62,
              63,
              65,
              66,
              67,
              82,
              83,
              84,
              85,
              86,
              88,
              89,
              90,
              91,
              92,
              93,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("tempTooHigh", 1),
          ("tempTooLow", 2),
          ("tempReadFailure", 3),
          ("cardFailure", 4),
          ("sntpServerDown", 6),
          ("swDownloadInProgress", 7),
          ("swDownloadFailure", 8),
          ("txPowerSetToHigh", 9),
          ("txPowerSetToLow", 10),
          ("mgmtSwRestarted", 12),
          ("linkDown", 15),
          ("batteryInUse", 20),
          ("batteryMissing", 21),
          ("batteryLowVWarning", 22),
          ("batteryActiveLowVWarning", 23),
          ("batteryLowVFailure", 24),
          ("batteryActiveLowVFailure", 25),
          ("radarDetected", 26),
          ("meshLinkStatusChange", 46),
          ("manualReset", 49),
          ("adminDown", 50),
          ("communicationFailure", 51),
          ("linkDownStarTopo", 52),
          ("linkDownP2pTopo", 53),
          ("radarBlackoutEnded", 56),
          ("wrmLinkDown", 57),
          ("wrmLinkDownRemote", 58),
          ("cmLinkDown", 59),
          ("tunnelDown", 61),
          ("tunnelMainActive", 62),
          ("tunnelSecondaryActive", 63),
          ("authenticationFailure", 65),
          ("cemVcPeerNotResponding", 66),
          ("cemVcPktRemoteTrunkRai", 67),
          ("pllLockDetectFailure", 82),
          ("transmitPowerFailure", 83),
          ("noPrimaryLinkAvailable", 84),
          ("noSecondaryLinkAvailable", 85),
          ("primarySecondarySwitchover", 86),
          ("ipAddressChange", 88),
          ("configChange", 89),
          ("cmIpAddressChange", 90),
          ("secureMacSpoofing", 91),
          ("dhcpAttack", 92),
          ("wifiClientAuthenticated", 93),
          ("userLoginFailure", 98),
          ("rstpTopologyChange", 99),
          ("configChangeUnsaved", 100))
    )



class BelAirSeverity(TextualConvention, Integer32):
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
        *(("cleared", 1),
          ("indeterminate", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6),
          ("informational", 7))
    )



class BelAirAlarmObjectIndex(TextualConvention, Integer32):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("scalar", 1),
          ("ifIndex", 2),
          ("belairCardTypeAndCardIndex", 3))
    )



class BelAirVlanIdOrZero(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )



class BelAirSsidIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )



class BelAirAuthenType(TextualConvention, Integer32):
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
        *(("openSystem", 1),
          ("sharedKey", 2),
          ("ieee802dot1x", 3))
    )



class BelAirEncryptionKey(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 63),
    )



class BelAirEncryptionType(TextualConvention, Integer32):
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
          ("wep", 2),
          ("tkip", 3),
          ("aes", 4))
    )



class BelAirAdminState(TextualConvention, Integer32):
    status = "current"
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



class BelAirCardType(TextualConvention, Integer32):
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
        *(("arm", 1),
          ("brm", 2),
          ("scm", 3),
          ("lim", 4),
          ("cem", 5))
    )



class BelAirChannelList(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BELAIR-TC",
    **{"BelAirSoftwareBank": BelAirSoftwareBank,
       "BelAirRowStatus": BelAirRowStatus,
       "BelAirAlarmId": BelAirAlarmId,
       "BelAirSeverity": BelAirSeverity,
       "BelAirAlarmObjectIndex": BelAirAlarmObjectIndex,
       "BelAirVlanIdOrZero": BelAirVlanIdOrZero,
       "BelAirSsidIndex": BelAirSsidIndex,
       "BelAirAuthenType": BelAirAuthenType,
       "BelAirEncryptionKey": BelAirEncryptionKey,
       "BelAirEncryptionType": BelAirEncryptionType,
       "BelAirAdminState": BelAirAdminState,
       "BelAirCardType": BelAirCardType,
       "BelAirChannelList": BelAirChannelList,
       "belairTcModule": belairTcModule}
)
