# SNMP MIB module (HH3C-LLDP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/h3c_25506/HH3C-LLDP-EXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 18:38:38 2025
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(LldpPortNumber,) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpPortNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3clldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100)
)
if mibBuilder.loadTexts:
    hh3clldp.setRevisions(
        ("2009-03-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3clldpObjects_ObjectIdentity = ObjectIdentity
hh3clldpObjects = _Hh3clldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1)
)
_Hh3clldpConfiguration_ObjectIdentity = ObjectIdentity
hh3clldpConfiguration = _Hh3clldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1)
)
_Hh3clldpAdminStatus_Type = TruthValue
_Hh3clldpAdminStatus_Object = MibScalar
hh3clldpAdminStatus = _Hh3clldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 1),
    _Hh3clldpAdminStatus_Type()
)
hh3clldpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpAdminStatus.setStatus("current")
_Hh3clldpComplianceCDPStatus_Type = TruthValue
_Hh3clldpComplianceCDPStatus_Object = MibScalar
hh3clldpComplianceCDPStatus = _Hh3clldpComplianceCDPStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 2),
    _Hh3clldpComplianceCDPStatus_Type()
)
hh3clldpComplianceCDPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpComplianceCDPStatus.setStatus("current")
_Hh3clldpPortConfigTable_Object = MibTable
hh3clldpPortConfigTable = _Hh3clldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3clldpPortConfigTable.setStatus("current")
_Hh3clldpPortConfigEntry_Object = MibTableRow
hh3clldpPortConfigEntry = _Hh3clldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 3, 1)
)
hh3clldpPortConfigEntry.setIndexNames(
    (0, "HH3C-LLDP-EXT-MIB", "hh3clldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    hh3clldpPortConfigEntry.setStatus("current")
_Hh3clldpPortConfigPortNum_Type = LldpPortNumber
_Hh3clldpPortConfigPortNum_Object = MibTableColumn
hh3clldpPortConfigPortNum = _Hh3clldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 3, 1, 1),
    _Hh3clldpPortConfigPortNum_Type()
)
hh3clldpPortConfigPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3clldpPortConfigPortNum.setStatus("current")


class _Hh3clldpPortConfigCDPComplianceStatus_Type(Integer32):
    """Custom type hh3clldpPortConfigCDPComplianceStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("txAndRx", 1),
          ("disabled", 2))
    )


_Hh3clldpPortConfigCDPComplianceStatus_Type.__name__ = "Integer32"
_Hh3clldpPortConfigCDPComplianceStatus_Object = MibTableColumn
hh3clldpPortConfigCDPComplianceStatus = _Hh3clldpPortConfigCDPComplianceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 100, 1, 1, 3, 1, 2),
    _Hh3clldpPortConfigCDPComplianceStatus_Type()
)
hh3clldpPortConfigCDPComplianceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3clldpPortConfigCDPComplianceStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LLDP-EXT-MIB",
    **{"hh3clldp": hh3clldp,
       "hh3clldpObjects": hh3clldpObjects,
       "hh3clldpConfiguration": hh3clldpConfiguration,
       "hh3clldpAdminStatus": hh3clldpAdminStatus,
       "hh3clldpComplianceCDPStatus": hh3clldpComplianceCDPStatus,
       "hh3clldpPortConfigTable": hh3clldpPortConfigTable,
       "hh3clldpPortConfigEntry": hh3clldpPortConfigEntry,
       "hh3clldpPortConfigPortNum": hh3clldpPortConfigPortNum,
       "hh3clldpPortConfigCDPComplianceStatus": hh3clldpPortConfigCDPComplianceStatus}
)
