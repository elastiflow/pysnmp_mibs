# SNMP MIB module (APAMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/acmepacket_9148/APAMI-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:10:25 2025
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

(acmepacketMgmt,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketMgmt")

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

apAMIModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 6)
)
if mibBuilder.loadTexts:
    apAMIModule.setRevisions(
        ("2012-07-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApAMIMIBObjects_ObjectIdentity = ObjectIdentity
apAMIMIBObjects = _ApAMIMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 6, 1)
)
_ApAMISoapObjects_ObjectIdentity = ObjectIdentity
apAMISoapObjects = _ApAMISoapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1)
)


class _ApAMISoapHttp_Type(Integer32):
    """Custom type apAMISoapHttp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ApAMISoapHttp_Type.__name__ = "Integer32"
_ApAMISoapHttp_Object = MibScalar
apAMISoapHttp = _ApAMISoapHttp_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 1),
    _ApAMISoapHttp_Type()
)
apAMISoapHttp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAMISoapHttp.setStatus("current")
_ApAMISoapHttpPort_Type = Integer32
_ApAMISoapHttpPort_Object = MibScalar
apAMISoapHttpPort = _ApAMISoapHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 2),
    _ApAMISoapHttpPort_Type()
)
apAMISoapHttpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAMISoapHttpPort.setStatus("current")


class _ApAMISoapHttps_Type(Integer32):
    """Custom type apAMISoapHttps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ApAMISoapHttps_Type.__name__ = "Integer32"
_ApAMISoapHttps_Object = MibScalar
apAMISoapHttps = _ApAMISoapHttps_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 3),
    _ApAMISoapHttps_Type()
)
apAMISoapHttps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAMISoapHttps.setStatus("current")
_ApAMISoapHttpsPort_Type = Integer32
_ApAMISoapHttpsPort_Object = MibScalar
apAMISoapHttpsPort = _ApAMISoapHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 9148, 3, 6, 1, 1, 4),
    _ApAMISoapHttpsPort_Type()
)
apAMISoapHttpsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAMISoapHttpsPort.setStatus("current")
_ApAMIModuleConformance_ObjectIdentity = ObjectIdentity
apAMIModuleConformance = _ApAMIModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 6, 2)
)
_ApAMIModuleGroups_ObjectIdentity = ObjectIdentity
apAMIModuleGroups = _ApAMIModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 3, 6, 2, 1)
)

# Managed Objects groups

apAMIMibObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9148, 3, 6, 2, 1, 1)
)
apAMIMibObjectsGroup.setObjects(
      *(("APAMI-MIB", "apAMISoapHttp"),
        ("APAMI-MIB", "apAMISoapHttpPort"),
        ("APAMI-MIB", "apAMISoapHttps"),
        ("APAMI-MIB", "apAMISoapHttpsPort"))
)
if mibBuilder.loadTexts:
    apAMIMibObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APAMI-MIB",
    **{"apAMIModule": apAMIModule,
       "apAMIMIBObjects": apAMIMIBObjects,
       "apAMISoapObjects": apAMISoapObjects,
       "apAMISoapHttp": apAMISoapHttp,
       "apAMISoapHttpPort": apAMISoapHttpPort,
       "apAMISoapHttps": apAMISoapHttps,
       "apAMISoapHttpsPort": apAMISoapHttpsPort,
       "apAMIModuleConformance": apAMIModuleConformance,
       "apAMIModuleGroups": apAMIModuleGroups,
       "apAMIMibObjectsGroup": apAMIMibObjectsGroup}
)
