# SNMP MIB module (SCTE-HMS-HEADENDIDENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-HEADENDIDENT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:32:18 2025
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

(insidePlantIdent,) = mibBuilder.importSymbols(
    "SCTE-HMS-ROOTS",
    "insidePlantIdent")

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

headEndIdentMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 0)
)
if mibBuilder.loadTexts:
    headEndIdentMib.setRevisions(
        ("2008-01-16 13:00",
         "2007-10-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class HeTenthVolt(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HeTenthdBm(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HeTenthdBmV(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HeTenthCentigrade(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HeHundredthNanoMeter(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"


class HeTenthdB(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


class HeOnOffControl(TextualConvention, Integer32):
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
        *(("off", 1),
          ("on", 2),
          ("meaningless", 3))
    )



class HeOnOffStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )



class HeFaultStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("fault", 2))
    )



class HeLaserType(DisplayString):
    status = "current"


class HeMilliAmp(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-3"


class HeHundredthWatts(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs

_HeOptics_ObjectIdentity = ObjectIdentity
heOptics = _HeOptics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 1)
)
if mibBuilder.loadTexts:
    heOptics.setStatus("current")
_HeBaseIdent_ObjectIdentity = ObjectIdentity
heBaseIdent = _HeBaseIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2)
)
if mibBuilder.loadTexts:
    heBaseIdent.setStatus("current")
_HeCommon_ObjectIdentity = ObjectIdentity
heCommon = _HeCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    heCommon.setStatus("current")
_HePowerSupply_ObjectIdentity = ObjectIdentity
hePowerSupply = _HePowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 2)
)
if mibBuilder.loadTexts:
    hePowerSupply.setStatus("current")
_HeFans_ObjectIdentity = ObjectIdentity
heFans = _HeFans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 2, 3)
)
if mibBuilder.loadTexts:
    heFans.setStatus("current")
_HeHMTS_ObjectIdentity = ObjectIdentity
heHMTS = _HeHMTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 3)
)
if mibBuilder.loadTexts:
    heHMTS.setStatus("current")
_HeRF_ObjectIdentity = ObjectIdentity
heRF = _HeRF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 4)
)
if mibBuilder.loadTexts:
    heRF.setStatus("current")
_HeDigital_ObjectIdentity = ObjectIdentity
heDigital = _HeDigital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5)
)
if mibBuilder.loadTexts:
    heDigital.setStatus("current")
_HeManagedServer_ObjectIdentity = ObjectIdentity
heManagedServer = _HeManagedServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 6)
)
if mibBuilder.loadTexts:
    heManagedServer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-HEADENDIDENT-MIB",
    **{"HeTenthVolt": HeTenthVolt,
       "HeTenthdBm": HeTenthdBm,
       "HeTenthdBmV": HeTenthdBmV,
       "HeTenthCentigrade": HeTenthCentigrade,
       "HeHundredthNanoMeter": HeHundredthNanoMeter,
       "HeTenthdB": HeTenthdB,
       "HeOnOffControl": HeOnOffControl,
       "HeOnOffStatus": HeOnOffStatus,
       "HeFaultStatus": HeFaultStatus,
       "HeLaserType": HeLaserType,
       "HeMilliAmp": HeMilliAmp,
       "HeHundredthWatts": HeHundredthWatts,
       "headEndIdentMib": headEndIdentMib,
       "heOptics": heOptics,
       "heBaseIdent": heBaseIdent,
       "heCommon": heCommon,
       "hePowerSupply": hePowerSupply,
       "heFans": heFans,
       "heHMTS": heHMTS,
       "heRF": heRF,
       "heDigital": heDigital,
       "heManagedServer": heManagedServer}
)
