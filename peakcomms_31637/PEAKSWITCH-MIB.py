# SNMP MIB module (PEAKSWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKSWITCH-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(converters,) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "converters")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

peakSwitchModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 13)
)
if mibBuilder.loadTexts:
    peakSwitchModule.setRevisions(
        ("2015-09-15 10:00",
         "2014-07-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwitchInput_Type = OctetString
_SwitchInput_Object = MibScalar
switchInput = _SwitchInput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 13, 1),
    _SwitchInput_Type()
)
switchInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchInput.setStatus("current")
_SwitchWantedInput_Type = OctetString
_SwitchWantedInput_Object = MibScalar
switchWantedInput = _SwitchWantedInput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 13, 2),
    _SwitchWantedInput_Type()
)
switchWantedInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchWantedInput.setStatus("current")
_SwitchConvGroups_ObjectIdentity = ObjectIdentity
switchConvGroups = _SwitchConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 13, 110)
)
_SwitchConvConformance_ObjectIdentity = ObjectIdentity
switchConvConformance = _SwitchConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 13, 111)
)

# Managed Objects groups

switchCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 13, 110, 1)
)
switchCNFReqGrp.setObjects(
      *(("PEAKSWITCH-MIB", "switchInput"),
        ("PEAKSWITCH-MIB", "switchWantedInput"))
)
if mibBuilder.loadTexts:
    switchCNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

switchCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 13, 111, 1)
)
switchCNFCompliance.setObjects(
    ("PEAKSWITCH-MIB", "switchCNFReqGrp")
)
if mibBuilder.loadTexts:
    switchCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKSWITCH-MIB",
    **{"peakSwitchModule": peakSwitchModule,
       "switchInput": switchInput,
       "switchWantedInput": switchWantedInput,
       "switchConvGroups": switchConvGroups,
       "switchCNFReqGrp": switchCNFReqGrp,
       "switchConvConformance": switchConvConformance,
       "switchCNFCompliance": switchCNFCompliance}
)
