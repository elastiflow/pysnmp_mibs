# SNMP MIB module (CISCO-HARDWARE-IP-VERIFY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-HARDWARE-IP-VERIFY-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:28:31 2025
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

ciscoHardwareIpVerifyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804)
)
if mibBuilder.loadTexts:
    ciscoHardwareIpVerifyMIB.setRevisions(
        ("2012-09-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoHardwareIpVerifyMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoHardwareIpVerifyMIBNotifs = _CiscoHardwareIpVerifyMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 0)
)
_CiscoHardwareIpVerifyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoHardwareIpVerifyMIBObjects = _CiscoHardwareIpVerifyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1)
)
_ChivIpVerifyTable_Object = MibTable
chivIpVerifyTable = _ChivIpVerifyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1)
)
if mibBuilder.loadTexts:
    chivIpVerifyTable.setStatus("current")
_ChivIpVerifyEntry_Object = MibTableRow
chivIpVerifyEntry = _ChivIpVerifyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1)
)
chivIpVerifyEntry.setIndexNames(
    (0, "CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckIpType"),
    (0, "CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckTypeName"),
)
if mibBuilder.loadTexts:
    chivIpVerifyEntry.setStatus("current")


class _ChivIpVerifyCheckIpType_Type(Integer32):
    """Custom type chivIpVerifyCheckIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_ChivIpVerifyCheckIpType_Type.__name__ = "Integer32"
_ChivIpVerifyCheckIpType_Object = MibTableColumn
chivIpVerifyCheckIpType = _ChivIpVerifyCheckIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 1),
    _ChivIpVerifyCheckIpType_Type()
)
chivIpVerifyCheckIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chivIpVerifyCheckIpType.setStatus("current")


class _ChivIpVerifyCheckTypeName_Type(Integer32):
    """Custom type chivIpVerifyCheckTypeName based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("addressSrcBroadcast", 1),
          ("addressSrcMulticast", 2),
          ("addressDestZero", 3),
          ("addressIdentical", 4),
          ("addressSrcReserved", 5),
          ("addressClassE", 6),
          ("checksum", 7),
          ("protocol", 8),
          ("fragment", 9),
          ("lengthMinimum", 10),
          ("lengthConsistent", 11),
          ("lengthMaximumFragment", 12),
          ("lengthMaximumUdp", 13),
          ("lengthMaximumTcp", 14),
          ("tcpFlags", 15),
          ("tcpTinyFlags", 16),
          ("version", 17))
    )


_ChivIpVerifyCheckTypeName_Type.__name__ = "Integer32"
_ChivIpVerifyCheckTypeName_Object = MibTableColumn
chivIpVerifyCheckTypeName = _ChivIpVerifyCheckTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 2),
    _ChivIpVerifyCheckTypeName_Type()
)
chivIpVerifyCheckTypeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chivIpVerifyCheckTypeName.setStatus("current")


class _ChivIpVerifyCheckStatus_Type(Integer32):
    """Custom type chivIpVerifyCheckStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ChivIpVerifyCheckStatus_Type.__name__ = "Integer32"
_ChivIpVerifyCheckStatus_Object = MibTableColumn
chivIpVerifyCheckStatus = _ChivIpVerifyCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 3),
    _ChivIpVerifyCheckStatus_Type()
)
chivIpVerifyCheckStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chivIpVerifyCheckStatus.setStatus("current")
_ChivIpVerifyPacketsDropped_Type = Counter64
_ChivIpVerifyPacketsDropped_Object = MibTableColumn
chivIpVerifyPacketsDropped = _ChivIpVerifyPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 1, 1, 1, 4),
    _ChivIpVerifyPacketsDropped_Type()
)
chivIpVerifyPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chivIpVerifyPacketsDropped.setStatus("current")
_CiscoHardwareIpVerifyMIBConform_ObjectIdentity = ObjectIdentity
ciscoHardwareIpVerifyMIBConform = _CiscoHardwareIpVerifyMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 2)
)
_CiscoHardwareIpVerifyMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoHardwareIpVerifyMIBCompliances = _CiscoHardwareIpVerifyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 1)
)
_CiscoHardwareIpVerifyMIBGroups_ObjectIdentity = ObjectIdentity
ciscoHardwareIpVerifyMIBGroups = _CiscoHardwareIpVerifyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 2)
)

# Managed Objects groups

ciscoHardwareIpVerifyMIBStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 2, 1)
)
ciscoHardwareIpVerifyMIBStatisticGroup.setObjects(
      *(("CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyCheckStatus"),
        ("CISCO-HARDWARE-IP-VERIFY-MIB", "chivIpVerifyPacketsDropped"))
)
if mibBuilder.loadTexts:
    ciscoHardwareIpVerifyMIBStatisticGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoHardwareIpVerifyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 804, 2, 1, 1)
)
ciscoHardwareIpVerifyMIBCompliance.setObjects(
    ("CISCO-HARDWARE-IP-VERIFY-MIB", "ciscoHardwareIpVerifyMIBStatisticGroup")
)
if mibBuilder.loadTexts:
    ciscoHardwareIpVerifyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-HARDWARE-IP-VERIFY-MIB",
    **{"ciscoHardwareIpVerifyMIB": ciscoHardwareIpVerifyMIB,
       "ciscoHardwareIpVerifyMIBNotifs": ciscoHardwareIpVerifyMIBNotifs,
       "ciscoHardwareIpVerifyMIBObjects": ciscoHardwareIpVerifyMIBObjects,
       "chivIpVerifyTable": chivIpVerifyTable,
       "chivIpVerifyEntry": chivIpVerifyEntry,
       "chivIpVerifyCheckIpType": chivIpVerifyCheckIpType,
       "chivIpVerifyCheckTypeName": chivIpVerifyCheckTypeName,
       "chivIpVerifyCheckStatus": chivIpVerifyCheckStatus,
       "chivIpVerifyPacketsDropped": chivIpVerifyPacketsDropped,
       "ciscoHardwareIpVerifyMIBConform": ciscoHardwareIpVerifyMIBConform,
       "ciscoHardwareIpVerifyMIBCompliances": ciscoHardwareIpVerifyMIBCompliances,
       "ciscoHardwareIpVerifyMIBCompliance": ciscoHardwareIpVerifyMIBCompliance,
       "ciscoHardwareIpVerifyMIBGroups": ciscoHardwareIpVerifyMIBGroups,
       "ciscoHardwareIpVerifyMIBStatisticGroup": ciscoHardwareIpVerifyMIBStatisticGroup}
)
