# SNMP MIB module (A3COM-HUAWEI-LLDP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/3com_43/A3COM-HUAWEI-LLDP-EXT-MIB.mib
# Produced by pysmi-1.6.1 at Thu Jun  5 23:04:06 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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

h3clldp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100)
)
if mibBuilder.loadTexts:
    h3clldp.setRevisions(
        ("2009-03-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3clldpObjects_ObjectIdentity = ObjectIdentity
h3clldpObjects = _H3clldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1)
)
_H3clldpConfiguration_ObjectIdentity = ObjectIdentity
h3clldpConfiguration = _H3clldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1)
)
_H3clldpAdminStatus_Type = TruthValue
_H3clldpAdminStatus_Object = MibScalar
h3clldpAdminStatus = _H3clldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 1),
    _H3clldpAdminStatus_Type()
)
h3clldpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpAdminStatus.setStatus("current")
_H3clldpComplianceCDPStatus_Type = TruthValue
_H3clldpComplianceCDPStatus_Object = MibScalar
h3clldpComplianceCDPStatus = _H3clldpComplianceCDPStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 2),
    _H3clldpComplianceCDPStatus_Type()
)
h3clldpComplianceCDPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpComplianceCDPStatus.setStatus("current")
_H3clldpPortConfigTable_Object = MibTable
h3clldpPortConfigTable = _H3clldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3clldpPortConfigTable.setStatus("current")
_H3clldpPortConfigEntry_Object = MibTableRow
h3clldpPortConfigEntry = _H3clldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3, 1)
)
h3clldpPortConfigEntry.setIndexNames(
    (0, "A3COM-HUAWEI-LLDP-EXT-MIB", "h3clldpPortConfigPortNum"),
)
if mibBuilder.loadTexts:
    h3clldpPortConfigEntry.setStatus("current")
_H3clldpPortConfigPortNum_Type = LldpPortNumber
_H3clldpPortConfigPortNum_Object = MibTableColumn
h3clldpPortConfigPortNum = _H3clldpPortConfigPortNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3, 1, 1),
    _H3clldpPortConfigPortNum_Type()
)
h3clldpPortConfigPortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3clldpPortConfigPortNum.setStatus("current")


class _H3clldpPortConfigCDPComplianceStatus_Type(Integer32):
    """Custom type h3clldpPortConfigCDPComplianceStatus based on Integer32"""
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


_H3clldpPortConfigCDPComplianceStatus_Type.__name__ = "Integer32"
_H3clldpPortConfigCDPComplianceStatus_Object = MibTableColumn
h3clldpPortConfigCDPComplianceStatus = _H3clldpPortConfigCDPComplianceStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 100, 1, 1, 3, 1, 2),
    _H3clldpPortConfigCDPComplianceStatus_Type()
)
h3clldpPortConfigCDPComplianceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3clldpPortConfigCDPComplianceStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-LLDP-EXT-MIB",
    **{"h3clldp": h3clldp,
       "h3clldpObjects": h3clldpObjects,
       "h3clldpConfiguration": h3clldpConfiguration,
       "h3clldpAdminStatus": h3clldpAdminStatus,
       "h3clldpComplianceCDPStatus": h3clldpComplianceCDPStatus,
       "h3clldpPortConfigTable": h3clldpPortConfigTable,
       "h3clldpPortConfigEntry": h3clldpPortConfigEntry,
       "h3clldpPortConfigPortNum": h3clldpPortConfigPortNum,
       "h3clldpPortConfigCDPComplianceStatus": h3clldpPortConfigCDPComplianceStatus}
)
