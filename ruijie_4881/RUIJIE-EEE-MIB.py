# SNMP MIB module (RUIJIE-EEE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-EEE-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:21 2025
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

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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

ruijieEEEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 119)
)
if mibBuilder.loadTexts:
    ruijieEEEMIB.setRevisions(
        ("2012-10-16 00:00",
         "2012-10-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieEEEConfigMIBObjects_ObjectIdentity = ObjectIdentity
ruijieEEEConfigMIBObjects = _RuijieEEEConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 119, 1)
)
_RuijieEEETable_Object = MibTable
ruijieEEETable = _RuijieEEETable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 119, 1, 1)
)
if mibBuilder.loadTexts:
    ruijieEEETable.setStatus("current")
_RuijieEEEEntry_Object = MibTableRow
ruijieEEEEntry = _RuijieEEEEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 119, 1, 1, 1)
)
ruijieEEEEntry.setIndexNames(
    (0, "RUIJIE-EEE-MIB", "ruijieEEEifIndex"),
)
if mibBuilder.loadTexts:
    ruijieEEEEntry.setStatus("current")


class _RuijieEEEifIndex_Type(Integer32):
    """Custom type ruijieEEEifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RuijieEEEifIndex_Type.__name__ = "Integer32"
_RuijieEEEifIndex_Object = MibTableColumn
ruijieEEEifIndex = _RuijieEEEifIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 119, 1, 1, 1, 1),
    _RuijieEEEifIndex_Type()
)
ruijieEEEifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEEEifIndex.setStatus("current")


class _RuijieEEEAdminEnable_Type(Integer32):
    """Custom type ruijieEEEAdminEnable based on Integer32"""
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


_RuijieEEEAdminEnable_Type.__name__ = "Integer32"
_RuijieEEEAdminEnable_Object = MibTableColumn
ruijieEEEAdminEnable = _RuijieEEEAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 119, 1, 1, 1, 2),
    _RuijieEEEAdminEnable_Type()
)
ruijieEEEAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijieEEEAdminEnable.setStatus("current")


class _RuijieEEEOperEnable_Type(Integer32):
    """Custom type ruijieEEEOperEnable based on Integer32"""
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


_RuijieEEEOperEnable_Type.__name__ = "Integer32"
_RuijieEEEOperEnable_Object = MibTableColumn
ruijieEEEOperEnable = _RuijieEEEOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 119, 1, 1, 1, 3),
    _RuijieEEEOperEnable_Type()
)
ruijieEEEOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieEEEOperEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-EEE-MIB",
    **{"ruijieEEEMIB": ruijieEEEMIB,
       "ruijieEEEConfigMIBObjects": ruijieEEEConfigMIBObjects,
       "ruijieEEETable": ruijieEEETable,
       "ruijieEEEEntry": ruijieEEEEntry,
       "ruijieEEEifIndex": ruijieEEEifIndex,
       "ruijieEEEAdminEnable": ruijieEEEAdminEnable,
       "ruijieEEEOperEnable": ruijieEEEOperEnable}
)
