# SNMP MIB module (AMDI-FFDA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/applied_micro_47182/AMDI-FFDA-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:25:51 2025
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

amdiFFDARegMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47182)
)
if mibBuilder.loadTexts:
    amdiFFDARegMIB.setRevisions(
        ("2016-04-12 13:42",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AmdiFFDAObjects_ObjectIdentity = ObjectIdentity
amdiFFDAObjects = _AmdiFFDAObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47182, 1)
)
_AmdiFFDAAgentModules_ObjectIdentity = ObjectIdentity
amdiFFDAAgentModules = _AmdiFFDAAgentModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47182, 1, 1)
)
_AmdiFFDAfwdpwr_Type = OctetString
_AmdiFFDAfwdpwr_Object = MibScalar
amdiFFDAfwdpwr = _AmdiFFDAfwdpwr_Object(
    (1, 3, 6, 1, 4, 1, 47182, 1, 1, 1),
    _AmdiFFDAfwdpwr_Type()
)
amdiFFDAfwdpwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amdiFFDAfwdpwr.setStatus("current")
if mibBuilder.loadTexts:
    amdiFFDAfwdpwr.setUnits("dB")
_AmdiFFDArevpwer_Type = OctetString
_AmdiFFDArevpwer_Object = MibScalar
amdiFFDArevpwer = _AmdiFFDArevpwer_Object(
    (1, 3, 6, 1, 4, 1, 47182, 1, 1, 2),
    _AmdiFFDArevpwer_Type()
)
amdiFFDArevpwer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amdiFFDArevpwer.setStatus("current")
if mibBuilder.loadTexts:
    amdiFFDArevpwer.setUnits("dB")
_AmdiFFDAcurrent_Type = OctetString
_AmdiFFDAcurrent_Object = MibScalar
amdiFFDAcurrent = _AmdiFFDAcurrent_Object(
    (1, 3, 6, 1, 4, 1, 47182, 1, 1, 3),
    _AmdiFFDAcurrent_Type()
)
amdiFFDAcurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amdiFFDAcurrent.setStatus("current")
if mibBuilder.loadTexts:
    amdiFFDAcurrent.setUnits("A")


class _AmdiFFDAtemperature_Type(Integer32):
    """Custom type amdiFFDAtemperature based on Integer32"""
    defaultValue = 0


_AmdiFFDAtemperature_Type.__name__ = "Integer32"
_AmdiFFDAtemperature_Object = MibScalar
amdiFFDAtemperature = _AmdiFFDAtemperature_Object(
    (1, 3, 6, 1, 4, 1, 47182, 1, 1, 4),
    _AmdiFFDAtemperature_Type()
)
amdiFFDAtemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amdiFFDAtemperature.setStatus("current")
if mibBuilder.loadTexts:
    amdiFFDAtemperature.setUnits("C")
_AmdiFFDAEvents_ObjectIdentity = ObjectIdentity
amdiFFDAEvents = _AmdiFFDAEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47182, 2)
)
_AmdiFFDAConf_ObjectIdentity = ObjectIdentity
amdiFFDAConf = _AmdiFFDAConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47182, 3)
)
_AmdiFFDAGroups_ObjectIdentity = ObjectIdentity
amdiFFDAGroups = _AmdiFFDAGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47182, 3, 1)
)
_AmdiFFDACompliances_ObjectIdentity = ObjectIdentity
amdiFFDACompliances = _AmdiFFDACompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47182, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AMDI-FFDA-MIB",
    **{"amdiFFDARegMIB": amdiFFDARegMIB,
       "amdiFFDAObjects": amdiFFDAObjects,
       "amdiFFDAAgentModules": amdiFFDAAgentModules,
       "amdiFFDAfwdpwr": amdiFFDAfwdpwr,
       "amdiFFDArevpwer": amdiFFDArevpwer,
       "amdiFFDAcurrent": amdiFFDAcurrent,
       "amdiFFDAtemperature": amdiFFDAtemperature,
       "amdiFFDAEvents": amdiFFDAEvents,
       "amdiFFDAConf": amdiFFDAConf,
       "amdiFFDAGroups": amdiFFDAGroups,
       "amdiFFDACompliances": amdiFFDACompliances}
)
